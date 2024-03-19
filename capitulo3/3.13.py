scale = input("If you want to convert from Farenheit to Celcius, enter F\n"
              "If you want to convert from Celsius to Farenheit, enter C: ")

scale = scale.upper()

print("\n")

temperature = float(input("Enter the temperature you want to convert: "))

print("\n")

if scale == "C":
   convertedTemperature = temperature * 9/5 + 32
   print(f'Converting {temperature:5.2f} Celsius to Farenheit')
   print(f'Resulting temperature = {convertedTemperature:5.2f} °C')
else:
   convertedTemperature = (temperature - 32) * 5/9
   print(f'Converting {temperature:5.2f} Farenheit to Celsius')
   print(f'Resulting temperature = {convertedTemperature:5.2f} °F')