import unittest
from collectDocumentation import _isCloneExist

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

def main():
    unittest.main()

if __name__ == '__main__':
    main()