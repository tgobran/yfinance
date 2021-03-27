# Test Case Report
**Test Stage:** Functionality <BR>
**Test Date:** 27/03/2021 <BR>
**System Test Date:** 27/03/2021 <BR>
**Tester:** Group 2<BR>
**Test Case Number:** 1 <BR>
**Test Case Description:** Verify the return value is a dictionary. <BR>
**Results:** Fail <BR>
**Requirement(s)to be tested:** info from base.py line 332 to 347. <BR>
**Set Up Procedures:** run `test_info.py` file to get test results. Ensure that `info.py` is in the same directory as it contains the functionality to be tested. <BR>
**Stop Procedures:** Test stops by itself and reports results. <BR>
**Hardware:** No specific hardware requirements. <BR>
**Software:** Must have python3, unittest, and doctest installed. <BR>
**Procedural Requirements:** There are no constraints on the test procedures necessary to execute the test case. <BR>
**Test Items and Features:** This test checks that the functionality runs with no errors and returns a dictionary as expected.<BR>
**Input Specifications:** The input for this test case is an empty dictionary.<BR>
**Procedural Steps:** From the command line enter `python test_info.py`. Test test cases have already been set up to run automatically with test inputs and expected output. `unittest` runs the test and print if there is a mismatch between expected output and output from the test.<BR>
**Expected Results of Case:** The anticipated outcome is no errors and that the result is a dictionary. To check this, we verify that the output is of type `dict` and that no errors are raised during the test.<BR>
**Output Specifications:** The output of this case is a KeyError from python due to the line `info['regularMarketPrice'] = info['regularMarketOpen']`. 'regularMarketOpen' is not defined in the info dictaionary. As such, the test failed as no errors was the expected output of the test<BR>
![Error Output](img/keyError.png)