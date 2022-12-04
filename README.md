# Data Engineering

## Spark Installation
- Download a pre-packaged of Hadoop from https://spark.apache.org/downloads.html.
- Run `tar -zvxf <file_name>` on the downloaded package.
- Install JRE and JVM.
  - Run `sudo apt update`
  - Run `sudo apt install default-jre`
  - Run `java -version` to verify the installation.
  - Run `sudo apt install default-jdk`
  - Run `javac -version` to verify the installtion.
- (Optional) manage multiple versions of Java
  - Run `sudo update-alternatives --config java`
  - Run `sudo update-alternatives --config javac`
- Set the `JAVA_HOME` environment variable.
  - Run `sudo update-alternatives --config java` to determine where Java is installed.
  - Run `sudo vim /etc/environment` or `sudo vim ~/.bashrc`
  - Add `JAVA_HOME="<path_to_java>"`
  - Run `source /etc/environment` or `source ~/.bashrc`
  - Run `echo $JAVA_HOME` to verify that the environment variable was set.
