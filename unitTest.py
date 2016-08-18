import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
netIP = "192.168.2."
def pingSweep():  
                #this is very obvious and should be blocked by internal security considering how it sends all 256 requests at once.
		conf.verb = 0
		for num in range(0, 256): 
			layerIP = IP(dst = netIP + str(num))
                	layerICMP = ICMP()/"Boo!"
                	newPacket = layerIP/layerICMP
                	reply = sr1(newPacket, timeout = 2)
                	if not (reply is None):
                	        print reply.src + " is up"

def pingHost(target):
                conf.verb = 0
                layerIP = IP(dst = target)
                layerICMP = ICMP()/"Knock Knock"
                newPacket = layerIP/layerICMP
                reply = sr1(newPacket, timeout = 4)
                if not (reply is None):
                        print reply.src + " is up"
def scanNetwork(*args):
	conf.verb = 0
        #tcp syn said ports 
	sourceDict = {} 
	print "Host and open ports  (blank if nothing)"
        for num in range(0, 10):	 
        	for port in args:
                	layerIP = IP(dst = netIP + str(num))
                        layerTCP = TCP(flags = 'S', dport = port)
                        newPacket = layerIP/layerTCP
                        reply = sr1(newPacket, timeout = 2)
                	if not (reply is None):
				if not ((netIP + str(num)) in sourceDict):
					sourceDict[netIP + str(num)] = []
                        	sourceDict[reply.src].append(reply.sport) 
		if (bool(sourceDict)):
			print sourceDict
		sourceDict = {}  
def scanHost(target, *args):
	conf.verb = 0
	sourceDict = {} 
	for port in args:
		layerIP = IP(dst = target) 
		layerTCP = TCP(dport = port, flags = 'S') 
		newPacket = layerIP/layerTCP 
		reply = sr1(newPacket, timeout = 4) 
		if not (reply is None):
			if not(reply.src in sourceDict):
				sourceDict[reply.src] = [] 
			sourceDict[reply.src].append(reply.sport)
			
	if (bool(sourceDict)):
		print sourceDict 
		 
#pingSweep()
#pingHost("192.168.2.1")
#scanNetwork(80, 22, 1, 40)
scanHost("192.168.2.1", 80)
