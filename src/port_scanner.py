import socket
import concurrent.futures
from urllib.parse import urlparse
from src.proxy_utils import ProxyManager
import time

class PortScanner:
    def __init__(self, target, threads=10, proxy=None):
        self.target = target.strip('/')
        if self.target.startswith('http'):
            parsed = urlparse(self.target)
            self.target = parsed.netloc
        self.threads = threads
        self.open_ports = []
        self.common_ports = [
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
            993, 995, 1723, 3306, 3389, 5900, 8080
        ]
        self.proxy_manager = ProxyManager()
        if proxy:
            self.proxy_manager.set_proxy(proxy)
            if self.proxy_manager.ip_info:
                self.target = self.proxy_manager.ip_info['query']

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                service = socket.getservbyport(port)
                print(f"\033[38;5;51m[+] 发现开放端口: {port} ({service})\033[0m")
                self.open_ports.append((port, service))
            sock.close()
        except:
            pass

    def check_target_latency(self):
        try:
            print("\033[33m[*] 正在检测目标主机延迟...\033[0m")
            start_time = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((self.target, 80))
            latency = (time.time() - start_time) * 1000
            sock.close()
            
            if result == 0:
                print(f"\033[32m[+] 目标主机连接成功! 延迟: {latency:.2f}ms\033[0m")
                return True
            else:
                print(f"\033[31m[-] 目标主机连接失败\033[0m")
                return False
        except Exception as e:
            print(f"\033[31m[-] 目标主机连接失败: {str(e)}\033[0m")
            return False

    def start_scan(self):
        if not self.check_target_latency():
            print("\033[31m[-] 无法连接到目标主机，扫描终止\033[0m")
            return

        print(f"\033[38;5;51m[*] 开始扫描端口: {self.target}")
        print(f"[*] 待扫描端口数量: {len(self.common_ports)}\033[0m\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_port, self.common_ports)

        print(f"\n\033[38;5;51m{'=' * 40}")
        print(f"[+] 端口扫描完成!")
        print(f"[+] 共发现开放端口数量: {len(self.open_ports)}")
        print(f"{'=' * 40}\033[0m") 