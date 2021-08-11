#!/usr/bin/python
import os
import sys
import requests
import argparse
#All the arguments
arguments = str(['help', 'dns', 'sub', 'findshareddns', 'geoip', 'reverseip', 'httpheader','pagelinks','whois'])
def clear():
    os.system('clear && clear && clear')
#All Logos
def info():
    print('''
                            oggy - Get domain or IP informations.
                                    Author: zerobl0ck
                            Github: https://github.com/zerobl0ck
        ''')
def dns_logo(): 
    clear()
    print('''
    _______  .__   __.      _______.    __        ______     ______    __  ___  __    __  .______   
    |       \ |  \ |  |     /       |   |  |      /  __  \   /  __  \  |  |/  / |  |  |  | |   _  \  
    |  .--.  ||   \|  |    |   (----`   |  |     |  |  |  | |  |  |  | |  '  /  |  |  |  | |  |_)  | 
    |  |  |  ||  . `  |     \   \       |  |     |  |  |  | |  |  |  | |    <   |  |  |  | |   ___/  
    |  '--'  ||  |\   | .----)   |      |  `----.|  `--'  | |  `--'  | |  .  \  |  `--'  | |  |      
    |_______/ |__| \__| |_______/       |_______| \______/   \______/  |__|\__\  \______/  | _|      
                                                                                                ''')
    info()
def sub_logo(): 
    clear()
    print('''
     _______. __    __  .______    _______   ______   .___  ___.      ___       __  .__   __.      _______.
    /       ||  |  |  | |   _  \  |       \ /  __  \  |   \/   |     /   \     |  | |  \ |  |     /       |
   |   (----`|  |  |  | |  |_)  | |  .--.  |  |  |  | |  \  /  |    /  ^  \    |  | |   \|  |    |   (----`
    \   \    |  |  |  | |   _  <  |  |  |  |  |  |  | |  |\/|  |   /  /_\  \   |  | |  . `  |     \   \    
.----)   |   |  `--'  | |  |_)  | |  '--'  |  `--'  | |  |  |  |  /  _____  \  |  | |  |\   | .----)   |   
|_______/     \______/  |______/  |_______/ \______/  |__|  |__| /__/     \__\ |__| |__| \__| |_______/    
                                                                                                            ''')
    info()
def fsd_logo(): 
    clear()
    print('''
      ______. __    __       ___      .______       _______  _______      _______  .__   __.      _______.
    /       ||  |  |  |     /   \     |   _  \     |   ____||       \    |       \ |  \ |  |     /       |
   |   (----`|  |__|  |    /  ^  \    |  |_)  |    |  |__   |  .--.  |   |  .--.  ||   \|  |    |   (----`
    \   \    |   __   |   /  /_\  \   |      /     |   __|  |  |  |  |   |  |  |  ||  . `  |     \   \    
.----)   |   |  |  |  |  /  _____  \  |  |\  \----.|  |____ |  '--'  |   |  '--'  ||  |\   | .----)   |   
|_______/    |__|  |__| /__/     \__\ | _| `._____||_______||_______/    |_______/ |__| \__| |_______/    
                                                                                                          ''')
    info()
def geoip_logo(): 
    clear()
    print('''
  _______  _______   ______    __  .______   
 /  _____||   ____| /  __  \  |  | |   _  \  
|  |  __  |  |__   |  |  |  | |  | |  |_)  | 
|  | |_ | |   __|  |  |  |  | |  | |   ___/  
|  |__| | |  |____ |  `--'  | |  | |  |      
 \______| |_______| \______/  |__| | _|      
                                             ''')
    info()
def rip_logo(): 
    clear()
    print('''
.______       ___________    ____  _______ .______          _______. _______     __  .______   
|   _  \     |   ____\   \  /   / |   ____||   _  \        /       ||   ____|   |  | |   _  \  
|  |_)  |    |  |__   \   \/   /  |  |__   |  |_)  |      |   (----`|  |__      |  | |  |_)  | 
|      /     |   __|   \      /   |   __|  |      /        \   \    |   __|     |  | |   ___/  
|  |\  \----.|  |____   \    /    |  |____ |  |\  \----.----)   |   |  |____    |  | |  |      
| _| `._____||_______|   \__/     |_______|| _| `._____|_______/    |_______|   |__| | _|      
                                                                                               ''')
    info()
