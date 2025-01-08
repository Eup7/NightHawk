import dns.resolver
import concurrent.futures
from src.proxy_utils import ProxyManager
import requests
import time

class SubdomainScanner:
    def __init__(self, domain, threads=10, proxy=None):
        self.domain = domain.strip('/')
        if self.domain.startswith('http'):
            self.domain = self.domain.split('//')[1]
        self.threads = threads
        self.found_domains = []
        self.subdomains = [
            # 基础服务
            'www', 'mail', 'email', 'webmail', 'pop', 'pop3', 'imap', 'smtp',
            
            # DNS相关
            'ns1', 'ns2', 'ns3', 'ns4', 'dns', 'dns1', 'dns2',
            
            # 开发环境
            'dev', 'development', 'test', 'testing', 'staging', 'beta', 'demo',
            'sandbox', 'uat', 'qa', 'local', 'localhost',
            
            # 管理相关
            'admin', 'administrator', 'admins', 'webadmin', 'sysadmin',
            'manage', 'management', 'manager', 'portal', 'dashboard',
            
            # 应用服务
            'api', 'api-docs', 'developer', 'developers', 'dev-api',
            'app', 'apps', 'application', 'mobile', 'mobile-api',
            
            # 内容分发
            'cdn', 'static', 'assets', 'media', 'img', 'images', 'css', 'js',
            'download', 'downloads', 'upload', 'uploads',
            
            # 社区相关
            'forum', 'forums', 'community', 'bbs', 'blog', 'blogs', 'news',
            'support', 'help', 'faq', 'wiki',
            
            # 营销相关
            'shop', 'store', 'mall', 'payment', 'pay', 'cart', 'order',
            'market', 'marketing', 'ads', 'ad', 'promo',
            
            # 监控和统计
            'monitor', 'monitoring', 'status', 'stats', 'statistics',
            'analytics', 'metric', 'metrics', 'health',
            
            # 安全相关
            'secure', 'security', 'ssl', 'vpn', 'auth', 'login',
            
            # 邮件相关
            'newsletter', 'mail', 'smtp', 'pop', 'pop3', 'imap',
            'mailserver', 'mx', 'email', 'webmail',
            
            # 数据库相关
            'db', 'database', 'mysql', 'postgresql', 'oracle', 'sql',
            
            # 其他常见服务
            'ftp', 'sftp', 'ssh', 'webdisk', 'backup', 'git', 'svn',
            'jenkins', 'jira', 'confluence', 'proxy', 'gateway',
            
            # 区域和语言
            'en', 'us', 'uk', 'eu', 'asia', 'cn', 'de', 'fr', 'es',
            
            # 特殊用途
            'old', 'new', 'temp', 'tmp', 'cache', 'preview', 'stage',
            'internal', 'external', 'public', 'private', 'corp'
        ]
        self.proxy_manager = ProxyManager()
        if proxy:
            self.proxy_manager.set_proxy(proxy)

    def scan_subdomain(self, subdomain):
        try:
            domain = f"{subdomain}.{self.domain}"
            resolver = dns.resolver.Resolver()
            if self.proxy_manager.proxy:
                # 如果有代理，使用代理服务器的DNS
                resolver.nameservers = [self.proxy_manager.ip_info['query']]
            resolver.resolve(domain, 'A')
            print(f"\033[38;5;99m[+] 发现子域名: {domain}\033[0m")
            self.found_domains.append(domain)
        except:
            pass

    def check_target_latency(self):
        """检测主域名延迟"""
        try:
            print("\033[33m[*] 正在检测主域名延迟...\033[0m")
            start_time = time.time()
            response = requests.get(
                f"http://{self.domain}",
                timeout=5,
                proxies=self.proxy_manager.proxy,
                headers=self.proxy_manager.get_headers()
            )
            latency = (time.time() - start_time) * 1000
            if response.status_code == 200:
                print(f"\033[32m[+] 主域名连接成功! 延迟: {latency:.2f}ms\033[0m")
                return True
            else:
                print(f"\033[31m[-] 主域名响应异常 (状态码: {response.status_code})\033[0m")
                return False
        except Exception as e:
            print(f"\033[31m[-] 主域名连接失败: {str(e)}\033[0m")
            return False

    def start_scan(self):
        """开始扫描"""
        # 首先检测主域名延迟
        self.check_target_latency()

        print(f"\033[38;5;99m[*] 开始扫描子域名: {self.domain}")
        print(f"[*] 待扫描子域名数量: {len(self.subdomains)}\033[0m\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_subdomain, self.subdomains)

        print(f"\n\033[38;5;99m{'=' * 40}")
        print(f"[+] 子域名扫描完成!")
        print(f"[+] 共发现子域名数量: {len(self.found_domains)}")
        print(f"{'=' * 40}\033[0m") 