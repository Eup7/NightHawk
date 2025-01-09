import argparse
from src.scanner import DirectoryScanner
from src.subdomain_scanner import SubdomainScanner
from src.port_scanner import PortScanner
import time
import sys
from src.proxy_utils import ProxyManager

def print_banner():
    banner = """
    \033[31m
    ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
    ████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝██║  ██║██╔══██╗██║    ██║██║ ██╔╝
    ██╔██╗ ██║██║██║  ███╗███████║   ██║   ███████║███████║██║ █╗ ██║█████╔╝ 
    ██║╚██╗██║██║██║   ██║██╔══██║   ██║   ██╔══██║██╔══██║██║███╗██║██╔═██╗ 
    ██║ ╚████║██║╚██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
    ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
    \033[0m
    \033[36m[*] nighthawk v1.0 - 高级网络侦察工具
    [*] 作者: Eup7
    [*] 项目地址: https://github.com/Eup7/NightHawk
    [*] 警告: 请勿用于非授权测试！\033[0m
    """
    print(banner)

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(f"\r\033[33m[*] 正在初始化... {animation[i % len(animation)]}\033[0m")
        sys.stdout.flush()
    print("\n")

def print_separator(title, color):
    width = 60
    print(f"\n{color}{'=' * width}")
    print(f"{'=' * ((width - len(title)) // 2)} {title} {'=' * ((width - len(title)) // 2)}")
    print(f"{'=' * width}\033[0m\n")

def main():
    print_banner()
    loading_animation()

    parser = argparse.ArgumentParser(description='网站扫描工具')
    parser.add_argument('-u', '--url', required=True, help='目标网站URL')
    parser.add_argument('-t', '--threads', type=int, default=10, help='线程数 (默认: 10)')
    parser.add_argument('-m', '--mode', choices=['dir', 'sub', 'port', 'all'], 
                      default='all', help='扫描模式 (dir=目录, sub=子域名, port=端口, all=全部)')
    parser.add_argument('-p', '--proxy', help='代理服务器 (格式: http://user:pass@host:port)')
    
    args = parser.parse_args()
    
    # 初始化代理
    proxy_manager = ProxyManager()
    if args.proxy:
        print(f"\033[36m[*] 正在初始化代理: {args.proxy}\033[0m")
        if not proxy_manager.set_proxy(args.proxy):
            print("\033[31m[-] 代理初始化失败，程序退出\033[0m")
            return
        
        if proxy_manager.check_proxy():
            proxy_manager.print_ip_info()
        else:
            print("\033[31m[-] 代理服务器连接失败，程序退出\033[0m")
            return

    print(f"\033[32m[+] 目标网站: {args.url}")
    print(f"[+] 线程数量: {args.threads}")
    print(f"[+] 扫描模式: {args.mode}")
    if args.proxy:
        print(f"[+] 使用代理: {args.proxy}\033[0m")

    if args.mode in ['dir', 'all']:
        print_separator("目录扫描", "\033[38;5;82m")
        dir_scanner = DirectoryScanner(args.url, 'dirs.txt', args.threads)
        dir_scanner.start_scan()

    if args.mode in ['sub', 'all']:
        print_separator("子域名扫描", "\033[38;5;99m")
        sub_scanner = SubdomainScanner(args.url, args.threads)
        sub_scanner.start_scan()

    if args.mode in ['port', 'all']:
        print_separator("端口扫描", "\033[38;5;51m")
        port_scanner = PortScanner(args.url, args.threads)
        port_scanner.start_scan()

    print("\n\033[32m[+] 所有扫描任务完成!\033[0m")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31m[-] 扫描被用户终止\033[0m")
    except Exception as e:
        print(f"\n\033[31m[-] 错误: {str(e)}\033[0m") 