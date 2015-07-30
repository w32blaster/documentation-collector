# Documentation Collector

**Docementation Collector** is a simple script that collects README files from multiple Git projects and builds single HTML based documentation using [JBake](http://www.jbake.org) generator.

## Why?

There are lot of many different tools that can generate a documentation for your code. But all of them have one small disadventage: they work only for one single project. Let's image that your company has dozens of small projects (for example, microservices). To organize work you have create internal Wiki page and fill manulally all the valueble information about your code base. This script was written to automate this process.

## How does it work?

Each your project has its own README.md file (like in GitHub). **Docementation Collector** is simple script that scans recursively all your workspace and copies found README.md files to one place and runs JBake to build a HTML page for you.

The result could be look like this:

-----IMAGE-----

The script could be executed by CRON or Git hook.

## Limitation and requirements

* **Docementation Collector** is designed to be executed on the same server where bare Git repositories are located
* the script runs [JBake](http://www.jbake.org) generator, that uses Java installed
* requires *GitPython*. You can install it using command:

     ```
     pip install gitpython
     ```
     
## Installation steps

 1. download script **collectDocumentation.py** to the server where your bare Git repositories are hosted
 2. download JBake. No need to install it using **GVM**, you can just only [download](http://jbake.org/download.html) and unpack it.
 3. then create directory, where you will create your documentation. Navigate to this folder and run:
 
 ```
 $ /path/to/jbake init
 ```
 
 That will generate simple blog. If you run jbake without arguments:
 
 ```
 $ /path/to/jbake
 ```
 
 ...it will generate ready HTML website for you in the **output** directory.
 4. now you are ready to bake your first documentation. Open script **collectDocumentation.py** and modify the following settings in the top of the file:
  * **bakePath** - the path to the JBake website, that you created in Step 3.
  * **clonedReposPath** - directory where script will clone all your repos. On each other invocation it will update instead cloning.
  * **bareReposPath** - path where your **bare** Git repositories are located.
  * **documentationFinalPath** - public folder where to put (deploy) ready html website. For example, `/var/www`
  * **readmeFileName** - specify name of README files to be collected in case if you use different name or company prefixes, like *PRFX_README.md*.
  * **pathToJBakeExec** - full path to executable JBake. If you added it to your PATH, then specify simply *jbake*
 5. assume that you have already committed couple of README.md files. Then you can execute the script:
 
  ```
  python collectDocumentation.py
  ```
  
As result you will get ready HTML side generated from your documentation files. 


