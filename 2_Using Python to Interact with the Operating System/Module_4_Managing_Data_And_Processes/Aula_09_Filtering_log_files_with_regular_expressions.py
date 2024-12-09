import sys
import re


# To open a file received as parameter of out script, we can use code like this one.
logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    print(line.strip())


# Remember that for performance reasons, when files are large, it's generally good pratices 
# to read them line by line instead of loading the entire contents into memory.
logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    print(line.strip())


# In this example, we'll use escape characters, capture groups, and the end of strings anchor.
logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])