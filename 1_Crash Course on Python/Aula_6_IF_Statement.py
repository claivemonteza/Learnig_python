
#IF

temperature = 35

if temperature > 30 :
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:#(20,30]
    print("It's nice day")
elif temperature > 10:#(10,20]
    print("It's a bit cold")
print('Done')

#IF ELSE

temperature = 5

if temperature > 30 :
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's nice day")
print('Done')