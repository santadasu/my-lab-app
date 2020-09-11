import sys
import subprocess
import csv
import paramiko
import os

def ssh(hostname, user, passwd):

   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   # ssh.load_system_host_keys()
   ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
   ssh.connect(hostname, username=user, password=passwd, port=22)
   
   ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("last")
   exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 

   for line in ssh_stdout:
     print(line.strip())


def printSshResult(hostname, user, password):
    print("printsshresult "+ hostname)
    print(" user= "+ user)
    print(" paddword= "+ password)
    statusOfssh = ssh(hostname, user, password)

    #statusOfPing = ping(hostname)
    #
    #if (statusOfPing == 'host_not_found') :
        #writeToFile('server-not-found.txt', hostname)
    #elif (statusOfPing == 'unreacheable') :
       #writeToFile('unreachable.txt', hostname)
    #elif (statusOfPing == 'timed_out') :
       #writeToFile('timed_out.txt', hostname)	   
    #elif (statusOfPing == 'ok') :
        #writeToFile('ok.txt', hostname)
    #endIf
#endPing


def writeToFile(filename, data) :
    with open(filename, 'a') as output:
        output.write(data + '\n')
    #endWith
#endDef    


'''
servers.txt example
   vm8558
   host2
   server873
   google.com
'''
file = open('servers.txt')

try:
    reader = csv.reader(file)
    
    for item in reader:
        printSshResult(item[0].strip(), item[1].strip(), item[2].strip() )
    #endFor
finally:
    file.close()
#endTry
