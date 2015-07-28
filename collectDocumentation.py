#!/usr/bin/env python
import os
import sys, getopt
import fnmatch
import shutil
from shutil import copyfile
from subprocess import call
#GitPython:
from git import Repo
from git import InvalidGitRepositoryError
from subprocess import call


# path where the jBake site is located
bakePath = '/home/ilja/workspace/docs'
bakeContentPath = bakePath + '/content/'
bakeReadyWebsite = bakePath + '/output/'

# directory where is cloned repositories are located
clonedReposPath = '/home/ilja/testCloned/'

# directory where bare repositories are located
bareReposPath = '/home/ilja/testBareRepos/'

# directory, where HTML version of your documentation is hosted
documentationFinalPath = '/home/ilja/Public/documentation'

readmeFileName = 'PI_README.md'

# if JBake is in your env, then provide only 'jbake', otherwise full path name
pathToJBakeExec='jbake'

suffixLength = -len(".git")
prefixLength = len("title=")

def main(argv):
      '''
      Walk recursively within our projects and collects README files.
      Each file should be renamed and copied to jBake folder.
      '''

      # pull/clone all available repositories
      _updateRepositories()

      # remove all old files
      shutil.rmtree(bakeContentPath, True)
      os.mkdir(bakeContentPath)

      # recursively collect READMEs 
      for root, dirnames, filenames in os.walk(clonedReposPath):
            for filename in fnmatch.filter(filenames, readmeFileName):
                  fullPath = os.path.join(root, filename)
                  _copyFile(fullPath)

      # ask JBake to re-build the website
      call([pathToJBakeExec, bakePath, bakeReadyWebsite, "--bake"])

      # copy generated files to the destination folder
      shutil.rmtree(documentationFinalPath, True)
      shutil.copytree(bakeReadyWebsite, documentationFinalPath)


def _updateRepositories():
      '''
      Updates all the repositories. In case if there is some new bare repository,
      it will be cloned.
      '''

      bareDirnames=[d for d in os.listdir(bareReposPath) if os.path.isdir(os.path.join(bareReposPath, d)) ]
      clonesDirnames=[d for d in os.listdir(clonedReposPath) if os.path.isdir(os.path.join(clonedReposPath, d)) ]

      for dirname in bareDirnames:
            if _isCloneExist(clonesDirnames, dirname):
                  # this repo is has been cloned, update it
                  _update(dirname)
            else:
                  # new repo has been appeared, clone it
                  _cloneRepository(dirname)


def _update(dirname):
      '''
      Executes 'git pull origin master' for the specified directory
      '''
      cloneDirName = dirname[:suffixLength] if (".git" in dirname) else dirname
      repo = Repo(os.path.join(clonedReposPath, cloneDirName))
      o = repo.remotes.origin
      o.pull()
      print "[UPDATE] '%s' is updated " % cloneDirName


def _cloneRepository(dirname):
      '''
      Clones given repository.
      '''

      repoPath = os.path.join(bareReposPath, dirname)
      try:
            repo = Repo(repoPath)
            if repo.bare:
                  repo.clone(os.path.join(clonedReposPath, dirname[:suffixLength]))
            else:
                  repo.clone(os.path.join(clonedReposPath, dirname))
            
            print "[CLONE] '%s' was cloned" % repoPath

      except InvalidGitRepositoryError:
            print "[SKIP] the '%s' is not repo" % repoPath


def _isCloneExist(clonedRepos, currentBareRepo):
      '''
      Checks that the given bare repository has clone
      '''
      return (currentBareRepo in clonedRepos) or (currentBareRepo[:suffixLength] in clonedRepos)


def _copyFile(fullPath):
      '''
      Read the first line of a file and extract the title, that
      will be the name of a new file. Then it copies the file
      to a new destination.

      Expected, that the very first line will be:
         title=Some Human Readable title

      '''

      f=open(fullPath, 'r')
      
      # read the first line, containing "title=" line
      line=f.next().strip()
      f.close()

      # replace spaces and prefix "title="
      newFileName=line[prefixLength:].replace(" ", "_")
      
      # copy file
      newFullPath = _getNewPathForFile(bakeContentPath, clonedReposPath, fullPath, newFileName)
      
      # if this file in the subdirectory, than create it first
      subFolder = os.path.split(newFullPath)[0]
      if not os.path.isdir(subFolder):
            os.makedirs(subFolder)

      copyfile(fullPath, newFullPath)

      print "[COPY] the file '%s' is copied to '%s' " % (fullPath, newFullPath)


def _getNewPathForFile(bakeContentPath, cloneDirName, fullPath, newFileName):
      
      # get path relative Git storage
      rel = os.path.relpath(fullPath, cloneDirName)

      # get path relative the current repo root
      relFolder = rel.split(os.sep)
      relRepoRootPath = os.path.split(os.path.relpath(rel, relFolder[0]))

      return os.path.join(bakeContentPath, relRepoRootPath[0], newFileName + ".md")



if __name__ == "__main__":
    main(sys.argv[1:])
