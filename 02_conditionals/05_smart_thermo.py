device_status = str(input("Is the smart thermostat on? (on/off): ").strip().lower())
temperature = float(input("Enter the current temperature (in °C): "))

if device_status == "on":
    if temperature < 20:
        print("The thermostat is on and the temperature is low. Heating is active.")
    elif 20 <= temperature <= 25:
        print("The thermostat is on and the temperature is optimal. Maintaining current settings.")
    else:
        print("The thermostat is on and the temperature is high. Cooling is active.")
elif device_status == "off":
    print("The thermostat is off. No temperature regulation is active.")