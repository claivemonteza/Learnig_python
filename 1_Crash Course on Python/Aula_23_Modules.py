
# two way to import modules
# One
import converters

print(converters.kg_to_lbs(70))

# Two
from converters import kg_to_lbs

print(kg_to_lbs(70))

