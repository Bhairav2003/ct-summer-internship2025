# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

test_cases = [" .*\\+", ".*+"]
T = len(test_cases)

for S in test_cases:
    try:
        re.compile(S)
        print("True")
    except re.error:
        print("False")