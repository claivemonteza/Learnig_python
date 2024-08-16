weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
converted = 0
auxUnit = ''

if unit.lower() == 'k':
    converted = weight / 0.45
    auxUnit = 'Lbs'
else:
    converted = weight * 0.45
    auxUnit = 'Kg'
print('Weight in '+auxUnit+': '+ str(converted))