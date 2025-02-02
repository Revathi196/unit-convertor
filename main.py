from converter import UnitConverter

def main():
    converter = UnitConverter()
    
    print("10 kilometers to miles:", converter.km_to_miles(10))
    print("5 miles to kilometers:", converter.miles_to_km(5))
    print("100 Celsius to Fahrenheit:", converter.celsius_to_fahrenheit(100))
    print("212 Fahrenheit to Celsius:", converter.fahrenheit_to_celsius(212))

if __name__ == "__main__":
    main()
