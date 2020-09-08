From sequenceiq/hadoop-docker:2.7.1

RUN yum -y install java-1.8.0-openjdk

COPY ./startup.sh /usr
RUN chmod 0777 /usr/startup.sh

# download hive
RUN curl -s http://archive.apache.org/dist/hive/hive-2.1.0/apache-hive-2.1.0-bin.tar.gz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s ./apache-hive-2.1.0-bin hive

# create hive env
ENV HADOOP_HOME=/usr/local/hadoop
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

ENV HIVE_HOME=/usr/local/hive
ENV PATH=$HIVE_HOME/bin:$PATH
ENV CLASSPATH=$CLASSPATH:$HADOOP_HOME/lib/*:.
ENV CLASSPATH=$CLASSPATH:$HIVE_HOME/lib/*:.

# configure hive
RUN cp $HIVE_HOME/conf/hive-env.sh.template $HIVE_HOME/conf/hive-env.sh
RUN cp $HIVE_HOME/conf/hive-default.xml.template $HIVE_HOME/conf/hive-site.xml
RUN echo "export HADOOP_HOME=$HADOOP_HOME" >> $HIVE_HOME/conf/hive-env.sh

RUN sed -i '/<name>hive.exec.scratchdir<\/name>/!b;n;c<value>\/tmp\/hive-${user.name}<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.exec.local.scratchdir<\/name>/!b;n;c<value>\/tmp\/${user.name}<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.downloaded.resources.dir<\/name>/!b;n;c<value>\/tmp\/${user.name}_resources<\/value>' $HIVE_HOME/conf/hive-site.xml
RUN sed -i '/<name>hive.scratch.dir.permission<\/name>/!b;n;c<value>733<\/value>' $HIVE_HOME/conf/hive-site.xml

ENTRYPOINT ["/usr/startup.sh"]






