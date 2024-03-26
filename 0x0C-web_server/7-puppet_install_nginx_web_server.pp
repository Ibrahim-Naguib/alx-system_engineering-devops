# Install Nginx
package { 'nginx':
  ensure  => installed,
}

exec { 'install_nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  path     => '/usr/bin:/bin',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

exec { 'echo':
  path    => '/usr/bin:/bin',
  command => 'echo "server { listen 80; listen [::]:80 default_server; root /var/www/html; index index.html index.htm index.nginx-debian.html; server_name _; location /redirect_me { return 301  https://www.youtube.com/watch?v=QH2-TGUlwu4; } error_page 404 /404.html; location /404.html { root /var/www/html; internal; } }" > /etc/nginx/sites-available/default'
}

service { 'nginx':
  ensure  => running,
}
