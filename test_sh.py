
fp=open('network.dat','r')
while 1:
    line = fp.readline()
    if not line:
        break
    print(type(line.split()[0]),line.split()[1])
fp.close()