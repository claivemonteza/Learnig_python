try:
  # Try to append to a file that is normally not writable
  # for anyone other than root 
  f = open("/etc/hosts", "w+")
except IOError as ex:
  # The variable "ex" will hold details about the error
  # that occurred
  print("Error appending to file: " + str(ex))
else:
  # If there was no exception, close the file.
  f.close()
  
  
try:
  print(x)
except NameError:
  print("Variable x is not defined")
  
  

x = "hello"
if not isinstance(x, int):
  raise TypeError("Only integers are allowed")



def start_server(port):
  if not isinstance(port, int):
    raise TypeError("Port number must be an integer")
  elif port < 1024 or port > 65535:
    raise ValueError("Port number is invalid")