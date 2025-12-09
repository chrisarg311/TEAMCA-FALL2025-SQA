import unittest
import importlib.util
from pathlib import Path

module_path = Path("MLForensics-farzana/mining/git.repo.miner.py")
spec = importlib.util.spec_from_file_location("git.repo.miner", module_path)
gitrepominer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gitrepominer)

#from MLForensics_farzana/mining/git.repo.miner.py import getPythonCount, getMLStats
#from MLForensics_farzana/mining/mining.py import giveTimeStamp, makeChunks, days_between


class getPythonCountTests(unittest.TestCase):

  def getPythonCount1(self):
    self.assertEqual(getPythonCount(Path(__file__).resolve().parentprint(script_dir)), 1)
