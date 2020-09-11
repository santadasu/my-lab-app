import sys
import subprocess
import csv

def ping(hostname):
    p = subprocess.Popen(["ping",hostname,"-c 3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    pingStatus = 'ok';
        
    for line in p.stdout:
        output = line.rstrip().decode('UTF-8')
        print("output=" + output)
 
        if (output.endswith('unreachable.')) :
            #No route from the local system. Packets sent were never put on the wire.
            pingStatus = 'unreacheable'
            break
        elif (output.startswith('Ping request could not find host')) :
            pingStatus = 'host_not_found'
            break
        if (output.startswith('Request timeout')) :
            #No Echo Reply messages were received within the default time of 1 second.
            pingStatus = 'timed_out'
            break
        #end if
    #endFor
    
    return pingStatus
#endDef    


def printPingResult(hostname):
    print("printpingresult "+ hostname)
    statusOfPing = ping(hostname)
    
    if (statusOfPing == 'host_not_found') :
        print("ping SRVNOTFOUND to: " +hostname)
        writeToFile('server-not-found.txt', hostname)
    elif (statusOfPing == 'unreacheable') :
        print("ping UNREACHABLE to: " +hostname)
        writeToFile('unreachable.txt', hostname)
    elif (statusOfPing == 'timed_out') :
        print("ping TIMEOUT to: " +hostname)
        writeToFile('timed_out.txt', hostname)	   
    elif (statusOfPing == 'ok') :
        print("ping OK to: " +hostname)
        writeToFile('ok.txt', hostname)
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

while(1):
    file = open('servers.txt')
    reader = csv.reader(file)
    
    for item in reader:
        printPingResult(item[0].strip())
    #endFor
    file.close()
#endTry
