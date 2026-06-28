#Temperature conversion programme ( Celsius-Kelvin-Fahrenheit-Reaumur-Rankine )

Temperature = float(input("Enter the temperature value that you want to convert: "))
unit = input(" What is the unit of the temperature? ( C / K / F / R / Rn ):")

if unit == "C":
    TemperatureInFahrenheit = Temperature * 9/5 + 32
    print(f"Temperature in Fahrenheit: {TemperatureInFahrenheit} F")
    TemperatureInKelvin = Temperature + 273
    print(f"Temperature in Kelvin: {TemperatureInKelvin} K")
    TemperatureInReaumur = Temperature * 4/5
    print(f"Temperature in Reaumur: {TemperatureInReaumur} R ")
    TemperatureInRankine = Temperature * 9/5 + 492
    print(f"Temperature in Rankine: {TemperatureInRankine} Rn")
elif unit == "F":
    TemperatureInCelsius = (Temperature - 32) * 5/9
    print(f"Temperature in Celsius: {TemperatureInCelsius} C")
    TemperatureInKelvin =(Temperature - 32) * 5/9 + 273
    print(f"Temperature in Kelvin: {TemperatureInKelvin} K")
    TemperatureInReaumur = ( Temperature - 32 ) * 4/9
    print(f"Temperature in Reaumur: {TemperatureInReaumur} R ")
    TemperatureInRankine = Temperature + 460
    print(f"Temperature in Rankine: {TemperatureInRankine} Rn")
elif unit == "K":
    TemperatureInFahrenheit = ( Temperature - 273 ) * 9 / 5 + 32
    print(f"Temperature in Fahrenheit: {TemperatureInFahrenheit} F")
    TemperatureInCelsius = Temperature - 273
    print(f"Temperature in Celsius: {TemperatureInCelsius} C")
    TemperatureInReaumur = ( Temperature - 273 ) * 4/5
    print(f"Temperature in Reaumur: {TemperatureInReaumur} R ")
    TemperatureInRankine = ( Temperature - 273 ) * 9 / 5 + 492
    print(f"Temperature in Rankine: {TemperatureInRankine} Rn")
elif unit == "R":
    TemperatureInFahrenheit =  Temperature * 9/4 + 32
    print(f"Temperature in Fahrenheit: {TemperatureInFahrenheit} F")
    TemperatureInCelsius = 5/4 * Temperature
    print(f"Temperature in Celsius: {TemperatureInCelsius} C")
    TemperatureInKelvin = Temperature * 5/4 + 273
    print(f"Temperature in Kelvin: {TemperatureInKelvin} K")
    TemperatureInRankine = 9/4 * Temperature + 492
    print(f"Temperature in Rankine: {TemperatureInRankine} Rn")
elif unit == "Rn":
    TemperatureInFahrenheit = Temperature - 460
    print(f"Temperature in Fahrenheit: {TemperatureInFahrenheit} F")
    TemperatureInCelsius = ( Temperature - 492 ) * 4/9
    print(f"Temperature in Celsius: {TemperatureInCelsius} C")
    TemperatureInKelvin = 5/9 * ( Temperature - 492 ) + 273
    print(f"Temperature in Kelvin: {TemperatureInKelvin} K")
    TemperatureInReaumur = 4/9 * ( Temperature - 492)
    print(f"Temperature in Reaumur: {TemperatureInReaumur} R ")
else:
    print(" The unit that you have entered is invalid. Please choose the Valid one.")

