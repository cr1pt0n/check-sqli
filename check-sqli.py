# -*- coding: utf-8 -*-

import sys
import os
try:
    import requests

except ImportError:
    install = raw_input('request module not installed do you want to install (y/n)? ')
    if( install == 'y' or install == 'yes' ):
        os.system('pip install requests')

    else:
        print '\nBye'
        sys.exit()

# coded by: RNX

try:
    sites = sys.argv[1]
    RED = '\033[1;31m'

except IndexError:
    print 'check_vulnsql: v1.0\n\nUsage: python %s <sites.txt>\nExample: testphp.vulnweb.com/listproducts.php?cat=1' % sys.argv[0]
    sys.exit()

with open(sites) as web_sites:
    sites_vulns = []

    for sts in web_sites.readlines():
        sites_vulns.append(sts.strip('\n'))

print 'Starting test...\n'
for sites in sites_vulns:
    try:
        if( sites.startswith('http://') or sites.startswith('https://') ):
            connect = requests.get(sites + "'", timeout=5)
    
        else:
            connect = requests.get('http://' + sites + "'", timeout=5)

        if( 'You have an error in your SQL syntax;' in connect.content or 'check the manual that corresponds to your MySQL server version for the right syntax to use near' in connect.content ):
            print RED + '[!] Vulnerable: %s' % sites

    except:
        pass


