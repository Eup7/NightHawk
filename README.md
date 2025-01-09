 (NightHawk Scanner)
一款功能强大的网络侦察工具，支持目录扫描、子域名扫描和端口扫描。

✨ 功能特点
🚀 多线程扫描，提升扫描速度
🌐 目录扫描：快速发现网站目录结构
  - 内置丰富的目录字典，包含常见敏感路径
  - 支持多种目录类型的定向扫描
  - 智能识别后台、API、配置文件等敏感目录
🔍 子域名扫描：自动发现相关子域名
🔒 端口扫描：检测开放端口和服务
🔑 代理支持：支持 HTTP/SOCKS 代理
📊 延迟检测：自动检测目标延迟
🎨 彩色输出：清晰直观的扫描结果

🚀 安装方法

# 克隆项目
git clone https://github.com/Eup7/NightHawk.git

# 进入目录
cd NightHawk

# 创建并激活虚拟环境
python3 -m venv venv

# Linux/Mac激活虚拟环境
source venv/bin/activate

# Windows激活虚拟环境
# .\venv\Scripts\activate

# 安装依赖
pip3 install -r requirements.txt

📖 使用方法

# 全功能扫描
python3 main.py -u https://example.com

# 目录扫描模式
python3 main.py -u https://example.com -m dir   # 常规目录扫描
python3 main.py -u https://example.com -m dir --type admin  # 扫描管理后台
python3 main.py -u https://example.com -m dir --type api    # 扫描API接口
python3 main.py -u https://example.com -m dir --type backup # 扫描备份文件
python3 main.py -u https://example.com -m dir --type sensitive # 扫描敏感目录

# 子域名扫描
python3 main.py -u https://example.com -m sub

# 端口扫描
python3 main.py -u https://example.com -m port

# 使用代理
python3 main.py -u https://example.com -p http://127.0.0.1:7890

# 自定义线程数
python3 main.py -u https://example.com -t 20

参数说明
-u, --url      目标网站URL（必需）
-m, --mode     扫描模式（dir/sub/port/all）
-t, --threads  线程数（默认：10）
-p, --proxy    代理服务器
--type         目录扫描类型（可选：admin/api/backup/sensitive/cms/framework等）

目录扫描类型
- admin: 管理后台目录
- user: 用户相关目录
- media: 媒体文件目录
- backup: 备份文件目录
- sensitive: 敏感目录
- cms: CMS相关目录
- framework: 框架相关目录
- devops: DevOps工具目录
- api: API接口目录
- debug: 调试相关目录
- info_leak: 信息泄露目录
- server_admin: 服务器管理目录

🛡️ 免责声明
本工具仅用于授权的安全测试，使用本工具进行未经授权的测试可能违反相关法律法规。使用本工具即表示您同意：
- 仅将本工具用于授权的安全测试
- 不将本工具用于任何非法用途
- 对使用本工具造成的任何后果负责

📝 更新日志
v1.0
✨ 首次发布
🚀 支持目录扫描
  - 新增多种目录扫描类型
  - 支持定向扫描功能
🔍 支持子域名扫描
🔒 支持端口扫描
🔑 支持代理功能
📊 支持延迟检测

🤝 贡献
欢迎提交 Issue 和 Pull Request！

📜 开源协议
本项目采用 MIT 协议开源，详见 LICENSE 文件。

👨‍💻 作者
作者: Eup7
项目地址: https://github.com/Eup7/NightHawk

