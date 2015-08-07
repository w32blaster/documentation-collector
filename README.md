# Documentation Collector

**Docementation Collector** is a simple script that collects README files from multiple Git projects and builds single HTML based documentation using [JBake](http://www.jbake.org) generator.

## Why?

There are lot of many different tools that can generate a documentation for your code. But all of them have one small disadvantage: they work only for one single project. Let's image that your company has dozens of small projects (for example, microservices). To organize working process you have to create internal Wiki page and fill manulally all the valuable information about your code base. But this is exhausting work. The **Docementation Collector** script was written to automate this process.

## How does it work?

Each your project has its own README.md file (like in GitHub). **Docementation Collector** is simple script that scans recursively all your workspace and collects found README.md files and runs JBake to build a HTML page for you.

## Demo
The result could be look like this

 * [live demo](http://w32blaster.github.io/documentation-collector/)
 
but abviousely you can modify the layout and styles as you wish.

![Documentation generated using JBake and documentation collector script](http://w32blaster.github.io/documentation-collector/smart-commits.png)

Please, find the source code of this demo page [here](https://github.com/w32blaster/documentation-collector/tree/master/demo)

The script could be executed by CRON or Git hook.

## Limitation and requirements

* **Docementation Collector** is designed to be executed on the same server where bare Git repositories are located
* the script runs [JBake](http://www.jbake.org) generator, that uses Java installed
* expected that the very first line of each README file is _"title=Some Title"_ (see the _demo/content_ filder, [for example](https://raw.githubusercontent.com/w32blaster/documentation-collector/master/demo/content/Project_Three.md))
* requires *GitPython*. You can install it using command:

     ```
     pip install gitpython
     ```
     
## Installation steps

 1. download script **collectDocumentation.py** to the server where your bare Git repositories are hosted
 2. download JBake. No need to install it using **GVM**, you can just only [download](http://jbake.org/download.html) and unpack it.
 3. install GitPython
 4. create a directory, where you will create your documentation. Navigate to this folder and run:
 
 ```
 $ /path/to/jbake init
 ```
 
 That command asks JBake to generate a simple blog. If you then run it without arguments again:
 
 ```
 $ /path/to/jbake
 ```
 
 ...it will generate ready HTML website for you in the **output** directory.
 5. now you are ready to "bake" your first documentation. Open script **collectDocumentation.py** and modify the following settings in the top of the file:
  * **bakePath** - the path to the JBake directory, that you created in Step 3.
  * **clonedReposPath** - directory where script will clone all your repos. On each other invocation it will update instead cloning.
  * **bareReposPath** - path where your **bare** Git repositories are located.
  * **documentationFinalPath** - public folder where to put (deploy) ready html website. For example, `/var/www`
  * **readmeFileName** - specify name of README files to be collected in case if you use different name or company prefixes, like *PRFX_README.md*. Remember, you can use either Markdown or Asciidoc for your syntax!
  * **pathToJBakeExec** - full path to executable JBake. If you added it to your PATH, then specify simply *jbake*
 5. assume that you have already committed couple of README files. Then you can execute the script:
 
  ```
  python collectDocumentation.py
  ```
  
As result you will get ready HTML side generated from your documentation files. 


