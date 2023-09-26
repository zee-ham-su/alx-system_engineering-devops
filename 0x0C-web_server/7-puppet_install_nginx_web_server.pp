# Define a class for Nginx installation and configuration
# Add the stable version of Nginx repository.
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Update the list of software packages.
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install Nginx.
package { 'nginx':
  ensure => 'installed',
}

# Allow incoming HTTP traffic.
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Adjust folder permissions for /var/www.
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Create an index file with "Hello World!" content.
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Create a custom 404 error page.
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Configure Nginx default server block.
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}

# Restart the Nginx service.
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# Ensure the Nginx service is running.
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
