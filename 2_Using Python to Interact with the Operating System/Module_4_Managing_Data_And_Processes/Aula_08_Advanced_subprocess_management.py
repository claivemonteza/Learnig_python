import os
import subprocess
import pathlib

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)


cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()
print(cwd_subprocess)



cwd_pathlib = Path.cwd()
print(cwd_pathlib)


cwd_os = os.getcwd()
print(cwd_os)

os.mkdir('test_dir_os2')

test_dir_pathlib2 = Path('test_dir_pathlib2')

test_dir_pathlib2.mkdir(exist_ok=True) #Ensures the directory is created only if it doesn't already exist