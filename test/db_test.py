# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import sys
sys.path.insert(1, '../src')
import db_module as db
import unittest

class TestDB(unittest.TestCase):
    def testCreateDB(self):
        bd = db.ConexionDB()
        self.assertIsNotNone(bd)

if __name__ == "__main__":
    unittest.main()