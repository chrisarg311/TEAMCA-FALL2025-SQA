import unittest
import importlib.util
from pathlib import Path
from datetime import datetime

module_path = Path("MLForensics-farzana/mining/git.repo.miner.py")
spec = importlib.util.spec_from_file_location("git.repo.miner", module_path)
gitrepominer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gitrepominer)


module_path2 = Path("MLForensics-farzana/mining/mining.py")
spec2 = importlib.util.spec_from_file_location("mining", module_path2)
mining = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(mining)



class TestGetPythonCount(unittest.TestCase):

  def test_getPythonCount1(self):
    self.assertEqual(gitrepominer.getPythonCount(Path(__file__).resolve().parent), 13)

  def test_getPythonCount2(self):
    self.assertEqual(gitrepominer.getPythonCount("green"), 13)

  def test_getPythonCount3(self):
    self.assertEqual(gitrepominer.getPythonCount(13), Path(__file__).resolve().parent)


class TestGetMLStats(unittest.TestCase):

  def test_getMLStats1(self):
    self.assertEqual(gitrepominer.getMLStats(Path(__file__).resolve().parent), 1)

  def test_getMLStats2(self):
    self.assertEqual(gitrepominer.getMLStats("directory"), 1)

  def test_getMLStats3(self):
    self.assertEqual(gitrepominer.getMLStats("path"), "anotherPath")


class TestGiveTimeStamp(unittest.TestCase):

  def test_giveTimeStamp1(self):
    self.assertEqual(mining.giveTimeStamp(), datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

  def test_giveTimeStamp2(self):
    self.assertEqual(mining.giveTimeStamp(), "11:11:11")


#class TestMakeChunks(unittest.TestCase):

  #def test_(self):
    #self.assertEqual()

  #def test_(self):
    #self.assertEqual()


class TestDaysBetween(unittest.TestCase):

  def test_daysBetween1(self):
    self.assertEqual(mining.days_between("Tuesday", "Friday"), ERROR_FORMAT)

  def test_daysBetween2(self):
    self.assertEqual(mining.days_between(datetime(1989, 6, 6), datetime(1989, 6, 10), 4))


if __name__ == '__main__':
  unittest.main()
