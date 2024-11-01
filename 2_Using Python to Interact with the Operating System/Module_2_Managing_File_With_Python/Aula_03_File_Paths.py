import os
# File paths are the specific location of a file on a computer or web server. you also can use them to call environment variable.

# there ara two types of file paths : RELATIVE and ABSOLUTE.

# RELATIVE file paths is used do read and write files by the file name alone.
# RELATIVE file paths default to the specific directory where the python command was initially run.
# 
# ABSOLUTE file paths spell out the exact locationof the file - drive, name, then directory, then file name.

# RELATIVE file paths 
# EX: Aula_01, Aula_02


# ABSOLUTE file paths 

# CWD (Current Working Directory) Command
outputs['current_directory_before'] = os.getcwd()
outputs['files_and_directories'] = os.listdir()
outputs['path_value'] = os.environ.get('PATH')

