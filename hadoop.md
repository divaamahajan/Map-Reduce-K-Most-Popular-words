`sudo apt-get update` to update the package lists and then run `sudo apt-get install`

`sudo apt-get install --fix-missing` to attempt to fix any missing dependencies.

## 1. Install Java:
* **Download OpenJDK 8**: Run the command: `sudo apt install openjdk-8-jdk`
* **Verify the installation**: Run the command: `java -version`
* **Add the following lines to .bashrc**:

Go to `nano ~/.bashrc`
add below lines to the end of file
```yaml
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64
export PATH=$PATH:/usr/lib/jvm/java-8-openjdk-arm64/bin
export HADOOP_HOME=~/hadoop-3.3.5/
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar
export HADOOP_LOG_DIR=$HADOOP_HOME/logs
export PDSH_RCMD_TYPE=ssh
```

To update go to `source ~/.bashrc`
## 2. Create an SSH connection to localhost:
### Install SSH: 
Run the command: `sudo apt-get install ssh`
### Generate SSH keys:
>- Use the command: `ls -al ~/.ssh` to check for existing SSH keys.
>- If present, add the public key to the authorized_keys file. If the file is not present, create it.
>- You can generate new host keys by running the following command: `sudo dpkg-reconfigure openssh-server`
>-Then, try starting the SSH server again with: `sudo service ssh start`
>- If it starts successfully, you should be able to connect to localhost with: `ssh localhost` and then type `yes` to create a fingerprint.
  You should now be connected to the localhost.
  Use `control + d` to terminate the session.
### If there are no existing SSH keys, 
run the following commands:
>- `ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa`
>- `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`
>- `chmod 0600 ~/.ssh/id_rsa.pub`
>- Check the key's functionality by connecting to the local host using ssh localhost, then close the connection with `control + d`.
### Note:
If you cannot connect to the local host, uninstall and install it.
>- Uninstall: `sudo apt-get remove openssh-client openssh-server`
>- Install: `sudo apt-get install openssh-client openssh-server`
## 3. Download Hadoop:
### 1. Download Hadoop:
`wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz -P ~/Downloads/`
### 2.  Extract Hadoop in the root directory
`tar -zxvf ~/Downloads/hadoop-3.3.5.tar.gz`

### 3. Change the JAVA_HOME path:
>* Open the terminal on your system.
>* Type `echo $JAVA_HOME` and hit Enter. This will display the current value of `JAVA_HOME` environment variable.
> If the output matches with `/usr/lib/jvm/java-8-openjdk-arm64`, then it is your `JAVA_HOME` path. 
Update `JAVA_HOME` path in hadoop. 

`sudo nano hadoop-3.3.5/etc/hadoop/hadoop-env.sh`

#### Add at the end of file
`export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64`

Find the line `export JAVA_HOME=<path>` and replace `<path>` with `/usr/lib/jvm/java-8-openjdk-arm64`.

Save and exit the file by pressing `CTRL+X`, then `Y`, then `Enter`.
### 4. Add configuration to core-site.xml:

`sudo nano hadoop-3.3.5/etc/hadoop/core-site.xml`

Add the following configuration between the `<configuration>` tags:
  ```yaml
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
</property>
<property>
    <name>hadoop.proxyuser.dataflair.groups</name>
    <value>*</value>
</property>
<property>
    <name>hadoop.proxyuser.dataflair.hosts</name>
    <value>*</value>
</property>
<property>
    <name>hadoop.proxyuser.server.hosts</name>
    <value>*</value>
</property>
<property>
    <name>hadoop.proxyuser.server.groups</name>
    <value>*</value>
</property>

  ```

Save and exit the file by pressing `CTRL+X`, then `Y`, then `Enter`.

### 5. Add configuration to hdfs-site.xml:
`sudo nano hadoop-3.3.5/etc/hadoop/hdfs-site.xml`

Add the following configuration between the `<configuration>` tags:
  ``` yaml
<property>
    <name>dfs.replication</name>
    <value>1</value>
</property>

  ```
Save and exit the file by pressing `CTRL+X`, then `Y`, then `Enter`.
### 6. Add configuration to mapred-site.xml:
`sudo nano hadoop-3.3.5/etc/hadoop/mapred-site.xml`

Add the following configuration between the `<configuration>` tags:
  ``` yaml
<property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
</property>
<property>
    <name>mapreduce.application.classpath</name>
    <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
</property>

  ```
  Note: if error : `Unable to find 'resource-types.xml'`. change the properties to below:
```yaml
<property>
<name>yarn.app.mapreduce.am.env</name>
<value>HADOOP_MAPRED_HOME=/opt/hadoop</value>
</property>
<property>
<name>mapreduce.map.env</name>
<value>HADOOP_MAPRED_HOME=/opt/hadoop</value>
</property>
<property>
<name>mapreduce.reduce.env</name>
<value>HADOOP_MAPRED_HOME=/opt/hadoop</value>
</property>
```
Save and exit the file by pressing `CTRL+X`, then `Y`, then `Enter`.

### 7. Add configuration to yarn-site.xml:
`sudo nano hadoop-3.3.5/etc/hadoop/yarn-site.xml`

Add the following configuration between the `<configuration>` tags:
  ``` yaml
<property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
</property>
<property>
    <name>yarn.nodemanager.env-whitelist</name>
    <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
</property>

  ```
Save and exit the file by pressing `CTRL+X`, then `Y`, then `Enter`.

### 8. Format the namenode:
`sudo hadoop-3.3.5/bin/hdfs namenode -format`

### 9. Set PDSH_RCMD_TYPE environment variable:
`export PDSH_RCMD_TYPE=ssh`

### 10. Start all the daemons:
Run one of the below commands
* `sudo hadoop-3.3.5/sbin/start-all`
* `hadoop-3.3.5/sbin/start-all.sh`
* `chmod +x hadoop-3.3.5/sbin/start-all.sh`

#### Issue is with the permissions on the logs directory
Hadoop is unable to write to the directory, so it's failing to start. You can try to fix the permissions by running the following command:
> `sudo chown -R <username>:<username> hadoop-3.3.5/logs`
This will change the ownership of the logs directory to the user <username>. Then, try starting Hadoop again with the command:
> `hadoop-3.3.5/sbin/start-all.sh`
  
## Execute
  ```yaml
  hadoop-3.3.5/bin/hadoop jar hadoop-3.3.5/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-files "/<local_directory>/Map-Reduce-K-Most-Popular-words/exp1_stopwords/mapper_stopwords.py","/<local_directory>/Map-Reduce-K-Most-Popular-words/exp1_stopwords/reducer.py","/<local_directory>/Map-Reduce-K-Most-Popular-words/stop_words.txt" \
-mapper "/<local_directory>/Map-Reduce-K-Most-Popular-words/exp1_stopwords/mapper_stopwords.py" \
-reducer "/<local_directory>/Map-Reduce-K-Most-Popular-words/exp1_stopwords/reducer.py" \
-input /user/divyamahajan/MapReduce/input/data_16GB.txt \
-output /user/divyamahajan/MapReduce/output/exp0
  ```
## Note
* If working on python, make sure to add below header
  `#!/usr/bin/env python3`
* If working on Ubuntu app via Windows
> * `sudo apt-get install dos2unix`
> * `dos2unix mapper.py`
> * `dos2unix reducer.py`
> * `dos2unix topk.py`
* if trying too run same command, remove output file dir: `hadoop fs -rm -r /user/divyamahajan/MapReduce/output/exp0`
