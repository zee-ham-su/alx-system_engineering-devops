# 1-user_limit.pp

user { 'holberton':
  ensure     => present,
  home       => '/home/holberton', # Set the home directory
  managehome => true,
}

exec { 'change-os-configuration-for-holberton-user':
  command   => 'usermod -s /bin/bash holberton',
  path      => '/usr/sbin:/usr/bin:/sbin:/bin',
  logoutput => true,
}

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton hard nofile 4096\n",
  mode    => '0644',
}