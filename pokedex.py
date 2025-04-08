import requests
import json
import os

pokeAPI = "https://pokeapi.co/api/v2/pokemon/"
def start():
    """
        only runs once to determine whether or not there are already pokemon in the users party and to allow the user to reset
    """
    try:
        open("pokemonTeam.json", "x") #attempts to create pokemon.json file
        print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.") #since the file does not exist, it is assumed that the user has not interacted with the system before

    except:
        if os.path.getsize("pokemonTeam.json") > 0: #checks if the json file contains anything
            restart = ""
            while restart not in ["yes", "no"]:
                restart = input("It appears that you already have a registered team. would you like to restart? ('yes' to clear memory, 'no' to continue with previous team): ").lower()

                if restart == "yes":
                    open("pokemonTeam.json", "w").close() #clears memory and resets the system
                    print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")

                elif restart == "no":
                    print("welcome back young traveler") #does not clear memory
                   
                else:
                    print("invalid input")
        else:
            print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.") #since the file is empty, it is assumed that the user has not interacted with the system before

    print("If you require instructions try typing 'help' \n")


def Search_Pokemon(pokemon):
    response = requests.get(f"{pokeAPI}{pokemon.lower()}") #makes a request to the api using the pokemons name
    if response.status_code == 200: #Checks if the entered pokemon is in the api
        data = response.json() #turns the made request into a readable json file
        pokemonId = data["species"]["url"] #finds the url for the species directory of Pokeapi so pokedex entries can be accessed

        dexResponse = requests.get(f"{pokemonId}") #makes a request to the api using the pokemons id as a species
        dexData = dexResponse.json() #turns the made request into a readable json file
       
        baseStats = [baseStat["base_stat"] for baseStat in data["stats"]]
        baseStatTotal = sum(baseStats)
        #itterates through base_stat till every stat has be added to baseStats and then adds them together

        english_entries = [entry["flavor_text"] for entry in dexData["flavor_text_entries"] if entry["language"]["name"] == "en"] #finds the first pokedex entry for the entered pokemon
        return(f"{english_entries[0].capitalize()}\nand its base stat total is {baseStatTotal}\n")

    else:
        return("Pokemon could not be found.\n")


def Store_Pokemon(pokemon):
    """
        stores entered pokemon along with their relevant information
        Arg:
            pokemon (str): name of pokemon user want to add to their team

        returns:
            str: A message that tells the player that the desired pokemon has been added to the team if it exists.

        aditionally, the entered pokemon is saved in a json file for later use.
    """

    pokemonTeam = {}
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

    response = requests.get(f"{pokeAPI}{pokemon.lower()}") #makes a request to the api using the pokemons name
    if response.status_code == 200: #Checks if the entered pokemon is in the api
        data = response.json() #turns the made request into a readable json file

        counter = len(pokemonTeam)
        if counter < 6: #ensures the user has less than 6 pokemon
            pokemonTeam[pokemon] = {
                "moves": {},
                "bst": {"hp": data["stats"][0]["base_stat"],
                        "atk": data["stats"][1]["base_stat"],
                        "sp.atk": data["stats"][3]["base_stat"],
                        "def": data["stats"][2]["base_stat"],
                        "sp.def": data["stats"][4]["base_stat"],
                        "spd": data["stats"][5]["base_stat"]}
                        #assigns the values for base stats from the api to the pokemon
            }
            jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

            with open("pokemonTeam.json", "w") as outfile:
                outfile.write(jsonTeam) #saves the new pokemon to the json file
            return(pokemon.capitalize() + " has been added to party!\n")  

        else:
            return("You already have 6 pokemon, remove one before you try to add another.\n")
    else:
        return("Pokemon could not be found.\n")


def Check_Pokemon(pokemonAndData):
    """
        determines which kind of data the user wants to retrieve from the api and then displays it to the user
        args:
            pokemon (str): the name of the pokemon the user wants info about + the type of information the user wants
       
        returns:
            (str): the information the user requested about the pokemon
    """
    try:
        pokemon, datatype = pokemonAndData.split(' ', 1)
    except:
        return("Please fill both fields.\n")
    #ensures that the user gives both inputs

    response = requests.get(f"{pokeAPI}{pokemon.lower()}") #makes a request to the api using the pokemons name
    if response.status_code == 200:
        data = response.json()

        if "moveset" in datatype:
            for move_data in data['moves']:
                print(f"{move_data['move']['name']}\n")
            return f"That is every move that {pokemon.capitalize()} learns\n"

        elif "evolution line" in datatype:
            pokemonId = data["species"]["url"]

            dexResponse = requests.get(f"{pokemonId}")
            dexData = dexResponse.json()

            evolutionId = dexData["evolution_chain"]["url"]
            evolutionResponse = requests.get(f"{evolutionId}")
            evolutionData = evolutionResponse.json()

            evolutionChain = []
            currentEvo = evolutionData["chain"]
            queue = [currentEvo]

            while queue:
                evoStage = queue.pop(0)
                evolutionChain.append(evoStage["species"]["name"])

                for nextEvo in evoStage["evolves_to"]:
                    queue.append(nextEvo)


            return "This is the evolution line of " + pokemon.capitalize() + ":\n" + '\n'.join(evolutionChain) + "\n"
       
        elif "bst" in datatype:
            return f"This is the base stat total distribution of {pokemon}: hp: {data['stats'][0]['base_stat']}, atk: {data['stats'][1]['base_stat']}, sp.atk: {data['stats'][3]['base_stat']}, def: {data['stats'][2]['base_stat']}, sp.def: {data['stats'][4]['base_stat']}, spd: {data['stats'][5]['base_stat']}." + "\n"

        elif "moveset" in datatype:
            for move_data in data['moves']:
                print(move_data['move']['name'])
            return f"That is every move that {pokemon} learns"

        elif "type" in datatype:
            types = [t["type"]["name"] for t in data["types"]]
            return f"{pokemon.capitalize()} is: {', '.join(types)}." + "\n"
       
        else:
            return "Invalid datatype.\n"
    else:
        return "Pokemon does not exist.\n"

        #barry: needs GUI, good format for a text ui, efficient to use if you know what you're doing
        #William: The program is extremely efficent and effective at responding TO THE USERS INPUT AND RETIREVing the API information however the program could benefit from the introuction of a GUI to allow the user to more easily navigate the project.


