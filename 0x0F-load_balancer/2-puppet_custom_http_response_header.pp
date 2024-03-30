# Installs Nginx server with custome HTTP header

package { 'nginx':
  ensure  => installed,
}

exec { 'install_nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  path     => '/usr/bin:/bin',
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
