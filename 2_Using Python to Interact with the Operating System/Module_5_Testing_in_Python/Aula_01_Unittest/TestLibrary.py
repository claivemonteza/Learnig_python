import unittest
from Library import Library

# Unit test for the Library system
class TestLibrary(unittest.TestCase):

	def test_adding_book_to_library(self):
    	# Arrange
		library = Library()
		new_book = "Python Design Patterns"
    	# Act
    	library.add_book(new_book)
    	# Assert
    	self.assertTrue(library.has_book(new_book))

# Running the test
library_test_output = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
print(library_test_output)