class DirDict:
    def __init__(self):
        self.directories = [
            'admin', 'administrator', 'admincp', 'admins', 'admin-console',
            'manage', 'manager', 'management', 'backend', 'dashboard',
            'wp-admin', 'wp-login.php', 'admin.php', 'admin.html', 'admin.asp',
            'administrator.php', 'login.php', 'login.html', 'login.asp',
            'admin_login', 'admin_area', 'admin_panel', 'adminpanel',
            'cpanel', 'webadmin', 'control', 'console', 'master',
            'user', 'users', 'member', 'members', 'profile', 'account',
            'accounts', 'register', 'signup', 'login', 'logout', 'password',
            'forgot-password', 'reset-password', 'usercp', 'usercenter',
            'auth', 'authentication', 'signin', 'signout', 'home',
            'content', 'posts', 'pages', 'articles', 'blog', 'news',
            'category', 'categories', 'tag', 'tags', 'topics', 'archive',
            'archives', 'post', 'page', 'article', 'blog-post', 'feed',
            'rss', 'atom', 'comments', 'review', 'reviews',
            'upload', 'uploads', 'media', 'static', 'assets', 'images',
            'img', 'css', 'js', 'javascript', 'styles', 'fonts', 'flash',
            'download', 'downloads', 'file', 'files', 'document', 'documents',
            'pdf', 'docs', 'documentation', 'resources', 'resource',
            'shop', 'store', 'cart', 'checkout', 'order', 'orders',
            'product', 'products', 'catalog', 'category', 'categories',
            'payment', 'pay', 'invoice', 'shipping', 'discount', 'sale',
            'buy', 'purchase', 'transactions', 'market', 'marketplace',
            'api', 'api/v1', 'api/v2', 'api/v3', 'api/latest', 'rest',
            'graphql', 'swagger', 'docs', 'documentation', 'developer',
            'dev', 'sdk', 'interface', 'service', 'services', 'endpoint',
            'endpoints', 'webservice', 'soap', 'wsdl', 'xml',
            'config', 'configuration', 'settings', 'setup', 'install',
            'wp-config', 'wp-config.php', 'wp-includes', 'wp-content',
            'phpinfo.php', 'info.php', 'php.php', 'test.php', 'web.config',
            '.env', '.git', '.svn', '.htaccess', 'robots.txt', 'sitemap.xml',
            'database', 'db', 'mysql', 'phpmyadmin', 'phpMyAdmin',
            'myadmin', 'sql', 'mysqli', 'oracle', 'postgres', 'mongodb',
            'redis', 'memcached', 'sqlite', 'mariadb', 'pgsql',
            'backup', 'backups', 'bak', 'back', 'old', '.old', '.bak',
            '.backup', '_backup', 'backup1', 'backup2', '~backup',
            'wp-backup', 'sql-backup', 'db-backup', 'site-backup',
            'archive', 'archives', 'dump', 'sql-dump', 'db-dump',
            'temp', 'tmp', 'temporary', 'cache', '.tmp', '.temp',
            'test', 'testing', 'beta', 'dev', 'development', 'staging',
            'preview', 'demo', 'sandbox', 'example', 'sample', 'draft',
            'log', 'logs', 'error_log', 'error.log', 'debug.log',
            'access_log', 'access.log', 'web.log', 'weblog', 'system.log',
            'syslog', 'event.log', 'events.log', 'security.log',
            'security', 'secure', 'ssl', 'cert', 'certificate',
            'private', 'confidential', 'admin_files', 'secret',
            'password', 'passwords', 'key', 'keys', 'token', 'tokens',
            'wp', 'wp-admin', 'wp-content', 'wp-includes', 'wp-login.php',
            'wp-config.php', 'wp-cron.php', 'wp-blog', 'wordpress',
            'wp-json', 'wp-content/plugins', 'wp-content/themes',
            'administrator', 'joomla', 'cms', 'portal', 'site',
            'components', 'modules', 'templates', 'installation',
            'drupal', 'sites', 'modules', 'themes', 'node',
            'includes', 'misc', 'profiles', 'scripts',
            'laravel', 'public', 'resources', 'storage', 'vendor',
            'artisan', '.env', 'composer.json', 'routes', 'app',
            'application', 'runtime', 'think', 'extend', 'vendor',
            'django', 'static', 'media', 'templates', 'apps',
            'migrations', 'fixtures', 'requirements.txt',
            'admin/config', 'admin/db', 'admin/logs', 'admin/backup',
            'system/config', 'system/logs', 'system/backup',
            'includes/config', 'includes/db', 'includes/logs',
            'data/config', 'data/db', 'data/logs', 'data/backup',
            'cgi-bin', 'includes', 'common', 'lib', 'library',
            'inc', 'include', 'core', 'data', 'system',
            'templates', 'themes', 'modules', 'plugins', 'components',
            'ajax', 'json', 'xml', 'rss', 'feed', 'sitemap',
            'robots.txt', 'favicon.ico', '.htaccess', 'web.config',
            'shell', 'shells', 'backdoor', 'hack', 'webshell',
            'cmd', 'command', 'exec', 'system', 'eval', 'phpinfo',
            'test', 'debug', 'proxy', 'vpn', 'tunnel', 'connect',
            'www', 'wwwroot', 'webapp', 'webapps', 'web', 'website', 'htdocs',
            'public_html', 'sites', 'default', 'main', 'root', 'home', 'index',
            'dev', 'develop', 'development', 'test', 'testing', 'stage', 'staging',
            'uat', 'prod', 'production', 'pre-prod', 'preview', 'beta', 'alpha',
            'local', 'localhost', 'debug', 'release',
            'actuator', 'swagger-ui', 'api-docs', 'eureka', 'config-server',
            'application', 'bootstrap', 'resources', 'static', 'templates',
            'flask', 'static', 'templates', 'instance', 'blueprints',
            'node_modules', 'dist', 'build', 'public', 'src', 'app',
            'config', 'routes', 'middleware', 'controllers', 'models',
            'deploy', 'deployment', 'releases', 'versions', 'builds',
            'docker', 'kubernetes', 'k8s', 'helm', 'charts', 'manifests',
            'ansible', 'terraform', 'puppet', 'chef', 'vagrant',
            'monitor', 'monitoring', 'metrics', 'prometheus', 'grafana',
            'kibana', 'elasticsearch', 'logstash', 'beats', 'zabbix',
            'nagios', 'cacti', 'munin', 'splunk', 'graylog',
            'redis', 'memcached', 'cache', 'queue', 'rabbitmq', 'kafka',
            'activemq', 'celery', 'resque', 'beanstalkd', 'sidekiq',
            'proxy', 'nginx', 'apache', 'haproxy', 'traefik',
            'loadbalancer', 'gateway', 'cdn', 'waf', 'reverse-proxy',
            'services', 'microservices', 'service-registry', 'discovery',
            'config-server', 'api-gateway', 'auth-service', 'user-service',
            'penetration', 'pentest', 'security', 'scan', 'scanner',
            'exploit', 'vulnerability', 'audit', 'assessment', 'recon',
            '.git/HEAD', '.svn/entries', '.env.local', '.env.backup',
            'WEB-INF/web.xml', 'META-INF/MANIFEST.MF', 'composer.lock',
            'package-lock.json', 'yarn.lock', 'Gemfile.lock',
            'docs', 'documentation', 'manual', 'guide', 'tutorial',
            'help', 'faq', 'wiki', 'knowledge-base', 'support',
            'readme', 'changelog', 'license', 'about', 'contact',
            '.svn/wc.db', '.DS_Store', 'WEB-INF/database.properties',
            'config.inc.php', 'database.php', 'db.php', 'db.ini',
            'web.config.bak', 'database.yml', 'credentials.xml',
            '.idea/workspace.xml', '.vscode/settings.json',
            'manager/html', 'jmx-console', 'web-console', 'admin-console',
            'axis2-web', 'axis2-admin', 'axis2/axis2-admin',
            'websphere', 'workorder', 'supervisor', 'resin-admin',
            'application.yml', 'application.properties', '.env.production',
            'config.php.bak', 'wp-config.php.bak', '.htaccess.bak',
            'web.xml.bak', 'server.xml.bak', 'database.yml.bak',
            'upload_files', 'uploaded', 'upload_images', 'fileupload',
            'upload/image', 'upload/file', 'uploads/media', 'attachment',
            'attachments', 'upload/temp', 'tempfiles', 'userfiles',
            'api/admin', 'api/upload', 'api/user', 'api/login',
            'api/debug', 'api/test', 'api/dev', 'api/internal',
            'api/system', 'api/config', 'api/backup', 'api/logs',
            'phpmyadmin', 'phpMyAdmin', 'mysql', 'sql', 'myadmin',
            'dbadmin', 'db-admin', 'database-admin', 'mysqladmin',
            'pgadmin', 'phppgadmin', 'SQLiteManager', 'sqlbuddy',
            '.bak', '.backup', '.old', '.temp', '.tmp', '.swp',
            '.save', '~', '.copy', '.orig', '.bk', '_bak', '.back',
            'phpinfo.php', 'test.php', 'info.php', 'debug.php',
            'test.html', 'test.jsp', 'test.asp', 'probe.php',
            'status', 'server-status', 'server-info', 'test-cgi',
            '.git', '.svn', '.hg', 'CVS', '_darcs', '.bzr',
            '.git/config', '.svn/entries', '.hg/hgrc', 'CVS/Root',
            'solr', 'jenkins', 'jira', 'confluence', 'gitlab',
            'redmine', 'zentao', 'zabbix', 'nagios', 'cacti',
            'weblogic', 'websphere', 'tomcat', 'jboss', 'resin',
            'router', 'gateway', 'modem', 'switch', 'firewall',
            'cisco', 'huawei', 'h3c', 'zte', 'tplink', 'dlink',
            'netgear', 'asus', 'mikrotik', 'fortinet', 'pfsense',
            'waf', 'ids', 'ips', 'siem', 'nids', 'hids',
            'av', 'antivirus', 'firewall', 'utm', 'vpn',
            'sslvpn', 'openvpn', 'anyconnect', 'forticlient',
            'weblogic', 'websphere', 'jboss', 'tomcat', 'resin',
            'glassfish', 'jetty', 'apache', 'nginx', 'iis',
            'phpmyadmin', 'phpinfo', 'server-status', 'web.config',
            'aws', 'azure', 'gcp', 'aliyun', 'qcloud',
            's3', 'oss', 'cos', 'lambda', 'function',
            'api/v1', 'api/v2', 'api/v3', 'swagger', 'graphql',
            'oa', 'erp', 'crm', 'hr', 'mail',
            'zimbra', 'exchange', 'webmail', 'outlook', 'smtp',
            'internal', 'intranet', 'private', 'corp', 'inner',
            'zabbix', 'nagios', 'cacti', 'prometheus', 'grafana',
            'kibana', 'elasticsearch', 'logstash', 'splunk', 'nms',
            'jenkins', 'gitlab', 'svn', 'jira', 'confluence',
            'struts2', 'webshell', 'shell', 'cmd', 'command',
            'exec', 'system', 'eval', 'rce', 'lfi', 'rfi',
            'xxe', 'ssrf', 'upload', 'download', 'bypass'
        ]

    def get_all(self):
        return list(set(self.directories))

    def get_admin_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['admin', 'manage', 'dashboard', 'control'])]

    def get_user_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['user', 'member', 'account', 'profile'])]

    def get_media_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['upload', 'media', 'image', 'static', 'file'])]

    def get_backup_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['backup', 'bak', 'old', 'dump', 'archive'])]

    def get_sensitive_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['config', 'log', 'private', 'secret', 'shell', 'admin'])]

    def get_cms_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['wp-', 'joomla', 'drupal', 'cms'])]

    def get_framework_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['spring', 'flask', 'django', 'laravel', 'node'])]

    def get_devops_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['docker', 'kubernetes', 'ansible', 'jenkins', 'gitlab'])]

    def get_monitoring_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['monitor', 'prometheus', 'grafana', 'zabbix'])]

    def get_info_leak_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['.svn', '.git', '.env', 'config', 'database'])]

    def get_server_admin_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['manager', 'console', 'admin', 'supervisor'])]

    def get_debug_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['test', 'debug', 'dev', 'phpinfo'])]

    def get_api_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['api', 'rest', 'graphql', 'swagger'])]

    def get_network_device_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['router', 'switch', 'firewall', 'cisco', 'huawei'])]

    def get_security_device_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['waf', 'ids', 'ips', 'vpn', 'ssl'])]

    def get_middleware_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['weblogic', 'tomcat', 'jboss', 'apache', 'nginx'])]

    def get_internal_system_dirs(self):
        return [d for d in self.directories if any(x in d for x in ['oa', 'erp', 'crm', 'mail', 'internal'])] 