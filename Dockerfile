From ubuntu:20.04

# Install dependency
RUN apt-get update \
    && apt-get install -y default-jdk
	
# Create Environment
ENV HOME=/usr
ENV HADOOP_HOME=$HOME/hadoop

# Create directory
RUN mkdir -p $HADOOP_HOME

# Create User
RUN useradd -d $HADOOP_HOME hadoop
RUN su - hadoop

# Generate SSH password
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys


