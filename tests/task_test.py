import unittest
from pytask import Task

class TestAreWeTests(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, True)

    def test_pint(self):
        task = Task()
        self.assertEqual(task.ping(), 'pong')

# what is this?
if __name__ == '__main__':
    unittest.main()
