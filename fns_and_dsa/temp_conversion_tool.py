FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



def convert_to_celsius(fahrenheit):
        cle_value = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
        print(f"{fahrenheit}°F is {cle_value}°C")


def convert_to_fahrenheit(celsius):
        fah_value = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{celsius}°C is {fah_value}°F")


temp = float(input("Enter the temperature to convert: "))
cel_or_fah= input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if cel_or_fah == "c":
    convert_to_fahrenheit(celsius = temp)
    
elif cel_or_fah == "f":
     convert_to_celsius(fahrenheit = temp)

else:
    print("Invalid Input")


