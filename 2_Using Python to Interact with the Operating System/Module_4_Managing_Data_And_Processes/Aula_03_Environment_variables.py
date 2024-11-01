import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# to read python file in line on command line (bash)
# cat Aula_03_Environment_variables.py

#execute the file in line on command line (bash)
# ./Aula_03_Environment_variables.py

# to input a value on a environ on command line BASH
#export FRUIT=Pineaple