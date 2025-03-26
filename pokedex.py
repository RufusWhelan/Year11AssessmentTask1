import json
import os

def start():
    """
        only runs once to determine whether or not there are already pokemon in the users party and to allow the user to reset
    
    """
    try:
        open("pokemonTeam.json", "x") #attempts to create pokemon.json file
        print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.") #since the file does not exist, it is assumed that the user has not interacted with the system before

    
    except:
        if os.path.getsize("pokemonTeam.json") > 0: #checks if the json file contains anything
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
    return "here's " + pokemon + "'s details!"

def Store_Pokemon(pokemon, pokemonTeam):
    """
        stores entered pokemon along with their relevant information 
        Arg:
            pokemon (str): name of pokemon user want to add to their team

        returns: 
            str: A message that tells the player that the desired pokemon has been added to the team if it exists.

        aditionally, the entered pokemon is saved in a json file for later use.
    """
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0: #checks if pokemonTeam.json exists and isn't empty
        with open("pokemonTeam.json", "r") as openfile: 
            pokemonTeam = json.load(openfile)  # assigns the dictionary in pokemonTeam.json to the variable pokemonTeam

    counter = len(pokemonTeam)

    if counter < 6: #ensures the user has less than 6 pokemon
        pokemonTeam[pokemon] = {
            "moves": {"move1": "", "move2": "", "move3": "", "move4": ""},
            "bst": {"hp": 0, "atk": 0, "sp.atk": 0, "def": 0, "sp.def": 0, "spd": 0},
        } #assigns first four learnt moves and base stat total from the api 

        counter += 1
    else:
        print("you already have 6 pokemon, remove one before you try to add another.")

    jsonTeam = json.dumps(pokemonTeam) #establishes a variable that json can read

    with open("pokemonTeam.json", "w") as outfile:
        outfile.write(jsonTeam) #saves the new pokemon to the json file 
    return (pokemonTeam, counter)   

def Check_Pokemon(pokemon):
    """
        determines which kind of data the user wants to retrieve from the api and then displays it to the user
        args:
            pokemon (str): the name of the pokemon the user wants info about + the type of information the user wants
        
        returns:
            (str): the information the user requested about the pokemon
        
    """

    if " level up moveset" in pokemon:
        pokemon = pokemon.replace(" level up moveset", "")
        return "this is the level up moveset of " + pokemon
    
    elif " evolution line" in pokemon:
        pokemon = pokemon.replace(" evolution line", "")
        return "this is the evolution line of " + pokemon
    
    elif " bst distribution" in pokemon:
        pokemon = pokemon.replace(" bst distribution", "")
        return "this is the base stat total distribution of " + pokemon
    
    elif " type" in pokemon:
        pokemon = pokemon.replace(" type", "")
        return "this is the type of " + pokemon
    
    #all these if and elif statments esentially do the same thing. They determine the type of data the user was looking for and then display it to the user.
    
    else:
        return "invalid input"


def View_Team():
    return "This is your team" 

def Remove_Pokemon(pokemon):
    return pokemon + " has been removed from party!"

#def Give_Move(pokemon):

#def Challenge():

def help():
    """ Exists to explain how the system works to first time users """
    
    return """the pokedex works based off of keywords followed by the name of a pokemon or other form of information.
          the key words are:
          search (pokemon) - returns information about the entered pokemon if it exists
          store (pokemon) - adds the entered pokemon to your team
          check (pokemon) (type of data) - checks specific information for a pokemon. 
          your options for "check" are:
            level up moveset
            evolution line
            bst distribution
            type
          view team - displays the pokemon in your party
          remove (pokemon) - removes entered pokemon from your team
          give move (move) (pokemon) - gives your pokemon the entered move if they are compattible
          challenge - challenges the elite four and turns the pokedex into a battle simulator. WARNING there is no turning back once you enter the battle simulator until you lose. (there is a different list of commands for the battle sim)
          end - quits the program
          """
