# install flask from pip3
package { 'flask':
  ensure   => 'present',
  name     => 'flask~=2.2.0',
  provider => 'pip3',
}
