# Print an introduction for the user
print("Welcome to the band name generator!")

# Ask the user to input their favourite place and favourite animal, store what they enter in variables
place = input("What is your favourite place? ")
animal = input("What is your favourite animal? ")

# 3. Format a band name. You could either use a "+"" or a ",", or use an f string.
band_name = place + " " + animal

# 4. Output the band name to the console
print("Your band name could be: " + band_name)