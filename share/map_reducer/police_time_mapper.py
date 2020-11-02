#!/usr/bin/env python

import sys
import time

key_map = ["0 - 1", "1 - 2", "2 - 3","3 - 4", "4 - 5", "5 - 6", "6 - 7", "7 - 8", \
           "8 - 9", "9 - 10", "10 - 11", "11 - 12", "12 - 13", "13 - 14", "14 - 15", \
           "15 - 16", "16 - 17", "17 - 18", "18 - 19", "19 - 20", "20 - 21", "21 - 22", \
           "22 - 23", "23 - 24"]
# mapper to count number of flight out of each state
for line in sys.stdin:  
    line = line.strip()
    columns = line.split(",")
    
    try:
        int(columns[0])
        time_police = time.strptime(columns[3], "%H:%M")
        hours = int(time_police.tm_hour)
        
        key = key_map[hours]
        value = '1'
        
        results = [key, value]
        print("%s\t%s" % (key, value))
    except:
        continue

        
    