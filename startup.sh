#!/bin/bash

/etc/bootstrap.sh
jps

$HADOOP_HOME/bin/hadoop dfs -mkdir -p /tmp
$HADOOP_HOME/bin/hadoop dfs -mkdir -p /user/hive/warehouse
$HADOOP_HOME/bin/hadoop dfs -chmod g+w /user/hive/warehouse
$HADOOP_HOME/bin/hadoop dfs -chmod g+w /tmp
schematool -dbType derby -initSchemaTo 2.0.0 -verbose

$SPARK_HOME/bin/spark-class org.apache.spark.deploy.master.Master --ip `hostname` --port 7077 --webui-port 8080

echo "Finish Setting Up"
while true
do
  :
done
