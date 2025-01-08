class DirDict:
    def __init__(self):
        self.directories = [
            # 后台管理
            'admin', 'administrator', 'admincp', 'admins', 'admin-console',
            'manage', 'manager', 'management', 'backend', 'dashboard',
            'wp-admin', 'wp-login.php', 'admin.php', 'admin.html', 'admin.asp',
            'administrator.php', 'login.php', 'login.html', 'login.asp',
            'admin_login', 'admin_area', 'admin_panel', 'adminpanel',
            'cpanel', 'webadmin', 'control', 'console', 'master',
            
            # 用户相关
            'user', 'users', 'member', 'members', 'profile', 'account',
            'accounts', 'register', 'signup', 'login', 'logout', 'password',
            'forgot-password', 'reset-password', 'usercp', 'usercenter',
            'auth', 'authentication', 'signin', 'signout', 'home',
            
            # 内容管理
            'content', 'posts', 'pages', 'articles', 'blog', 'news',
            'category', 'categories', 'tag', 'tags', 'topics', 'archive',
            'archives', 'post', 'page', 'article', 'blog-post', 'feed',
            'rss', 'atom', 'comments', 'review', 'reviews',
            
            # 媒体文件
            'upload', 'uploads', 'media', 'static', 'assets', 'images',
            'img', 'css', 'js', 'javascript', 'styles', 'fonts', 'flash',
            'download', 'downloads', 'file', 'files', 'document', 'documents',
            'pdf', 'docs', 'documentation', 'resources', 'resource',
            
            # 电子商务
            'shop', 'store', 'cart', 'checkout', 'order', 'orders',
            'product', 'products', 'catalog', 'category', 'categories',
            'payment', 'pay', 'invoice', 'shipping', 'discount', 'sale',
            'buy', 'purchase', 'transactions', 'market', 'marketplace',
            
            # API接口
            'api', 'api/v1', 'api/v2', 'api/v3', 'api/latest', 'rest',
            'graphql', 'swagger', 'docs', 'documentation', 'developer',
            'dev', 'sdk', 'interface', 'service', 'services', 'endpoint',
            'endpoints', 'webservice', 'soap', 'wsdl', 'xml',
            
            # 系统配置
            'config', 'configuration', 'settings', 'setup', 'install',
            'wp-config', 'wp-config.php', 'wp-includes', 'wp-content',
            'phpinfo.php', 'info.php', 'php.php', 'test.php', 'web.config',
            '.env', '.git', '.svn', '.htaccess', 'robots.txt', 'sitemap.xml',
            
            # 数据库相关
            'database', 'db', 'mysql', 'phpmyadmin', 'phpMyAdmin',
            'myadmin', 'sql', 'mysqli', 'oracle', 'postgres', 'mongodb',
            'redis', 'memcached', 'sqlite', 'mariadb', 'pgsql',
            
            # 备份文件
            'backup', 'backups', 'bak', 'back', 'old', '.old', '.bak',
            '.backup', '_backup', 'backup1', 'backup2', '~backup',
            'wp-backup', 'sql-backup', 'db-backup', 'site-backup',
            'archive', 'archives', 'dump', 'sql-dump', 'db-dump',
            
            # 临时文件
            'temp', 'tmp', 'temporary', 'cache', '.tmp', '.temp',
            'test', 'testing', 'beta', 'dev', 'development', 'staging',
            'preview', 'demo', 'sandbox', 'example', 'sample', 'draft',
            
            # 日志文件
            'log', 'logs', 'error_log', 'error.log', 'debug.log',
            'access_log', 'access.log', 'web.log', 'weblog', 'system.log',
            'syslog', 'event.log', 'events.log', 'security.log',
            
            # 安全相关
            'security', 'secure', 'ssl', 'cert', 'certificate',
            'private', 'confidential', 'admin_files', 'secret',
            'password', 'passwords', 'key', 'keys', 'token', 'tokens',
            
            # 常见CMS
            # WordPress
            'wp', 'wp-admin', 'wp-content', 'wp-includes', 'wp-login.php',
            'wp-config.php', 'wp-cron.php', 'wp-blog', 'wordpress',
            'wp-json', 'wp-content/plugins', 'wp-content/themes',
            # Joomla
            'administrator', 'joomla', 'cms', 'portal', 'site',
            'components', 'modules', 'templates', 'installation',
            # Drupal
            'drupal', 'sites', 'modules', 'themes', 'node',
            'includes', 'misc', 'profiles', 'scripts',
            
            # 框架特征
            # Laravel
            'laravel', 'public', 'resources', 'storage', 'vendor',
            'artisan', '.env', 'composer.json', 'routes', 'app',
            # ThinkPHP
            'application', 'runtime', 'think', 'extend', 'vendor',
            # Django
            'django', 'static', 'media', 'templates', 'apps',
            'migrations', 'fixtures', 'requirements.txt',
            
            # 其他敏感目录
            'admin/config', 'admin/db', 'admin/logs', 'admin/backup',
            'system/config', 'system/logs', 'system/backup',
            'includes/config', 'includes/db', 'includes/logs',
            'data/config', 'data/db', 'data/logs', 'data/backup',
            
            # 其他常见目录
            'cgi-bin', 'includes', 'common', 'lib', 'library',
            'inc', 'include', 'core', 'data', 'system',
            'templates', 'themes', 'modules', 'plugins', 'components',
            'ajax', 'json', 'xml', 'rss', 'feed', 'sitemap',
            'robots.txt', 'favicon.ico', '.htaccess', 'web.config',
            
            # 漏洞利用相关
            'shell', 'shells', 'backdoor', 'hack', 'webshell',
            'cmd', 'command', 'exec', 'system', 'eval', 'phpinfo',
            'test', 'debug', 'proxy', 'vpn', 'tunnel', 'connect'
        ]

    def get_all(self):
        """获取所有目录"""
        return list(set(self.directories))  # 去重

    def get_admin_dirs(self):
        """获取管理后台相关目录"""
        return [d for d in self.directories if any(x in d for x in ['admin', 'manage', 'dashboard', 'control'])]

    def get_user_dirs(self):
        """获取用户相关目录"""
        return [d for d in self.directories if any(x in d for x in ['user', 'member', 'account', 'profile'])]

    def get_media_dirs(self):
        """获取媒体文件相关目录"""
        return [d for d in self.directories if any(x in d for x in ['upload', 'media', 'image', 'static', 'file'])]

    def get_backup_dirs(self):
        """获取备份文件相关目录"""
        return [d for d in self.directories if any(x in d for x in ['backup', 'bak', 'old', 'dump', 'archive'])]

    def get_sensitive_dirs(self):
        """获取敏感目录"""
        return [d for d in self.directories if any(x in d for x in ['config', 'log', 'private', 'secret', 'shell', 'admin'])]

    def get_cms_dirs(self):
        """获取CMS相关目录"""
        return [d for d in self.directories if any(x in d for x in ['wp-', 'joomla', 'drupal', 'cms'])] 