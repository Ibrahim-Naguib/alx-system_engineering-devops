# Creates a file in /tmp.

file { 'school':
  content => 'I love Puppet'
  path    => '/tmp/school'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
