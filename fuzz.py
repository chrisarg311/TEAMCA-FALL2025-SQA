import unittest
from pathlib import Path

from MLForensics-farzana/mining/git.repo.miner.py import getPythonCount, getMLStats
from MLForensics-farzana/mining/mining.py import giveTimeStamp, makeChunks, days_between


class getPythonCountTests(unittest.TestCase):

  def getPythonCount1(self):
    self.assertEqual(getPythonCount(Path(__file__).resolve().parentprint(script_dir)), 1)
