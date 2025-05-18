class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print("10°C =", TemperatureConverter.celsius_to_fahrenheit(10), "°F")  
print("25°C =", TemperatureConverter.celsius_to_fahrenheit(25), "°F") 
print("-40°C =", TemperatureConverter.celsius_to_fahrenheit(-40), "°F")  
