#!/usr/bin/env python

import sys

# mapper to count number of flight out of each state
for line in sys.stdin:  
    line = line.strip()
    columns = line.split(",")
    
    try:
        int(columns[0])
        key = columns[16]
        value = '1'
        
        results = [key, value]
        print("%s\t%s" % (key, value))
    except:
        continue

        
    