def http_logo(): 
    clear()
    print('''
 __    __  .___________.___________..______       __    __   _______     ___       _______   _______ .______      
|  |  |  | |           |           ||   _  \     |  |  |  | |   ____|   /   \     |       \ |   ____||   _  \     
|  |__|  | `---|  |----`---|  |----`|  |_)  |    |  |__|  | |  |__     /  ^  \    |  .--.  ||  |__   |  |_)  |    
|   __   |     |  |        |  |     |   ___/     |   __   | |   __|   /  /_\  \   |  |  |  ||   __|  |      /     
|  |  |  |     |  |        |  |     |  |         |  |  |  | |  |____ /  _____  \  |  '--'  ||  |____ |  |\  \----.
|__|  |__|     |__|        |__|     | _|         |__|  |__| |_______/__/     \__\ |_______/ |_______|| _| `._____|
                                                                                                                  ''')
    info()
def page_logo(): 
    clear()
    print('''
.______      ___       _______  _______     __       __  .__   __.  __  ___      _______.
|   _  \    /   \     /  _____||   ____|   |  |     |  | |  \ |  | |  |/  /     /       |
|  |_)  |  /  ^  \   |  |  __  |  |__      |  |     |  | |   \|  | |  '  /     |   (----`
|   ___/  /  /_\  \  |  | |_ | |   __|     |  |     |  | |  . `  | |    <       \   \    
|  |     /  _____  \ |  |__| | |  |____    |  `----.|  | |  |\   | |  .  \  .----)   |   
| _|    /__/     \__\ \______| |_______|   |_______||__| |__| \__| |__|\__\ |_______/    
                                                                                         ''')
    info()
def whois_logo(): 
    clear()
    print('''
____    __    ____  __    __    ______    __       _______.
\   \  /  \  /   / |  |  |  |  /  __  \  |  |     /       |
 \   \/    \/   /  |  |__|  | |  |  |  | |  |    |   (----`
  \            /   |   __   | |  |  |  | |  |     \   \    
   \    /\    /    |  |  |  | |  `--'  | |  | .----)   |   
    \__/  \__/     |__|  |__|  \______/  |__| |_______/    
                                                           ''')
    info()
# API URL and key
apiurl = "https://api.hackertarget.com/"
apiurl_2 = "https://api.ip2whois.com/v2?"
#You need to register on https://ip2whois.com and get a API key. Paste your API key below.
apikey = "Enter_Your_API_Key"

def print_help():
    parser = argparse.ArgumentParser()
    parser.add_argument("dns", nargs="?", help="Find DNS records for a domain")
    parser.add_argument("sub", nargs="?", help="Find forward DNS (A) records for a domain (Subdomains).")
    parser.add_argument("findshareddns", nargs="?", help="Find hosts sharing DNS servers.")
    parser.add_argument("geoip", nargs="?", help="Find the location of an IP address using the GeoIP lookup location tool.")
    parser.add_argument("reverseip", nargs="?", help="Discover web hosts sharing an IP address with a reverse IP lookup.")
    parser.add_argument("httpheader", nargs="?", help="View HTTP Headers of a web site.")
    parser.add_argument("pagelinks", nargs="?", help="Dump all the links from a web page.")
    parser.add_argument("whois", nargs="?", help="Determine the registered owner of a domain or IP address block with the whois tool.")
    parser.parse_args()
def whois(data):
    for key,value in data.items():
        print (key, ":", value)
        if type(value) == type(dict()):
            whois(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    whois(val)

def scan(list_):
    def print_text():
        print(response.text)
        output = open("output.txt", "w")
        print(response.text, file=output)
        print("\nOutput saved in output.txt file")
    for i in list_:
        try:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                print_help()
                quit()
            elif sys.argv[1] == "dns":
                dns_logo()
                query = input("Enter domain name: ")
                response = requests.get(apiurl+"/dnslookup/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "sub":
                sub_logo()
                query = input("Enter domain name: ")
                response = requests.get(apiurl+"/hostsearch/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "findshareddns":
                fsd_logo()
                query = input("Enter one nameserver: ")
                response = requests.get(apiurl+"/findshareddns/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "geoip":
                geoip_logo()
                query = input("Enter IP Address: ")
                response = requests.get(apiurl+"/geoip/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "reverseip":
                rip_logo()
                query = input("Enter IP Address: ")
                response = requests.get(apiurl+"/reverseiplookup/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "httpheader":
                http_logo()
                query = input("Enter domain name with https://: ")
                response = requests.get(apiurl+"/httpheaders/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "pagelinks":
                page_logo()
                query = input("Enter domain name: ")
                response = requests.get(apiurl+"/pagelinks/?q="+query)
                print_text()
                quit()
            elif sys.argv[1] == "whois":
                whois_logo()
                query = input("Enter domain name: ")
                response = requests.get(f'{apiurl_2}key={apikey}&domain={query}')
                response.status_code
                data = response.json()
                whois(data)
                quit()
        except KeyboardInterrupt:
            print ('')
    print("Use correct argument")
    quit()

while len(sys.argv) == 2:
    scan(arguments)
    pass
print("Enter vaild argument")
