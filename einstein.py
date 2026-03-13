def einstein(mass):
    # Calculate the energy equivalent of a given mass using Einstein's equation E=mc^2 
    speed_of_light = 299792458  # Speed of light in meters per second
    energy = mass * (speed_of_light ** 2)
    return energy

result = einstein(1) 
print(f"The energy equivalent of 1 kg of mass is: {result} joules")
