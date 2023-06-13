
#We start with a print statment welcoming the user to our program
print("Welcome to my Silly Sentence Generator")

# We create a variable and get the user to input a word. What the user types is stored in the variable
name = input("Enter your name ")

adj = input("Enter an adjective ( describing word ) ")

food = input("Enter a type of food ")

place = input("Enter a place ")

# We then create a new variable to put together our sentence. We use an f-string to use the variables from our questions
sentence = f"{name} is a {adj} goat. They like to eat {place} and live in {food}"

# We then print the created sentence to the screen
print(sentence)