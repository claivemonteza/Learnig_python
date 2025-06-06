import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    if result is None:
      continue
    name = result[1]
    usernames[name] = usernames.get(name,0)+1
print(result[1])