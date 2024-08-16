print("Mountains".upper())

print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

print(" yes ".strip())

print(" yes ".lstrip())

print(" yes ".rstrip())

print("The number of times e occurs in this string is 4".count("e"))

print("Forest".endswith("rest"))

print("Forest".isnumeric())

print("12345".isnumeric())

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))

print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))


name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
