#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from SwitchBox import SwitchBox
import argparse
from os import getuid
def main():
	parser = argparse.ArgumentParser(description = "Parser for Switch", usage = "Example usage: switch -i 192.168.1. -pn") 
	parser.add_argument("-sh", metavar = "t", help="Scan Host")
	parser.add_argument("-p", metavar = "p", help="Target Ports (Default 80 and 22)")
	parser.add_argument("-sn", metavar = "sn", help="Scan Network") 
	parser.add_argument("-pi", metavar = "pi", help ="Ping Target") 
	parser.add_argument("-pn", metavar = "pn", help = "Ping Network")
	#parser.add_argument "-v", metavar = "v", help = "Verbosity(0-2)") 
	parser.add_argument("-i", metavar = "i", help="Basic IP shit", required = True) 
	args = parser.parse_args()	
	

def rootCheck(): 
	if (getuid() != 0):
		print "You must run as root" 
	else: 
		main()

rootCheck()

