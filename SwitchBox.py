#!/usr/bin/python
from scapy.all import *


class SwitchBox():
	def __init__(self, netIP, verb): 
		self.netIP = netIP #subnet IP 
		self.verb = verb
		conf.verb = verb 
		self.sourceDict = {}


	def scanNetwork(self, *args):
		#print "Host and open ports (blank if nothing, might take awhile)"
		for num in range(0, 256):
			self.scanHost(self.netIP + str(num), *args)
			#for port in args:
			#	layerIP = IP(dst = self.netIP + str(num))
			#	layerTCP = TCP(flags = 'S', dport = port)
			#	newPacket = layerIP/layerTCP
			#	reply = sr1(newPacket, timeout = 2)
 			#	self.dictManage(reply)
		    	#self.printCheck() 


	def scanHost(self, target, *args):
		#print "Host and open ports (blank if nothing)"
		for port in args:
			layerIP = IP(dst = target)
		    	layerTCP = TCP(dport = port, flags = 'S')
			newPacket = layerIP/layerTCP
			reply = sr1(newPacket, timeout = 1)
	     		self.dictManage(reply) 
	     	self.printCheck()

	def pingHost(self, target):
		layerIP = IP(dst = target)
		layerICMP = ICMP()/"Knock Knock"
		newPacket = layerIP/layerICMP
		reply = sr1(newPacket, timeout = 1)
		if not (reply is None):
			print reply.src + " is up"

	def pingSweep(self): 
		for num in range(0, 256):
			self.pingHost(self.netIP + str(num)) 
			#layerIP = IP(dst = netIP + str(num))
			#layerICMP = ICMP()/"Boo!"
			#newPacket = layerIP/layerICMP
	   		#reply = sr1(newPacket, timeout = 2)
	   		#if not (reply is None):
		   	#	print reply.src + " is up"	 
#helper functions
	def dictManage(self, reply):
		if not (reply is None):
			if not(reply.src in self.sourceDict):
				self.sourceDict[reply.src] = []
			self.sourceDict[reply.src].append(reply.sport)


	def printCheck(self):
		if (bool(self.sourceDict)):
			print self.sourceDict
			self.sourceDict = {}




