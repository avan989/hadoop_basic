#! /usr/bin/env python

import sys

prev_state = None
current_state = None
counter = 0

for line in sys.stdin:
    line = line.strip()
    state, count = line.split("\t")
    count = int(count)
    
    # first iteration
    if current_state == None:
        prev_state = state 
    
    current_state = state # set current state to state
    
    if current_state == prev_state:
        counter += count # add to counter
    else:
        print(" %s\t%s " % (prev_state, counter)) 
        # reset counter
        counter = 1
        prev_state = current_state
        

# last row will not have an state change so we need to output the data
print(" %s\t%s " % (prev_state, counter)) 
        