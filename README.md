# oggy

oggy provides informations about IP Addresses, Networks, Web Pages and DNS records.

### DNS Lookup
Gather standard DNS records of the domain.

### Find DNS (A) record or subdomains
Collect more information about the target. Find subdomains and DNS (A) records.

### Find Shared DNS
Search all the shared DNS hosts of the target. Discover additional domains and host names from a shared DNS server.

### GeoIP
Search location of the IP address.

### Reverse IP Lookup

Collect all the (A) records associated with an IP address. It will locate a dns PTR record for that IP address. 

### HTTP Header

Quick review of the HTTP Headers from a web server. Get target's HTTP Header easily.

### Page Links

Find all the pages of a website. It will extract links from the page. 

### Whois

This tool will provide you whois records of the website.

```
usage: python3 oggy.py [-h] [dns] [sub] [findshareddns] [geoip] [reverseip] [httpheader] [pagelinks] 
               [whois]

positional arguments:
  dns 		 Find DNS records for a domain. 
  sub            Find forward DNS (A) records for a domain (Subdomains).
  findshareddns  Find hosts sharing DNS servers.
  geoip          Find the location of an IP address using the GeoIP lookup location tool.
  reverseip      Discover web hosts sharing an IP address with a reverse IP lookup.
  httpheader     View HTTP Headers of a web site.
  pagelinks      Dump all the links from a web page.
  whois          Determine the registered owner of a domain or IP address block with the whois tool.

optional arguments:
  -h, --help     show this help message and exit
```
### Sources to be implemented
- https://api.hackertarget.com/
- https://api.ip2whois.com/
