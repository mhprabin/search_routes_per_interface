#This code is from cisco PRNE course
from pprint import pprint
import re

#create regular expression to match ethernet interface names

eth_pattern = re.compile('Ethernet[0-9]')
routes = {}

#read all lines of IP routing information

file = open('ip-routes','r')
for line in file:
        match = eth_pattern.search(line)
        #check to see if we match ethernet string
        if match:
                intf = match.group(0) #get the interface from match
                print intf
                routes[intf] = routes[intf]+1 if intf in routes else 1
        else:
                continue

print ''
print "number of routes per interface"
print '------------------------------'
pprint(routes)
