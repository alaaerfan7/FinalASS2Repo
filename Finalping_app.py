import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    
    #call(...): Runs a command, waits for it to complete, then returns the return code.
 #if the command provided above is equal to 0, show the msg succeccfully pinged, else ping failed)
    if subprocess.call(command) == 0:
        msg = 'Ping  ' + host +  ' successfully :)'    #the msg will show that the ping was successfull
    else:
        msg= 'Ping  ' + host +  ' failed :('        #the msg will show that the ping failed

    return msg

#a list that consists of name of containers+IP addresses
mylist=['Assigncontainer2','172.28.0.4','Assigncontainer3','172.28.0.3','Assigncontainer4','172.28.0.2']
#a for loop that will run through the list
for mylist in mylist:           
    
    print('\n',ping(mylist),'\n')


