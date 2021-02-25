# This puppet modify limit of request
exec { 'unlimit':
    command => 'sudo sed -i "s/15/15000/" /etc/default/ngnix;
                sudo service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
