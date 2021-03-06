import sublime

import unittest
import os
import sys


class TestImport(unittest.TestCase):
    mpath = None

    @classmethod
    def setUpClass(cls):
        basedir = os.path.dirname(__file__)
        mpath = os.path.normpath(os.path.join(
            basedir, "..", "st3_{}_{}".format(sublime.platform(), sublime.arch())))
        if mpath not in sys.path:
            cls.mpath = mpath
            sys.path.append(mpath)

    def test_import(self):
        import psutil
        self.assertTrue("psutil" in sys.modules)
        self.assertTrue(psutil.cpu_count() > 0)

    @classmethod
    def tearDownClass(cls):
        if not cls.mpath:
            return
        mpath = cls.mpath
        if mpath in sys.path:
            sys.path.remove(mpath)
        if "psutil" in sys.modules:
            del sys.modules["psutil"]
