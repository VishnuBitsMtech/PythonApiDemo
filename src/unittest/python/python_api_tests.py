from mockito import mock, verify
import unittest

from python_api import helloworld

class PythonApiTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        out = mock()

        helloworld(out)

        verify(out).write("Hello world of Python\n")