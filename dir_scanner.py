import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

class DirectoryScanner:
    def __init__(self, base_url, wordlist_file, threads=10):
        self.base_url = base_url.rstrip('/')
        self.wordlist_file = wordlist_file
        self.threads = threads
        self.found_dirs = []

    def load_wordlist(self):
        try:
            with open(self.wordlist_file, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"错误: 找不到字典文件 {self.wordlist_file}")
            return []

    def scan_url(self, path):
        url = urljoin(self.base_url, path)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] 发现目录: {url} (状态码: {response.status_code})")
                self.found_dirs.append(url)
            elif response.status_code == 403:
                print(f"[!] 禁止访问: {url} (状态码: {response.status_code})")
        except requests.RequestException:
            pass

    def start_scan(self):
        paths = self.load_wordlist()
        if not paths:
            return

        print(f"\n开始扫描网站: {self.base_url}")
        print(f"使用字典文件: {self.wordlist_file}")
        print(f"线程数: {self.threads}\n")

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_url, paths)

        print("\n扫描完成!")
        print(f"共发现 {len(self.found_dirs)} 个可访问目录")

def main():
    parser = argparse.ArgumentParser(description='网站目录扫描工具')
    parser.add_argument('-u', '--url', required=True, help='目标网站URL')
    parser.add_argument('-w', '--wordlist', required=True, help='字典文件路径')
    parser.add_argument('-t', '--threads', type=int, default=10, help='线程数 (默认: 10)')
    
    args = parser.parse_args()
    
    scanner = DirectoryScanner(args.url, args.wordlist, args.threads)
    scanner.start_scan()

if __name__ == '__main__':
    main() 