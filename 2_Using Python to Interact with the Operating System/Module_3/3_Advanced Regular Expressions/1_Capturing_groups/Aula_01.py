
##This follow-along reading is organized to match the content in the 
# video that follows. 
# It contains the same code shown in the next video. 
# These code blocks will provide you with the opportunity to see how 
# the code is written, allow you to practice running it, and can be used
#  as a reference to refer back to.

import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])