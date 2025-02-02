class UnitConverter:
    def km_to_miles(self, km):
        return km * 0.621371
    
    def miles_to_km(self, miles):
        return miles / 0.621371
    
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
