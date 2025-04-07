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

    print("If you require instructions try typing 'help' ")


def Search_Pokemon(pokemon):
    response = requests.get(f"{pokeAPI}{pokemon.lower()}")
    if response.status_code == 200:
        data = response.json()
        pokemonId = data["species"]["url"]

        dexResponse = requests.get(f"{pokemonId}")
        dexData = dexResponse.json()
        
        baseStats = [baseStat["base_stat"] for baseStat in data["stats"]]
        baseStatTotal = sum(baseStats)

        english_entries = [entry["flavor_text"] for entry in dexData["flavor_text_entries"] if entry["language"]["name"] == "en"]
        return(f"{english_entries[0]}\nand its base stat total is {baseStatTotal}")

    else:
        return("pokemon could not be found")

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

    response = requests.get(f"{pokeAPI}{pokemon.lower()}")
    if response.status_code == 200:
        data = response.json()

        counter = len(pokemonTeam)
        if counter < 6: #ensures the user has less than 6 pokemon
            pokemonTeam[pokemon] = {
                "moves": {},
                "bst": {"hp": data["stats"][0]["base_stat"], "atk": data["stats"][1]["base_stat"], "sp.atk": data["stats"][3]["base_stat"], "def": data["stats"][2]["base_stat"], "sp.def": data["stats"][4]["base_stat"], "spd": data["stats"][5]["base_stat"]}

            } #assigns first four learnt moves and base stat total from the api
            jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

            with open("pokemonTeam.json", "w") as outfile:
                outfile.write(jsonTeam) #saves the new pokemon to the json file
            return(pokemon + " has been added to party!")  

        else:
            return("you already have 6 pokemon, remove one before you try to add another.")
    else:
        return("pokemon could not be found")


def Check_Pokemon(pokemonAndData):
    """
        determines which kind of data the user wants to retrieve from the api and then displays it to the user
        args:
            pokemon (str): the name of the pokemon the user wants info about + the type of information the user wants
       
        returns:
            (str): the information the user requested about the pokemon
       
    """
    pokemon, datatype = pokemonAndData.split(' ', 1)
    response = requests.get(f"{pokeAPI}{pokemon.lower()}")
    if response.status_code == 200:
        data = response.json()

        if "moveset" in datatype:
            for move_data in data['moves']:
                print(move_data['move']['name'])
            return f"That is every move that {pokemon} learns"

        elif "evolution line" in datatype:
            pokemonId = data["species"]["url"]

            dexResponse = requests.get(f"{pokemonId}")
            dexData = dexResponse.json()
            evolutionId = dexData["evolution_chain"]["url"]
            evolutionResponse = requests.get(f"{evolutionId}")
            evolutionData = evolutionResponse.json()
            evolutionChain = []
            currentEvo = evolutionData["chain"]

            while currentEvo:

                evolutionChain.append(currentEvo["species"]["name"])
                if currentEvo["evolves_to"]:
                    for evo in currentEvo["evolves_to"]:
                        evolutionChain.append(evo["species"]["name"])
                    break
                else:
                    currentEvo = None
            return f"This is the evolution line of {pokemon}: {', '.join(evolutionChain)}"
        

        elif "bst" in datatype:
            return f"This is the base stat total distribution of {pokemon}: hp: {data["stats"][0]["base_stat"]}, atk: {data["stats"][1]["base_stat"]}, sp.atk: {data["stats"][3]["base_stat"]}, def: {data["stats"][2]["base_stat"]}, sp.def: {data["stats"][4]["base_stat"]}, spd: {data["stats"][5]["base_stat"]}."

        elif "type" in datatype:
            types = [t["type"]["name"] for t in data["types"]]
            return f"{pokemon} is: {', '.join(types)}."
        
        else:
            return "unvalid datatype"
    else:
        return "Pokemon does not exist"
    
        #all these if and elif statments esentially do the same thing. They determine the type of data the user was looking for and then display it to the user.
        #barry: needs GUI, needs better format for display a bit confusing
        #miles:

def View_Team():
    pokemonTeam = {}
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam
   
        print("your current team is:")
        for key in pokemonTeam:
            print(key) #displays the name of pokemon in the users party
    else:
        print("you don't have a team.")


def Remove_Pokemon(pokemon):
    pokemonTeam = {}
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

        if pokemon in pokemonTeam:
            del pokemonTeam[pokemon]
       
        else:
            return(pokemon + " is not in your party")

        jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

        with open("pokemonTeam.json", "w") as outfile:
            outfile.write(jsonTeam) #saves the new pokemon to the json file

        return(pokemon + " has been removed from party!")
   
    else:
        return("you don't have a team.")


def Give_Move(pokemonAndMove):
    pokemon, move = pokemonAndMove.split(' ', 1)
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

    if pokemon in pokemonTeam: #checks if the entered pokemon is in the users team
        response = requests.get(f"{pokeAPI}{pokemon.lower()}") #makes a request to the api using the pokemons name.
        if response.status_code == 200: #checks if the request returns a value in the api
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

                    return pokemon + " was given " + move
                
                else:
                    return(pokemon + " aleady has 4 moves")
            else:
                return(pokemon + " cannot learn that move")
        else:
            return("Could not connect to api")
    else:
        return("you do not have that pokemon in your team")


def remove_Move(pokemonAndMove):
    move, pokemon = pokemonAndMove.split(' from ', 1)
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam
           
        if pokemon in pokemonTeam:
            if move in pokemonTeam[pokemon]["moves"]:
                del pokemonTeam[pokemon]["moves"][move]
       
            elif move not in pokemonTeam[pokemon]["moves"]:
                return(pokemon + " does not have that move")
       
            else:
                return("invalid input ")
        else:
            return(pokemon + " isn't in your party")

        jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

        with open("pokemonTeam.json", "w") as outfile:
            outfile.write(jsonTeam) #saves the new pokemon to the json file

        return(move + " has been removed from " + pokemon + "!")
   
    else:
        return("you don't have a team.")
    

#def Challenge():


def help():
    """ Exists to explain how the system works to first time users """
   
    return """the pokedex works based off of keywords followed by the name of a pokemon or other form of information.
          the key words are:
          search (pokemon) - returns information about the entered pokemon if it exists
          store (pokemon) - adds the entered pokemon to your team. You CANNOT store multiple of the same pokemon
          check (pokemon) (type of data) - checks specific information for a pokemon.
          your options for "check" are:
            moveset
            evolution line
            bst
            type
          view team - displays the pokemon in your party
          remove (pokemon) - removes entered pokemon from your team
          give move (move) (pokemon) - gives your pokemon the entered move if they are compattible
          challenge - challenges the elite four and turns the pokedex into a battle simulator. WARNING there is no turning back once you enter the battle simulator until you lose. (there is a different list of commands for the battle sim)
          end - quits the program
          """


