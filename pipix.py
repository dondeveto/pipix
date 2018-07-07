from urllib3 import *
from platform import system
from urllib.request import urlopen
import sys
import os

links = ["https://api.shodan.io/labs/honeyscore/{}?key=oxchYb8VrHJoYvLVRtid2reJa0TRStW8", #1
         "http://api.hackertarget.com/dnslookup/?q={}",                                   #2
         "http://api.hackertarget.com/nmap/?q={}",                                        #3
         "https://api.hackertarget.com/mtr/?q={}",                                        #5
         "http://api.hackertarget.com/whois/?q={}",                                       #6
         "http://ip-api.com/json/{}",                                                     #7
         "http://api.hackertarget.com/reverseiplookup/?q={}",                             #8
         "https://api.hackertarget.com/findshareddns/?q=ns1.{}",                          #10
         "http://api.hackertarget.com/httpheaders/?q={}",                                 #11
         "http://api.hackertarget.com/hostsearch/?q={}",                                  #13
         "http://api.hackertarget.com/zonetransfer/?q={}",                                #14
         "http://api.hackertarget.com/subnetcalc/?q={}",                                  #15
         "https://api.hackertarget.com/pagelinks/?q={}",                                  #16
         "https://api.hackertarget.com/nping/?q={}",                                      #17
         "https://api.hackertarget.com/reversedns/?q={}",                                 #18
         ]



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


#########################################################################################
def work(num):
    global links
    if num == 19:
        print("\n","\033[1;32m See you later (づ｡◕‿‿◕｡)づ✿ ","\n")
        exit
    else:
        choice = num -1
        op=links[choice]
        ipaddress = input("Enter the IP address  :")
        openn = urlopen(op.format(ipaddress)).read().decode()
        if num ==1:
            print("\n","Honey Score :",openn)
            input("press Enter to continue.....")
            mainpage()
        else:
            print(openn)
            input("press Enter to continue.....")
            mainpage()
########################################################################################
def list():
    choice = [4,9,12]
    choice2 = [1,2,3,5,6,7,8,10,11,13,14,15,16,17,18,19]
    while True:
        num = int(input("\033[1;36m Select Number  :"))
        if num in choice:            
                        
            if num == "4":
                ipaddress = input("Enter the hostname  :")
                harvest = os.getcwd()
                os.system('cd ' +  harvest  + '/modules && python2 theHarvester.py -d %s -b all' % ipaddress)
                input("press Enter to continue.....")
                mainpage()
                

            elif num == "9":
                ipaddress = input("Enter the hostname  :")
                subdom = os.getcwd()
                os.system('cd ' +  subdom + '/modules && python2 sub.py -t %s -l fr ' % ipaddress)
                input("press Enter to continue.....")
                mainpage()
                

                
            elif num == "12":
                ipaddress = input("Enter the IP address or hostname :")
                robot = os.getcwd()
                os.system('cd ' +  robot  + '/modules && python2 goofile.py -d %s -f txt' % ipaddress)
                input("press Enter to continue.....")
                mainpage()
                


            else:
                print("Invalid operation")
                input("press Enter to continue.....")
                mainpage()
        elif num in choice2:
            work(num)

        else:
            print("Invalid operation")
            input("press Enter to continue.....")
            mainpage()
list()
