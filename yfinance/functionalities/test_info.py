"""Run tests for isolated info from base.py lines 332 to 347.

If all tests are passing, the output will print OK.
Otherwise, error output from the tests will be shown indicating which assertion
failed.

    usage example:
        unittest.main()
"""

import unittest
from info import info_func

class TestInfo(unittest.TestCase):
    
    def test_website_field(self):
        url = "https://www.domainName.com/"
        urlPartial = "domainName.com"
        expectedOutput = "https://logo.clearbit.com/{}".format(urlPartial)
        info = info_func({'website': url})
        self.assertEqual(info['logo_url'], expectedOutput)


    def test_no_website_field(self):
        info = info_func({})
        self.assertEqual(info['logo_url'],'')

    
    def test_return_dict(self):
        info = info_func({})
        self.assertTrue(isinstance(info,dict))


    def test_data_keys_with_MarketPrice(self):  
        data = {'summaryProfile': {1:1}, 
                  'summaryDetail': {2:2},
                  'quoteType': {3:3},
                  'defaultKeyStatistics': {4:4},
                  'assetProfile': {5:5},
                  'financialData': {6:6},
                  'regularMarketOpen':{7:7}}
        output_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 'logo_url': '', 'regularMarketOpen': {7,7}}
        info = info_func(data)
        self.assertDictEqual(info, output_dict) 
        
        
    def test_data_keys_without_MarketPrice(self):  
        data = {'summaryProfile': {1:1}, 
                  'summaryDetail': {2:2},
                  'quoteType': {3:3},
                  'defaultKeyStatistics': {4:4},
                  'assetProfile': {5:5},
                  'financialData': {6:6}}
        output_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 'logo_url': '', 'regularMarketOpen': ''}
        info = info_func(data)
        self.assertDictEqual(info, output_dict) 
                  
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
    unittest.main()