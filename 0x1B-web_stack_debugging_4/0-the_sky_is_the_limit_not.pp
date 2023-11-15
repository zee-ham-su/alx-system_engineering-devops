# Fix open files limit

# Use the exec resource to run a sed command, replacing the open files limit in the nginx configuration file.
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

# Restart Nginx

# Use the exec resource to restart Nginx after fixing the open files limit.
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
