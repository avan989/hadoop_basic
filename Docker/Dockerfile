From sequenceiq/hadoop-docker:2.7.1

RUN yum -y install java-1.8.0-openjdk git

COPY ./startup.sh /usr
RUN chmod 0777 /usr/startup.sh

# download hive
RUN curl -s http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./apache-hive-2.1.0-bin hive

# Install Scala
RUN curl -s http://downloads.typesafe.com/scala/2.11.6/scala-2.11.6.tgz | tar -xz -C /opt/
RUN mv /opt/scala-2.11.6 /opt/scala

# configure Scala 
RUN alternatives --install /usr/bin/scala scala /opt/scala/bin/scala 2 
RUN alternatives --install /usr/bin/scalac scalac /opt/scala/bin/scalac 2 
RUN alternatives --install /usr/bin/scaladoc scaladoc /opt/scala/bin/scaladoc 2 
RUN alternatives --install /usr/bin/scalap scalap /opt/scala/bin/scalap 2

# Installing Spark
RUN curl -s http://archive.apache.org/dist/spark/spark-2.0.0/spark-2.0.0-bin-hadoop2.7.tgz  | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./spark-2.0.0-bin-hadoop2.7 spark 


# create hive env
ENV HADOOP_HOME=/usr/local/hadoop
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

ENV HIVE_HOME=/usr/local/hive
ENV PATH=$HIVE_HOME/bin:$PATH
ENV CLASSPATH=$CLASSPATH:$HADOOP_HOME/lib/*:.
ENV CLASSPATH=$CLASSPATH:$HIVE_HOME/lib/*:.

ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# configure hive
RUN cp $HIVE_HOME/conf/hive-env.sh.template $HIVE_HOME/conf/hive-env.sh
RUN cp $HIVE_HOME/conf/hive-default.xml.template $HIVE_HOME/conf/hive-site.xml
RUN echo "export HADOOP_HOME=$HADOOP_HOME" >> $HIVE_HOME/conf/hive-env.sh

RUN sed -i '/<name>hive.exec.scratchdir<\/name>/!b;n;c<value>\/tmp\/hive-${user.name}<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.exec.local.scratchdir<\/name>/!b;n;c<value>\/tmp\/${user.name}<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.downloaded.resources.dir<\/name>/!b;n;c<value>\/tmp\/${user.name}_resources<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.scratch.dir.permission<\/name>/!b;n;c<value>733<\/value>' $HIVE_HOME/conf/hive-site.xml

# make share folder
RUN mkdir -p /usr/local/share

ENTRYPOINT ["/usr/startup.sh"]






