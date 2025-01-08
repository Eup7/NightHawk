import requests
import json
import time
from fake_useragent import UserAgent

class ProxyManager:
    def __init__(self):
        self.proxy = None
        self.user_agent = UserAgent().random
        self.ip_info = None
        self.latency = None

    def set_proxy(self, proxy):
        """设置代理
        格式: http://user:pass@host:port 或 http://host:port
        """
        if proxy:
            self.proxy = {
                'http': proxy,
                'https': proxy
            }
            print("\033[33m[*] 正在测试代理连接...\033[0m")
            if self.test_latency():
                print(f"\033[32m[+] 代理连接成功! 延迟: {self.latency:.2f}ms\033[0m")
                return True
            else:
                print("\033[31m[-] 代理连接失败\033[0m")
                return False

    def get_headers(self):
        """获取随机User-Agent的请求头"""
        return {
            'User-Agent': self.user_agent
        }

    def test_latency(self):
        """测试代理延迟"""
        try:
            start_time = time.time()
            response = requests.get(
                'http://www.baidu.com', 
                proxies=self.proxy,
                headers=self.get_headers(),
                timeout=10
            )
            if response.status_code == 200:
                self.latency = (time.time() - start_time) * 1000  # 转换为毫秒
                return True
            return False
        except Exception as e:
            print(f"\033[31m[-] 代理测试错误: {str(e)}\033[0m")
            return False

    def check_proxy(self):
        """检查代理是否可用并获取IP信息"""
        try:
            print("\033[33m[*] 正在获取代理IP信息...\033[0m")
            response = requests.get(
                'http://ip-api.com/json/', 
                proxies=self.proxy,
                headers=self.get_headers(),
                timeout=10
            )
            self.ip_info = response.json()
            if self.ip_info.get('status') == 'success':
                return True
            print("\033[31m[-] 无法获取IP信息\033[0m")
            return False
        except Exception as e:
            print(f"\033[31m[-] IP信息获取失败: {str(e)}\033[0m")
            return False

    def print_ip_info(self):
        """打印IP信息"""
        if not self.ip_info:
            print("\033[31m[-] 无法获取IP信息\033[0m")
            return

        print("\n\033[36m" + "=" * 50)
        print(" 代理服务器信息")
        print("=" * 50)
        print(f"[*] IP地址: {self.ip_info.get('query', 'Unknown')}")
        print(f"[*] 国家/地区: {self.ip_info.get('country', 'Unknown')}")
        print(f"[*] 城市: {self.ip_info.get('city', 'Unknown')}")
        print(f"[*] ISP: {self.ip_info.get('isp', 'Unknown')}")
        print(f"[*] 位置: {self.ip_info.get('lat', 'Unknown')}, {self.ip_info.get('lon', 'Unknown')}")
        print(f"[*] 延迟: {self.latency:.2f}ms")
        print("=" * 50 + "\033[0m\n") 