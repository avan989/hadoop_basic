#!/bin/bash

hadoop jar /usr/local/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /usr/local/share/map_reducer/mapper.py    -mapper /usr/local/share/map_reducer/mapper.py \
-file /usr/local/share/map_reducer/reducer.py   -reducer /usr/local/share/map_reducer/reducer.py \
-input /tmp/2008.csv -output /tmp/2008_output