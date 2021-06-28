# Python TTD Task
## The Task
- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
- create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive 
- create a method in the class to pass the test

- Psuedocode
```
calculate remainder of 2 numbers
test if remainder == 0
if True, return True, test has passed
if False, return False, test has failed

calculate remainder of 2 numbers
test if remainder => 0
if True, return True, test has passed
if False, return False, test has failed
```

## Step 1 - Creating the test file
```py
# Importing unittest and pytest for the test to able to run

import pytest
import unittest

from remainder_calc import Remainder  # Importing class from file


class RemainderTest(unittest.TestCase):
    rem = Remainder()

    def test_remain(self):  # Test for seeing if result == True when remainder is 0
        self.assertEqual(self.rem.remain(4, 2), True)

    def test_positive(self):  # Test for seeing  result == True when remainder is positive
        self.assertEqual(self.rem.positive(5, 2), True)
```

## Step 2 - Writing the code to pass the test

```python
class Remainder:  # Creating the class, making sure it's the same as the test file
    def remain(self, num1, num2):  # Method for finding if remainder is 0
        if num1 % num2 == 0:
            return True

    def positive(self, num1, num2):  # Method for finding if remainder is positive
        if num1 % num2 >= 0:
            return True
```