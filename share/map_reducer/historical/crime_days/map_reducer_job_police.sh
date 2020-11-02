#!/bin/bash

hadoop jar /usr/local/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-file /usr/local/share/map_reducer/police_mapper.py    -mapper /usr/local/share/map_reducer/police_mapper.py \
-file /usr/local/share/map_reducer/police_reducer.py   -reducer /usr/local/share/map_reducer/police_reducer.py \
-input /tmp/police_reports.csv -output /tmp/police_reports_output