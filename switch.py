import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from SwitchBox import SwitchBox
import argparse

def main():
	
	s = SwitchBox("192.168.2.", 0)
	s.pingSweep()

main()   
	
