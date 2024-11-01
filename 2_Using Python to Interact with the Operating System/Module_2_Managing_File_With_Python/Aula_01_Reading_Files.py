# open() method open de file
file = open("Aula_01_Reading_Files.txt")
# readLine() method reads one line from tje file 
print(file.readline())
# read() method reads the entire file and  returns it as a string
print(file.read())
#close() method closes the file
file.close()

# this will open the file and read all the line on the file then will close
with open("Aula_01_Reading_Files.txt") as file:
    print(file.readline())

#
with open("Aula_01_Reading_Files.txt") as file:
   for line in file:
        print(line.upper())    

# strip() method is used to remove the newline character, and we get output without empty lines.
with open("Aula_01_Reading_Files.txt") as file:
    for line in file:
        print(line.strip().upper())    

#
file = open("Aula_01_Reading_Files.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
