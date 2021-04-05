import unittest
import json
from explogger import ExpLogger


class Test_ExpLogger(unittest.TestCase):
    def setUp(self):
        self.eLogger = ExpLogger()

    def test_logResults(self):
        _ = self.eLogger.logResults('PG','Sharpe',122)
        _ = self.eLogger.logResults('PG','MaxDD',5)
        ret = self.eLogger.logResults('DDPG','MaxDD',1500)
        self.assertTrue('PG' in ret)

    def test_saveResults(self):
        self.test_logResults()
        ret = self.eLogger.saveResults('unitTests.json')
        self.assertTrue(ret)

if __name__ == '__main__':
    unittest.main()