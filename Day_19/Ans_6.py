# Convert a list of temperatures from Celsius to Fahrenheit using map().
temp_c = [19,32,67,200,7]
def convert(n):
    result = ((n*(9/5))+32)
    return result
temp_f = list(map(convert,temp_c))
for x in range(0,len(temp_c)):
    print(f"temp in celcius ={temp_c[x]} temp in fahrenheit ={temp_f[x]:.2f}")