title=System Requirements
date=2015-05-14
type=post
tags=spring,java
status=published
author=Max Anderson
jira=http://jira.server.com/issue/PROJECT-TWO-42
docker=project-two
~~~~~~

      NB! the content is copied from the [Revizor](https://github.com/w32blaster/revizor/wiki/How-to-prepare-developer-environment) wiki for demonstration purposes.

This article explains how to prepare your environment for the development in Grails and how to run the Revizor on your local machine.

## Requirements
 * Java 7
 * Maven

## Install Groovy and Grails
I recommend to use tool called GVM ([offsite](http://gvmtool.net/)). It allows you to install Groovy language and the Grails framework with only few commands. Please, follow instructions on the official website and install **groovy** and **grails**.

As a result, you should be able to run this commands from your console:

     $ groovy -version
     $ grails

## How to run the project in development mode
Navigate to your project in the console and type the command:

    grails -reloading run-app

After Grails sets up all the necessary dependencies, you will be asked to open `http://localhost:8080/revizor/` URL in your browser.

## How to build the project for production

In order to automate release process, I created a shell script **release.sh** ([source code](https://github.com/w32blaster/revizor/blob/master/release.sh)), but nevertheless I am going to explain the whole process in this chapter.

There are two options how you can deploy/execute the Revizor on your server: as standalone JAR file or as WAR archive.

### 1. Executable Jar file

To build JAR file please run this command:

    grails prod build-standalone revizor.jar

As result, you will get the file **revizor.jar** in the *target* folder, that contains Jetty, database and all other settings and can be executed as simply:

    java -jar revizor.jar

For all other properties, please, refer to the [grails-standalone plugin manual](http://grails-plugins.github.io/grails-standalone/docs/manual/guide/running.html)

### 2. WAR file

To build a WAR file simply run the command:

    grails war

As result you will find **revizor-[version].war** file in the *target* directory. You can deploy this archive to any container you want.

### How to run Revizor in production mode

Please refer to the **Quick start** page for details.


