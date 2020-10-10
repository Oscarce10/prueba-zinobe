# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import sys
sys.path.insert(1, '../src')
import api_module as api
import unittest

class TestAPI(unittest.TestCase):
    def test_received_regions(self):
        result = api.getRegiones()
        self.assertIsNotNone(result)

    def test_country(self):
        regiones = api.getRegiones()
        for i in regiones:
            self.assertIsNotNone(api.getPaisPorRegion(i))
    


if __name__ == "__main__":
    unittest.main()