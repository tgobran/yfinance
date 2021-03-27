# Introduction

### Objectives

Our test object is to isolate (separate the code into its own function) and test the **info** function of the Yahoo Finance Market Data Downloader application.<br>

### Team Members

- Ayooluwa Oladosu
- Beth Ding
- Lidia Ataupillco Ramos
- Jonathan Ong
- Tyler Gobran

# Research and Screening

### Issues Related to the Code

- **Issue #637**
  - Dictionary access of `regularMarketOpen` must be done conditionally.
- **Issue #604**
  - Questionable re-assignment of `regularMarketPrice` to `regularMarketOpen`
- **Issue #569**
  - Incorrect data for `regularMarketPrice`
- **Issue #353**
  - `regularMarketOpen` not always a dictionary key.
- **Issue #333**
  - `regularMarketOpen` not always a dictionary key.

### Pull Requests Related to the Code

- **PR #629**
  - Filtering out errors necessitates check for a missing conditional.
- **PR #628**
  - `regularMarketPrice` wrongly assigned to `regularMarketOpen`.
- **PR #620**
  - Info put into a Try block.
- **PR #590**
  - Changed data structure holding Info data elements.
- **PR #498**
  - Moves Info section into a try block.
- **PR #409**
  - Adds significant error handling to the Info section
- **PR #354**
  - Moves `regularMarketOpen` to a conditional
- **PR #321**
  - Data structure name change.
- **PR #309**
  - Small refactoring work.

# Problems Found

- The access of the `regularMarketOpen` dictionary value can fail (keyError).
  - `regularMarketOpen` is not always defined in the dictionary.

# Planned Tests

- Test that the return value of info is a dictionary as expected
- Test the website field in the returned dictionary works regardless of whether a url is provided or not
- Test that the functionality works when `regularMarketOpen` is defined
- Test that the functionality works when `regularMarketOpen` is not defined

# Assumptions / Risks

### Assumptions

- Since the exact values coming into our function is unknown, we assume that the dummy test values used during tests do not have an impact on the correctness of the functionality. That is if our dummy value is a dictionary of integers, whereas in production it is a dictionary of strings, this does not affect our testing. This is a fair assumption to make because our functionality only deals with the keys of the dictionary, not the values themselves. So as long, as the key types match, testing should work as expected.
- The expected output of the function is unclear. One line in the code seems to indicate that the output dictionary should have a key called `regularMarketPrice`, however, this line causes an error depending on the input. Therefore, it is unclear whether the line should be removed completely which will result in the output not having `regularMarketPrice` as a key or if the line should be modified so that `regularMarketPrice` is still a key, but the line it is on does not cause an error. As it stands, the assumption is that the output dictionary should have `regularMarketPrice` as a key with an empty string as a default value.

### Risks

- Since expected output is slightly unclear, fixing the issue may cause some of the implemented tests to fail since they were created with an output changing assumption.

# Test Approach

- Our approach to testing is to use automation so that tests can be run quickly and whenever updates are made to the code base.

# Test Environment

- The testing environment is python. Tests were created using `unittest`, a python testing framework and `docstrings` for some documentation on how to run the code.

# Software Fixing

### Pull Requests

- Pull request #590 addresses the issue of the KeyError, `regularMarketOpen`, from happening on every run of the function. The proposed solution is that instead of `regularMarketOpen` being a key to info defined within the function, it is a key to data which is passed in as input.

### Quick Fixes

- There is not a quick fix to this solution that we could implement without knowledge of the structure of the dictionary and what the keys of the dictionary are. In order to get an example of the dictionary structure, the value `self.ticker` must be defined. This value is not defined within `base.py`. It is sent as an argument to the constructor of the class. Following where the class is used in code, leads to a long inheritance that still does not reveal potential values that causes this bug. As such a quick fix is not possible on our end.
