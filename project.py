#This program is being made to convert degrees fahrenheit to degrees celsius.



#Prompt user to input the degrees fahrenheit
degrees_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

#Convert Fahrenheit to Celsius
degrees_celsius = (degrees_fahrenheit-32) * (5/9)

#Display degrees Celsius
print ("The temperature in celsius is: ", f'{degrees_celsius:.1f}',"°")