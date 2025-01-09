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
            'www', 'mail', 'email', 'webmail', 'pop', 'pop3', 'imap', 'smtp',
            'ns1', 'ns2', 'ns3', 'ns4', 'dns', 'dns1', 'dns2',
            'dev', 'development', 'test', 'testing', 'staging', 'beta', 'demo',
            'sandbox', 'uat', 'qa', 'local', 'localhost',
            'admin', 'administrator', 'admins', 'webadmin', 'sysadmin',
            'manage', 'management', 'manager', 'portal', 'dashboard',
            'api', 'api-docs', 'developer', 'developers', 'dev-api',
            'app', 'apps', 'application', 'mobile', 'mobile-api',
            'cdn', 'static', 'assets', 'media', 'img', 'images', 'css', 'js',
            'download', 'downloads', 'upload', 'uploads',
            'forum', 'forums', 'community', 'bbs', 'blog', 'blogs', 'news',
            'support', 'help', 'faq', 'wiki',
            'shop', 'store', 'mall', 'payment', 'pay', 'cart', 'order',
            'market', 'marketing', 'ads', 'ad', 'promo',
            'monitor', 'monitoring', 'status', 'stats', 'statistics',
            'analytics', 'metric', 'metrics', 'health',
            'secure', 'security', 'ssl', 'vpn', 'auth', 'login',
            'newsletter', 'mail', 'smtp', 'pop', 'pop3', 'imap',
            'mailserver', 'mx', 'email', 'webmail',
            'db', 'database', 'mysql', 'postgresql', 'oracle', 'sql',
            'ftp', 'sftp', 'ssh', 'webdisk', 'backup', 'git', 'svn',
            'jenkins', 'jira', 'confluence', 'proxy', 'gateway',
            'en', 'us', 'uk', 'eu', 'asia', 'cn', 'de', 'fr', 'es',
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
                resolver.nameservers = [self.proxy_manager.ip_info['query']]
            resolver.resolve(domain, 'A')
            print(f"\033[38;5;99m[+] 发现子域名: {domain}\033[0m")
            self.found_domains.append(domain)
        except:
            pass

    def check_target_latency(self):
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
        self.check_target_latency()

        print(f"\033[38;5;99m[*] 开始扫描子域名: {self.domain}")
        print(f"[*] 待扫描子域名数量: {len(self.subdomains)}\033[0m\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_subdomain, self.subdomains)

        print(f"\n\033[38;5;99m{'=' * 40}")
        print(f"[+] 子域名扫描完成!")
        print(f"[+] 共发现子域名数量: {len(self.found_domains)}")
        print(f"{'=' * 40}\033[0m") 