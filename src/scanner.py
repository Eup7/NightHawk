import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import logging
from datetime import datetime
from .dir_dict import DirDict
from .proxy_utils import ProxyManager
import time

class DirectoryScanner:
    def __init__(self, base_url, wordlist_file=None, threads=10, proxy=None):
        self.base_url = base_url.rstrip('/')
        self.wordlist_file = wordlist_file
        self.threads = threads
        self.found_dirs = []
        self.dir_dict = DirDict()
        self.proxy_manager = ProxyManager()
        if proxy:
            self.proxy_manager.set_proxy(proxy)

    def load_wordlist(self):
        if self.wordlist_file:
            try:
                with open(self.wordlist_file, 'r') as f:
                    return [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"\033[31m[-] 错误: 找不到字典文件 {self.wordlist_file}\033[0m")
                return []
        else:
            # 使用内置字典
            return self.dir_dict.get_all()

    def scan_url(self, path):
        url = urljoin(self.base_url, path)
        try:
            response = requests.get(
                url, 
                timeout=5,
                proxies=self.proxy_manager.proxy,
                headers=self.proxy_manager.get_headers()
            )
            if response.status_code == 200:
                print(f"\033[38;5;82m[+] 发现目录: {url} (状态码: {response.status_code})\033[0m")
                self.found_dirs.append(url)
            elif response.status_code == 403:
                print(f"\033[38;5;208m[!] 访问禁止: {url} (状态码: {response.status_code})\033[0m")
        except requests.RequestException:
            pass

    def check_target_latency(self):
        """检测目标网站延迟"""
        try:
            print("\033[33m[*] 正在检测目标网站延迟...\033[0m")
            start_time = time.time()
            response = requests.get(
                self.base_url,
                timeout=5,
                proxies=self.proxy_manager.proxy,
                headers=self.proxy_manager.get_headers()
            )
            latency = (time.time() - start_time) * 1000  # 转换为毫秒
            if response.status_code == 200:
                print(f"\033[32m[+] 目标网站连接成功! 延迟: {latency:.2f}ms\033[0m")
                return True
            else:
                print(f"\033[31m[-] 目标网站响应异常 (状态码: {response.status_code})\033[0m")
                return False
        except Exception as e:
            print(f"\033[31m[-] 目标网站连接失败: {str(e)}\033[0m")
            return False

    def start_scan(self):
        """开始扫描"""
        # 首先检测目标延迟
        if not self.check_target_latency():
            print("\033[31m[-] 无法连接到目标网站，扫描终止\033[0m")
            return

        paths = self.load_wordlist()
        if not paths:
            print("\033[31m[-] 错误: 字典文件不存在或为空\033[0m")
            return

        print(f"\033[38;5;82m[*] 待扫描路径总数: {len(paths)}")
        print("[*] 扫描进行中...\033[0m\n")

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_url, paths)

        print(f"\n\033[38;5;82m{'=' * 40}")
        print(f"[+] 扫描完成!")
        print(f"[+] 共发现目录数量: {len(self.found_dirs)}")
        print(f"{'=' * 40}\033[0m")

    def save_results(self):
        """保存扫描结果到文件"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        result_file = f"results_{timestamp}.txt"
        
        with open(result_file, 'w') as f:
            f.write(f"扫描结果 - {self.base_url}\n")
            f.write("=" * 50 + "\n")
            for url in self.found_dirs:
                f.write(f"{url}\n") 