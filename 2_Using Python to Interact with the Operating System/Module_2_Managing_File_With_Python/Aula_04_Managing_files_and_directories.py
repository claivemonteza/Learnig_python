import os
import datetime

# Will remove the file
# the second remove will throw a exception for not find the file
# os.remove("Aula_04_Managing_files_and_directories.txt")

# Will rename the file
# os.rename("Aula_04_rename_file_name.txt", "Aula_04_file_renamed.txt")

# this code  checks whether or not a file exists.
# os.path.exists("Aula_04_file_renamedg.txt")

# This code will provide the file size
os.path.getsize("Aula_04_file_renamed.txt")

# This code will provide a unix timestamp for the file
os.path.getmtime("Aula_04_file_renamed.txt")

# This code will provide the date and time for the file in an 
# easy-to-understand format
timestamp = os.path.getmtime("Aula_04_file_renamed.txt")
datetime.datetime.fromtimestamp(timestamp)

# This code takes the file name and turns it into an absolute path
os.path.abspath("Aula_04_file_renamed.txt")


# Directory
# This code snippet returns the current working directory.
print(os.getcwd())

# The os.mkdir("new_dir") function creates a new directory called new_dir
os.mkdir("new_dir")


# This code snippet changes the current working directory to new_dir. 
# The second line prints the current working directory.
os.chdir("new_dir")
os.getcwd()

# This code snippet creates a new directory called newer_dir. 
# The second line deletes the newer_dir directory.
os.mkdir("newer_dir")
os.rmdir("newer_dir")

# This code snippet returns a list of all the files and 
# sub-directories in the website directory.
os.listdir("website")


# Here is the code all together. 
# This code defines a dir variable with the name of the directory that we want to check. 
# This makes our code more readable and more usable. 
# Then, it iterates through the file names returned by the os.listdir(). 
# We know from our previous execution of this function that these are just the names of the files without directory. 
# By using os.path.join(), we join the directory to each of those file names and create a string with a valid full name. 
# Finally, we use that full name to call os.path.isdir() to check if it's a directory or a file. 
 dir = "website"
 for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))