🦅 夜鹰扫描器 (NightHawk Scanner)
一款功能强大的网络侦察工具，支持目录扫描、子域名扫描和端口扫描。
✨ 功能特点
🚀 多线程扫描，提升扫描速度
🌐 目录扫描：快速发现网站目录结构
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

# 安装依赖
pip install -r requirements.txt

📖 使用方法

# 全功能扫描
python main.py -u https://example.com

# 指定扫描模式
python main.py -u https://example.com -m dir   # 仅目录扫描
python main.py -u https://example.com -m sub   # 仅子域名扫描
python main.py -u https://example.com -m port  # 仅端口扫描

# 使用代理
python main.py -u https://example.com -p http://127.0.0.1:7890

# 自定义线程数
python main.py -u https://example.com -t 20

参数说明
-u, --url      目标网站URL（必需）
-m, --mode     扫描模式（dir/sub/port/all）
-t, --threads  线程数（默认：10）
-p, --proxy    代理服务器

🛡️ 免责声明
本工具仅用于授权的安全测试，使用本工具进行未经授权的测试可能违反相关法律法规。使用本工具即表示您同意：
仅将本工具用于授权的安全测试
不将本工具用于任何非法用途
对使用本工具造成的任何后果负责
📝 更新日志
v1.0
✨ 首次发布
🚀 支持目录扫描
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
项目地址: https://github.com/Eup7/NightHawk🛡️ 免责声明
本工具仅用于授权的安全测试，使用本工具进行未经授权的测试可能违反相关法律法规。使用本工具即表示您同意：
仅将本工具用于授权的安全测试
不将本工具用于任何非法用途
对使用本工具造成的任何后果负责
📝 更新日志
v1.0
✨ 首次发布
🚀 支持目录扫描
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
项目地址: https://github.com/Eup7/NightHawk🛡️ 免责声明
本工具仅用于授权的安全测试，使用本工具进行未经授权的测试可能违反相关法律法规。使用本工具即表示您同意：
仅将本工具用于授权的安全测试
不将本工具用于任何非法用途
对使用本工具造成的任何后果负责
📝 更新日志
v1.0
✨ 首次发布
🚀 支持目录扫描
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

