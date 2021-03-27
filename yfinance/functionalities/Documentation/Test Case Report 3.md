# Test Case Report
**Test Stage:** Functionality <BR>
**Test Date:** 27/03/2021 <BR>
**System Test Date:** 27/03/2021 <BR>
**Tester:** Group 2<BR>
**Test Case Number:** 3 <BR>
**Test Case Description:** Verify the function runs when 'MarketPrice' is a key in the input dictioary and when it is not.<BR>
**Results:** Fail <BR>
**Requirement(s)to be tested:** info from base.py line 332 to 347. <BR>
**Set Up Procedures:** run `test_info.py` file to get test results. Ensure that `info.py` is in the same directory as it contains the functionality to be tested. <BR>
**Stop Procedures:** Test stops by itself and reports results. <BR>
**Hardware:** No specific hardware requirements. <BR>
**Software:** Must have python3, unittest, and doctest installed. <BR>
**Procedural Requirements:** There are no constraints on the test procedures necessary to execute the test case. <BR>
**Test Items and Features:** This test checks that the function runs .<BR>
**Input Specifications:** The input for this test case is an dictionary of dictionaries. On the first run, 'regularMarketOpen' is a key in the dictionary and on the second run it is absent.<BR>
**Procedural Steps:** From the command line enter `python test_info.py`. Test test cases have already been set up to run automatically with test inputs and expected output. `unittest` runs the test and print if there is a mismatch between expected output and output from the test.<BR>
**Expected Results of Case:** The anticipated outcome is no errors and that the result is a dictionary containing the values of the input dictionary of dictionary. In the case where 'regularMarketOpen' is not a key, 'regularMarketPrice' would be an empty string. When it is a key, 'regularMarketPrice' would have a value matching the input dictionaries value<BR>
**Output Specifications:** The output of this case is a KeyError from python due to the line `info['regularMarketPrice'] = info['regularMarketOpen']`. 'regularMarketOpen' is not defined in the info dictaionary. As such, the test failed as no errors was the expected output of the test with a populated dictionary matching the values of the input dictionary.<BR>
![Error Output](img/keyError.png)