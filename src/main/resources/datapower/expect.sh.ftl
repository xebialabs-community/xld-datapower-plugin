#!/bin/expect
#
#    THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
#    FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#



set timeout 9

set domain ${deployed.container.domain}
set host   ${deployed.container.host}
set port   ${deployed.container.RestPort}
set command ${deployed.filePath}://${deployed.fileName}

set username ${deployed.container.username}
set password ${deployed.container.password}


log_user 0

#send_user "\n#####\n# $host\n#####\n"

spawn ssh -q -o StrictHostKeyChecking=no $host

expect {
  timeout { send_user "\nFailed to get username prompt\n"; exit 1 }
  eof { send_user "\nSSH failure for $host\n"; exit 1 }
  "*gin:"
}

send "$username\n"

expect {
  timeout { send_user "\nFailed to get password prompt\n"; exit 1 }
  eof { send_user "\nSSH failure for $host\n"; exit 1 }
  "*assword"
}

send "$password\r"
#send_user "~*********~\n"

expect {
  timeout { send_user "\nLogin failed. Password incorrect.\n"; exit 1}
  "*# "
}

log_user 1
send "exec $command\r"

expect {
  timeout { send_user "\ncommand failed.\n"; exit 1}
  "*# "
}

send "exit\r"
send_user "\n"
close


