#!/usr/bin/env python
import os.path
import sys, getopt
import fnmatch
import shutil
from shutil import copyfile
from subprocess import call
#GitPython:
from git import Repo
from git import InvalidGitRepositoryError



# path where the jBake site is located
bakePath = '/home/ilja/workspace/docs'
bakeContentPath = bakePath + '/content/'

# directory where is cloned repositories are located
clonedReposPath = '/home/ilja/testCloned/'

# directory where bare repositories are located
bareReposPath = '/home/ilja/testBareRepos'

readmeFileName = 'PI_README.md'

def main(argv):
      '''
      Walk recursively within our projects and collects README files.
      Each file should be renamed and copied to jBake folder.
      '''

      isCreate = _extractCLArguments(argv)

      if isCreate:
            _cloneRepositories()

      else:
            # pull the latest changes to each repository
            _updateRepositories()

            # remove all old files
            shutil.rmtree(bakeContentPath)
            os.mkdir(bakeContentPath)

            # recursively collect READMEs 
            for root, dirnames, filenames in os.walk(clonedReposPath):
                  for filename in fnmatch.filter(filenames, readmeFileName):
                        fullPath = os.path.join(root, filename)
                        _copyFile(fullPath)



def _cloneRepositories():
      '''
      In order to get access to the source code we need to clone bare repos first.
      This command is designed to be executed only once, then it will be only updated.
      '''

      suffixLength = -len(".git")
      # get the list of all the top-level directories
      dirnames=[d for d in os.listdir(bareReposPath) if os.path.isdir(os.path.join(bareReposPath, d)) ]

      for dirname in dirnames:
            bareRepoPath = os.path.join(bareReposPath, dirname)
            try:
                  repo = Repo(bareRepoPath)
                  if repo.bare:
                        repo.clone(os.path.join(clonedReposPath, dirname[:suffixLength]))
                        print "the %s repository was cloned" % bareRepoPath

            except InvalidGitRepositoryError:
                  print "the %s is not repo" % bareRepoPath

def _updateRepositories():
      '''
      Get the latest changes for each repository
      '''

      dirnames=[d for d in os.listdir(clonedReposPath) if os.path.isdir(os.path.join(clonedReposPath, d)) ]
      for dirname in dirnames:
            repo = Repo(os.path.join(clonedReposPath, dirname))
            o = repo.remotes.origin
            o.pull()
            print "repository %s is updated " % dirname


def _copyFile(fullPath):
      '''
      Read the first line of a file and extract the title, that
      will be the name of a new file. Then it copies the file
      to a new destination
      '''
      f=open(fullPath, 'r')
      
      # read the first line, containing "title=" line
      line=f.next().strip()
      f.close()

      # replace spaces and prefix "title="
      newFileName=line[6:].replace(" ", "_")
      
      # copy file
      newFullPath = bakeContentPath + newFileName + ".md"
      copyfile(fullPath, newFullPath)
      print "the file %s is copied to %s " % (fullPath, newFullPath)


def _extractCLArguments(argv):
      '''
      Extracts command line arguments
      '''

      isCreate = False
      try:
            opts, args = getopt.getopt(argv,"c",[])
      except getopt.GetoptError:
            print 'process.py -s <smallFileToBeModified> -p <producersFile>'
            sys.exit(2)

      for opt, arg in opts:
            if opt == '-c':
                  isCreate = True

      return isCreate    



if __name__ == "__main__":
    main(sys.argv[1:])
