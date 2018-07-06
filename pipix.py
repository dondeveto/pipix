from urllib3 import *
from platform import system
from urllib.request import urlopen
import sys
import os

def pipix():
    print("""\033[1;36m
				███████████      ███████████       ██      ██          https://github.com/4Vic
				██       ██  ██  ██       ██  ██   ██      ██		
				██       ██      ██       ██         ██  ██
				███████████  ██  ███████████  ██     ██  ██
				██           ██  ██           ██       ██
				██           ██  ██           ██       ██
				██           ██  ██           ██     ██  ██
				██           ██  ██           ██     ██  ██
				██           ██  ██           ██   ██      ██
				██           ██  ██           ██   ██      ██
				""")
                                                               
pipix()
def mainpage():

    print(""" \033[1;31m
     Sexy?Sex  
     ?Sexy?Sexy                                 
    y?Sexy?Sexy?				
    ?Sexy?Sexy?S 		       					1)  Honeypot Detector
    ?Sexy?Sexy?S 		       					2)  DNS Lookup
   ?Sexy?Sexy?Se 		       					3)  Port Scanner
  ?Sexy?Sexy?Se 		       					4)  E-Mail Collector
  ?Sexy?Sexy?Se 		       					5)  Traceroute
  ?Sexy?Sexy?Sexy? 		       					6)  Whois Lookup
 ?Sexy?Sexy?Sexy?Sexy 		       					7)  IP Lookup
 ?Sexy?Sexy?Sexy?Sexy?Se 		       				8)  Reverse IP Lookup
 ?Sexy?Sexy?Sexy?Sexy?Sex 		      	 			9)  Subdomain Finder
  ?Sexy?  ?Sexy?Sexy?Sex 		       				10) Find Share DNS Servers
    ?Sex    ?Sexy?Sexy? 		       				11) HTTP Header
    ?Sex     ?Sexy?Sexy							12) Robots.txt
    ?Sex     ?Sexy?Sexy							13) Host Finder
     ?Sex    ?Sexy?Sexy							14) Zone Transfer
      ?Se    ?Sexy?Sex							15) Subnet Lookup
       ?Se  ?Sexy?Sexy							16) Extract Links
         ?Sexy?Sexy?Sex							17) Test ping
         ?Sexy?Sexy?sex							18) Reverse DNS Lookup
         ?Sexy?Sexy?Sexy?Se						19) Exit
         ?Sexy?Sexy?Sexy?Sexy?
         ?Sexy?Sexy?Sexy?Sexy?Sexy
         ?Sexy?Sexy?Sexy?Sexy?Sexy?S
         ?Sexy?Sexy    ?Sexy?Sexy?se           
          ?Sexy?Se       ?Sexy?Sexy?          
          ?Sexy?Se     ?Sexy?Sexy?             
          ?Sexy?S    ?Sexy?Sexy                
          ?Sexy?S ?Sexy?Sexy                   
         ?Sexy?Sexy?Sexy                                     
         ?Sexy?Sexy?S                          
         ?Sexy?Sexy                            
        ?Sexy?Se							  
        ?Sexy? 								  
       ?Sexy?    			  
       ?Sexy?      
       ?Sexy? 							  
       ?Sexy						       
       ?Sexy								   
        ?Sex							       
        ?Sex		\033[1;35m					      
        ?Sex		\033[1;35m
       ?Sexy		\033[1;35m
       ?Sexy		\033[1;35m
       |Sexy		\033[1;35m
       | Sexy		\033[1;35m
       |  SexY		\033[1;35m
	   

""")
                     																	   
mainpage()
def list():
    while True:
        
        choose = input("\033[1;36m Select Number  :")
        if choose == "19":
            print("\n","\033[1;32m See you later (づ｡◕‿‿◕｡)づ✿ ","\n")
            break

        elif choose == "1":  
            ipaddress = input("Enter the IP address  :")
            sh="https://api.shodan.io/labs/honeyscore/" + ipaddress + "?key=oxchYb8VrHJoYvLVRtid2reJa0TRStW8"
            openn = urlopen(sh).read().decode()
            print("\n","Honey Score :",openn)
            mainpage()
       
        elif choose == "2":
            ipaddress = input("Enter the IP address or hostname :")
            ht ="http://api.hackertarget.com/dnslookup/?q=" + ipaddress
            openn = urlopen(ht).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "3":
            ipaddress = input("Enter the IP address or hostname :")
            ht = "http://api.hackertarget.com/nmap/?q=" + ipaddress
            openn = urlopen(ht).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "4":
            ipaddress = input("Enter the hostname  :")
            harvest = os.getcwd()
            os.system('cd ' +  harvest  + '/modules && python2 theHarvester.py -d %s -b all' % ipaddress)
            mainpage()
            
        elif choose == "5":
            ipaddress = input("Enter the IP address or hostname  :")
            tra = "https://api.hackertarget.com/mtr/?q=" + ipaddress
            openn = urlopen(tra).read().decode()
            print (openn)
            mainpage()
            
        elif choose == "6":
            ipaddress = input("Enter the IP address or hostname  :")
            who = "http://api.hackertarget.com/whois/?q=" + ipaddress
            openn = urlopen(who).read().decode()
            print(openn)
            mainpage()
        
        elif choose == "7":
            ipaddress = input("Enter the IP address or hostname  :")
            ip = "http://ip-api.com/json/"  + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "8":
            ipaddress = input("Enter the IP address or hostname   :")
            ip = "http://api.hackertarget.com/reverseiplookup/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
               
        elif choose == "9":
            ipaddress = input("Enter the hostname  :")
            subdom = os.getcwd()
            os.system('cd ' +  subdom + '/modules && python2 sub.py -t %s -l fr ' % ipaddress)
            mainpage()
            
        elif choose == "10":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/findshareddns/?q=ns1." + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
        elif choose == "11":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/httpheaders/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "12":
            ipaddress = input("Enter the IP address or hostname :")
            robot = os.getcwd()
            os.system('cd ' +  robot  + '/modules && python2 goofile.py -d %s -f txt' % ipaddress)
            mainpage()
            
        elif choose == "13":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/hostsearch/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "14":
            ipaddress = input("Enter the IP address or hostname :")            
            ip = "http://api.hackertarget.com/zonetransfer/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "15":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "http://api.hackertarget.com/subnetcalc/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
        
        elif choose == "16":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/pagelinks/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
            
        elif choose == "17":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/nping/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()
			
        elif choose == "18":
            ipaddress = input("Enter the IP address or hostname :")
            ip = "https://api.hackertarget.com/reversedns/?q=" + ipaddress
            openn = urlopen(ip).read().decode()
            print(openn)
            mainpage()

        else:
            print("Invalid operation")
            mainpage()
list()






