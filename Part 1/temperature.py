TEMPERATUE_SCALES = "kelvin", "fahrenheit", "celsius"

def convert_to_celsius(degrees, source="fahrenheit"):
    if source.lower() == "fahrenheit":
        return (degrees - 32) * (5/9)
    elif source == 'kelvin':
        return degrees - 273.15
    else:
        return f"Error converting form f{source}"   