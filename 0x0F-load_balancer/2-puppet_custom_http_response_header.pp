# creating a custom HTTP header response, but with Puppet

exec { 'update system':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# ngnix server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# custom header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# lunch nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
