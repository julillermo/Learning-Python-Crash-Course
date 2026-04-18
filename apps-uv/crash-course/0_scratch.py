# A Passing Test

import unittest
from name_function import get_formatted_name

# When naming a Class for testing, be sure to inlcude 'Test' in the name
class NamesTestCase(unittest.TestCase):
    """ Tests for the funtion """
    # This is effectively a child class of unittest.TestCase
    # This class inherits from the unittest.TestCase

    # no def __init__() ????

    # Any method that starts with 'test_' will automatically run
    # when the Python file (this code) opens
    def test_first_last_name(self):
        """ Do names like 'Janis Joplin' work? """

        # inside the 'test_' functions we call functions we want to test
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

        # .assert is a unittest specific method
        # "Assert methods verify that a resuilt you received matches
        #   the result you expected to receive."

# the if block below 
if __name__ == '__main__':
    unittest.main()