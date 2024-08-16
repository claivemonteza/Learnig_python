def greeting(name,department):
    print("Welcome, "+name)
    print("You are part of", department)

greeting("Claive", "Software engineering")


def area_triangle(base, height):
    return base*height/2

print(area_triangle(4, 2))

## or using keyword arguments
print(area_triangle( height=2, base=4))

