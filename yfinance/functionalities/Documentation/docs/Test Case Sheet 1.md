# Test Case Sheet #1
## System Test Case #1 <BR>
**Tester Name:** Group 2 <BR>
**Date(s) of Test:** 27/03/2021 <BR>
**Prerequisites for this test:** `python3`, `unittest`, and `doctest` installed <BR>
**Required Configuration:** run `test_info.py` <BR>
**NOTES and RESULTS:**<BR>
  Due to line `info['regularMarketPrice'] = info['regularMarketOpen']`, `regularMarketOpen` is not defined in the `info` dictionary, therefore test failed.<BR><BR>
## TEST SCRIPT STEPS/RESULTS
| **STEP** | **TEST STEP/INPUT** | **EXPECTED RESULTS** | **ACTUAL RESULTS** | **Requirements Validated** | **PASS/FAIL** |
| --- | --- | --- | --- | --- | --- |
|1.| Enter `python test_info.py` in command line | return a dictionary with no errors | `KeyError: 'regularMarketOpen'` | | FAIL|
