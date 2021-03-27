# Test Case Report #2
## General Information
**Test Stage:** Functionality <BR>
**Test Date:** 27/03/2021 <BR>
**System Test Date:** 27/03/2021 <BR>
**Tester:** Group 2<BR>
**Test Case Number:** 2 <BR>
**Test Case Description:** Verify the key `logo_url` is in the dictionary and its value is correct. <BR>
**Results:** Pass<BR>
## Introduction
**Requirement(s)to be tested:** info from base.py line 332 to 347. <BR>
**Set Up Procedures:** Run `test_info.py` file to get test results. Ensure that `info.py` is in the same directory as it contains the functionality to be tested. <BR>
**Stop Procedures:** Test stops by itself and reports results. <BR>
## Environmental Needs
**Hardware:** No specific hardware requirements. <BR>
**Software:** Must have python3, unittest, and doctest installed. <BR>
**Procedural Requirements:** There are no constraints on the test procedures necessary to execute the test case. <BR>
## Test
**Test Items and Features:** This test checks that 'logo_url' is a key of the output and that its value matches up with what is expected.<BR>
**Input Specifications:** The input for this test case is an empty dictionary for the first run, then a dictionary with 'website' as a key with a url as a value.<BR>
**Procedural Steps:** From the command line enter `python test_info.py`. Test test cases have already been set up to run automatically with test inputs and expected output. `unittest` runs the test and print if there is a mismatch between expected output and output from the test.<BR>
**Expected Results of Case:** The anticipated outcome is no errors and that the result when no url is provided is an empty string and a newly formatted url prepended with 'logo.clearbit.com' when a url is provided.<BR>
## Actual Results
**Output Specifications:** The output of this case is a success. The value of 'logo_url' is output correctly with or without a website url being provided.<BR><BR>
![Error Output](img/keyError.png)
