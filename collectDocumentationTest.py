import unittest
from collectDocumentation import _isCloneExist
from collectDocumentation import _getNewPathForFile
from collectDocumentation import readmeFileName

class ProcessTests(unittest.TestCase):

      def test_detect_missing_repositories(self):

            # given
            clonedRepos = ('one', 'two', 'three')

            # when
            self.assertEqual(True, _isCloneExist(clonedRepos, 'one.git'))
            self.assertEqual(True, _isCloneExist(clonedRepos, 'one'))
            self.assertEqual(True, _isCloneExist(clonedRepos, 'two.git'))
            self.assertEqual(True, _isCloneExist(clonedRepos, 'two'))
            self.assertEqual(True, _isCloneExist(clonedRepos, 'three'))
            self.assertEqual(True, _isCloneExist(clonedRepos, 'three.git'))
            self.assertEqual(False, _isCloneExist(clonedRepos, 'four'))
            self.assertEqual(False, _isCloneExist(clonedRepos, 'four.git'))


      def test_new_file_path_created_with_nested_directories(self):
            
            # given
            content = "/var/www/"
            clones = "/home/git/"

            # when
            self.assertEqual("/var/www/One.md", _getNewPathForFile(content, clones, "/home/git/myRepo/" + readmeFileName, "One"))
            self.assertEqual("/var/www/Two.md", _getNewPathForFile(content, clones, "/home/git/myRepo/" + readmeFileName, "Two"))

            # and
            self.assertEqual("/var/www/nestedFilder/Two.md", _getNewPathForFile(content, clones, "/home/git/myRepo/nestedFilder/" + readmeFileName, "Two"))
            self.assertEqual("/var/www/nestedFilder/folder2/Two.md", _getNewPathForFile(content, clones, "/home/git/myRepo/nestedFilder/folder2/" + readmeFileName, "Two"))




def main():
    unittest.main()

if __name__ == '__main__':
    main()