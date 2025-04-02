import requests

# Function to check if Pokémon exists in PokeAPI
def check_pokemon_exists(pokemon_name):
    # Convert input to lowercase to handle case-insensitivity
    
    # Make a GET request to the PokeAPI
    response = requests.get(url)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        print(f"{pokemon_name.capitalize()} found!")
        # You can now proceed with your code (e.g., display Pokémon data, etc.)
        data = response.json()  # Store the data if you want to use it
        # For example, print the Pokémon's ID
        print(f"ID: {data['id']}")
    else:
        print(f"{pokemon_name.capitalize()} not found. Please check the spelling and try again.")

# Get the user's input for the Pokémon name
pokemon_name = input("Enter a Pokémon name: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
# Check if the Pokémon exists
check_pokemon_exists(pokemon_name)