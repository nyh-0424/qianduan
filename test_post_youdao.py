import unittest
from unittest import mock



from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)


    def test_get_ts(self):
      get_ts=mock.Mock(return_value='15846844357889')
      self.assertEqual('15846844357889',get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15846844357889')
        self.assertEqual('15846844357889',get_salt())

    def test_get_sign(self):
        self.assertEqual('4cf44da69384da8fb5c2364a31b22380',get_sign())

if __name__ == '__main__':
        unittest.main()
