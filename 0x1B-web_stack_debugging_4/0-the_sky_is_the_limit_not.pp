# Puppet Manifest: Adjust Nginx Open Files Limit and Restart

# Increase Nginx Open Files Limit

#Modify Nginx open files limit with sed.
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  }

# Restart Nginx after open files limit update

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
