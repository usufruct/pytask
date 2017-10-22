import unittest
import uuid
import json
from pytask import Task

class TestAreWeTests(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, True)

    def test_ping(self):
        task = Task('foo', 'bar')
        self.assertEqual(task.ping(), 'pong')

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.task = Task('respondey', 'secretey')

    def test_is_dictionary(self):
        self.assertIsInstance(self.task.message, dict)

    def test_has_respond_to(self):
        self.assertEqual(self.task.message["respond_to"], 'respondey')

    def test_has_param_secret(self):
        self.assertEqual(self.task.message["params"]["secret"], 'secretey')

class TestMessageFormatting(unittest.TestCase):
    def setUp(self):
        self.task = Task(uuid.uuid1(), 34)

    def test_respond_to_is_a_string(self):
        self.assertIsInstance(self.task.message["respond_to"], str)

    def test_param_secret_is_a_string(self):
        self.assertIsInstance(self.task.message["params"]["secret"], str)

class TestJsonMessage(unittest.TestCase):
    def setUp(self):
        self.task = Task('respondey', 'secretey')

    def test_is_json(self):
        self.assertEqual(self.task.json_message(), json.dumps(self.task.message))


# what is this?
if __name__ == '__main__':
    unittest.main()
