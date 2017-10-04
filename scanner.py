import socket, os, re
from ping import *
from Tkinter import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))

# opens file with name of "people.txt"
f = open("people.txt", "r")

ip = s.getsockname()[0]

lines = []
data = []

# Get the Local IP
end = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', ip)

# Chop down the last IP Digits
create_ip = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.', ip)

# Print IP to the user
print "Your IP Address is: " + str(end.group(0))


# Pinging the IP
def ping(ip):
    if verbose_ping(ip) == True:
        return 1
    else:
        return 0


# Check IP
def CheckLoopBack(ip):
    if (end.group(0) == '127.0.0.1'):
        return True
        print "Either your IP is a Loop Back or it does not belong in local IP range"


def getFileData():
    while 1:
        line = f.readline()
        if not line: break
        temp = str(line).rstrip()
        temp = temp + " 0"
        lines.append(temp)
    f.close()


def getNames():
    while 1:
        temp = str(lines.pop())
        data.append(temp.split(" "))
        if len(lines) == 0:
            break


def printUsers():
    print data[2]
    print data[1]
    print data[0]

print "Pinging IP's..."
getFileData()
getNames()

root = Tk()
v={}
l={}

for x in range(0,len(data)):
    v["var{0}".format(x)]=StringVar()
    l["num{0}".format(x)]=Label(root,textvariable = v["var{0}".format(x)],font=("Helvetica", 40))
    l["num{0}".format(x)].pack()

if (CheckLoopBack(create_ip)):
	print "Either your IP is a Loop Back or it does not belong in local IP range"
else:
	while 1:
		for i in range(0, len(data)):
			data[i][2] = ping(data[i][1])
			if data[i][2] == 1:
				temp = "Online"
				l["num{0}".format(i)].config(fg="green")
			else:
				temp = "Offline"
				l["num{0}".format(i)].config(fg="red")
			v["var{0}".format(i)].set(data[i][0] + ' is ' + temp)
			root.update_idletasks()