def View_Team():
    pokemonTeam = {}
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam
   
        print("Your current team is:")
        for key in pokemonTeam:
            print(key) #displays the name of pokemon in the users party
        return("\n")
    else:
        return("You don't have a team.\n")


def Remove_Pokemon(pokemon):
    pokemonTeam = {}
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

        if pokemon in pokemonTeam:
            del pokemonTeam[pokemon]
       
        else:
            return(pokemon.capitalize() + " is not in your party!\n")

        jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

        with open("pokemonTeam.json", "w") as outfile:
            outfile.write(jsonTeam) #saves the new pokemon to the json file

        return(pokemon.capitalize() + " has been removed from party!\n")
    
    else:
        return("You don't have a team.\n")


def Give_Move(pokemonAndMove):
    try:
        pokemon, move = pokemonAndMove.split(' ', 1)
    except:
        return("Please fill both fields.\n")
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

    if pokemon in pokemonTeam: #checks if the entered pokemon is in the users team
        response = requests.get(f"{pokeAPI}{pokemon.lower()}") #makes a request to the api using the pokemons name.
        if response.status_code == 200:
            data = response.json() #converts the api webpage to a readable json file
            canLearnMove = False

            for move_data in data['moves']:
                if move_data['move']['name'] == move.lower():
                    canLearnMove = True
            #checks if the entered move can be found in the api and if it is found then the pokemon can learn that move

            if canLearnMove:
                counter = len(pokemonTeam[pokemon]["moves"]) #checks how many moves the pokemon has to ensure that the pokemon doesn't learn more than 4 moves
                if counter < 4:
                    pokemonTeam[pokemon]["moves"][move] = move

                    jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

                    with open("pokemonTeam.json", "w") as outfile:
                        outfile.write(jsonTeam) #saves the new pokemon to the json file

                    return (f"{pokemon.capitalize()}  was given {move}." + "\n")
               
                else:
                    return(pokemon.capitalize() + " aleady has 4 moves\n")
            else:
                return(pokemon.capitalize() + " cannot learn that move\n")
        else:
            return("Could not connect to api\n")
    else:
        return("You do not have that pokemon in your team.\n")


def remove_Move(pokemonAndMove):
    try:
        move, pokemon = pokemonAndMove.split(' from ', 1)
    except:
        return("Please fill both fields.\n")
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam
           
        if pokemon in pokemonTeam:
            if move in pokemonTeam[pokemon]["moves"]:
                del pokemonTeam[pokemon]["moves"][move]
       
            elif move not in pokemonTeam[pokemon]["moves"]:
                return(pokemon.capitalize() + " does not have that move.\n")
            
            else:
                return("Invalid input")
        else:
            return(pokemon.capitalize() + " isn't in your party.\n")

        jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

        with open("pokemonTeam.json", "w") as outfile:
            outfile.write(jsonTeam) #saves the new pokemon to the json file

        return(move + " has been removed from " + pokemon.capitalize() + "!\n")
   
    else:
        return("You don't have a team.\n")
    

def Challenge():
    return("Coming soon...\n")


def help():
    """ Exists to explain how the system works to first time users """
   
    return """The pokedex works based off of keywords followed by the name of a pokemon or other form of information.
          The key words are:
          search (pokemon) - Returns information about the entered pokemon if it exists.
          store (pokemon) - Adds the entered pokemon to your team. You CANNOT store multiple of the same pokemon.
          check (pokemon) (type of data) - Checks specific information for a pokemon.
          your options for "check" are:
            moveset
            evolution line
            bst
            type
          view team - Displays the pokemon in your party.
          remove (pokemon) - Removes entered pokemon from your team.
          give move (move) (pokemon) - Gives your pokemon the entered move if they are compattible. NOTE spaces in moves are replaced with "-" so for example the move fire punch is now fire-punch.
          challenge - Challenges the elite four and turns the pokedex into a battle simulator. NOTE not implemented currently, will work in a future update.
          end - quits the program\n
          """