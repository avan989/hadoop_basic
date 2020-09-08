#!/bin/bash

/etc/bootstrap.sh
jps

$HADOOP_HOME/bin/hadoop dfs -mkdir -p /tmp
$HADOOP_HOME/bin/hadoop dfs -mkdir -p /user/hive/warehouse
$HADOOP_HOME/bin/hadoop dfs -chmod g+w /user/hive/warehouse
$HADOOP_HOME/bin/hadoop dfs -chmod g+w /tmp

schematool -dbType derby -initSchemaTo 2.0.0 -verbose

echo "Finish Setting Up"
while true
do
  :
done
