import unittest

import itchat


class TestItchat(unittest.TestCase):

    def setUp(self):
        print("======start setting up======")
        itchat.auto_login(hotReload=True)

    def tearDown(self):
        print("======start tearing down======")
        itchat.logout()
