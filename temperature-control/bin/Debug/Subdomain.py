# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# code by CSeroad

import sys
import urllib.request
import urllib.parse
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def crt_domain(domains):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    with urllib.request.urlopen('https://crt.sh/?q=' + domains) as f:
        code = f.read().decode('utf-8')
        for cert, domain in re.findall('<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(domains) + ')</td>(?:\s|\S)*?</tr>', code, re.IGNORECASE):
            domain = domain.split('@')[-1]
            print(domain)
            with open('crt_result.txt', 'a+') as f:
                f.write(str(domain)+'\n')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        domains=sys.argv[1]
        crt_domain(domains[11:])
    else:
        print('User: python3 crt_domain.py domain')
