def convert_fanhrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


print(convert_fanhrenheit_to_celsius(45))

def convert_celsius_to_fanhrenheit(celsius):
    fanhrenheit = (celsius * 9 / 5) + 32

    return fanhrenheit


print(convert_celsius_to_fanhrenheit(12))
