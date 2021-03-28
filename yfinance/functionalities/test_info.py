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
    
    def test_return_dict(self):
        """Tests that the info method returns a dictionary type.
        
        Simple check that just ensures that a dictionary type is returned by an info_func call.
        
        """
        info = info_func({})
        self.assertTrue(isinstance(info,dict))
        
    
    def test_website_field(self):
        """Tests that the URL field is handled correctly.
        
        This test is a simple check to ensure that when provided with correct data, the
        info_func will return the correct results for the info field.
        
        This test relates to an issue we have seen with the regularMarketOpen value
        interfering with this.
        
        """
    
        url = "https://www.domainName.com/"
        urlPartial = "domainName.com"
        expectedOutput = "https://logo.clearbit.com/{}".format(urlPartial)
        info = info_func({'summaryProfile': {'website': url}, 'financialData':{'regularMarketOpen':7}})
        self.assertEqual(info['logo_url'], expectedOutput)

    def test_no_website_field(self):
        """Tests that the lack of a URL field is handled correctly.
        
        Variant of the previous test checking the opposite behaviour.
        
        """
    
        info = info_func({'financialData':{'regularMarketOpen':7}})
        self.assertEqual(info['logo_url'],'')


    def test_data_keys_with_MarketPrice(self):  
        """Tests that the dictionary output is correct when MarketPrice is set.
        
        Checks that there is correct behaviour in the info_func when the regularMarketOpen
        value is set in the input. This tests an issue we saw previously with the code.
        
        """
    
        data = {'summaryProfile': {1:1}, 
                  'summaryDetail': {2:2},
                  'quoteType': {3:3},
                  'defaultKeyStatistics': {4:4},
                  'assetProfile': {5:5},
                  'financialData':{'regularMarketOpen':7}}
        output_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 'logo_url': '', 'regularMarketPrice': 7, 'regularMarketOpen':7}
        info = info_func(data)
        print(info)
        self.assertDictEqual(info, output_dict) 
       
        
    def test_data_keys_without_MarketPrice(self):  
        """Tests that the dictionary output is correct when MarketPrice is not set.
        
        Variant of the previous function that ensures correct behaviour remains when
        the regularMarketOpen value is not set ahead of time.
        
        """
    
        data = {'summaryProfile': {1:1}, 
                  'summaryDetail': {2:2},
                  'quoteType': {3:3},
                  'defaultKeyStatistics': {4:4},
                  'assetProfile': {5:5},
                  'financialData': {6:6}}
        output_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 'logo_url': '', 'regularMarketPrice': ''}
        info = info_func(data)
        self.assertDictEqual(info, output_dict) 
                  
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()    
    unittest.main()
