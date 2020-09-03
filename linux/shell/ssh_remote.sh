#!/usr/bin/expect

# 设置参数
set IP [ lindex $argv 0 ]
set PW [ lindex $argv 1 ]

# 登录远程终端
spawn ssh -o ServerAliveInterval=30 xatu@$IP


expect {
	"yes/no" {send "yes\r";exp_continue}
	"password:" {send "$PW\r"}
}

#expect "#"
#send "htop"
#ecpect eof

# 执行完之后保持交互,并不会在执行完命令后结束
interact
