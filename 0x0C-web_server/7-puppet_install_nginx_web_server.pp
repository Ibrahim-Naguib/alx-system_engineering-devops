# Script that installs Nginx with Puppet
exec {'install':
  provider => shell,
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx ;'
}

exec {'echo':
  path    => '/usr/bin:/bin',
  command => 'echo "Hello World!" > /var/www/html/index.html'
}

exec {'echo':
  path    => '/usr/bin:/bin',
  command => 'echo "Ceci n\'est pas une page" > /var/www/html/404.html'
}

exec {'echo':
  path    => '/usr/bin:/bin',
  command => 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location /redirect_me {
        return 301  https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404.html {
        root /var/www/html;
        internal;
    }
  }" > /etc/nginx/sites-available/default'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
