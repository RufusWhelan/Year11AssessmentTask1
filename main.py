import json
import os

def main():
    userinput = ""
    pokemonName = ""
    moveName = ""
    typeOfData = ""
    team = {}
    pokemonInTeam = 0
    
    start()
    while userinput != "end":
        userinput = input("").lower()
        if userinput.startswith("search "):
            pokemonName = userinput.replace("search ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Search_Pokemon(pokemonName))

        elif userinput.startswith("store "):
            pokemonName = userinput.replace("store ", "") #removes the key term used so that the name of the pokemon can be found by the api
            team, pokemonInTeam = Store_Pokemon(pokemonName, team)
            print(team)
            print(pokemonInTeam)

        elif userinput.startswith("check "):
            pokemonName = userinput.replace("check ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Check_Pokemon(pokemonName))
        
        elif userinput == "view team":
            print(View_Team())

        elif userinput.startswith("remove "):
            pokemonName = userinput.replace("remove ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Remove_Pokemon(pokemonName))
        
        elif userinput.startswith("give "):
            pokemonName = userinput.replace("give ", "") #removes the key term used so that the name of the pokemon can be found by the api
            #will add function once api is implemented
        
        elif userinput == "challenge":
            print("Goodluck")
            #will implement once rest of project is complete

        elif userinput == "help":
            print(help())

        elif userinput == "end":
            print("goodbye")

        else:
            print("invalid input")


def Search_Pokemon(pokemon):
    return "here's " + pokemon + "'s details!"

def Store_Pokemon(pokemon, pokemonTeam):
    if os.path.exists("pokemonTeam.json") and os.path.getsize("pokemonTeam.json") > 0:
        with open("pokemonTeam.json", "r") as openfile:
            pokemonTeam = json.load(openfile)
    counter = len(pokemonTeam)
    if counter < 6:
        pokemonTeam[pokemon] = {
            "moves": {"move1": "", "move2": "", "move3": "", "move4": ""},
            "bst": {"hp": 0, "atk": 0, "sp.atk": 0, "def": 0, "sp.def": 0, "spd": 0},
        }
        counter += 1
    else:
        print("you already have 6 pokemon, remove one before you try to add another.")
    jsonTeam = json.dumps(pokemonTeam)

    with open("pokemonTeam.json", "w") as outfile:
        outfile.write(jsonTeam)
    return (pokemonTeam, counter)   

def Check_Pokemon(pokemon):

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

    #determines which kind of data the user wants to retrieve from the database
    
    else:
        return "invalid input"


def View_Team():
    return "This is your team" 

def Remove_Pokemon(pokemon):
    return pokemon + " has been removed from party!"

#def Give_Move(pokemon):

#def Challenge():

def help():
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
          challenge - challenges the elite four and turns the pokedex into a battle simulator. WARNING there is no turning back once you enter the battle simulator until you lose.
          end - quits the program
          """

def start():
    try:
        open("pokemonTeam.json", "x")
        print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")
    except:
        if os.path.getsize("pokemonTeam.json") > 0:
            restart = input("It appears that you already have a registered team. would you like to restart? ('yes' to clear memory, 'no' to continue with previous team): ").lower()

            if restart == "yes":
                open("pokemonTeam.json", "w").close()
                print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")

            elif restart == "no":
                print("welcome back young traveler")
                
            else:
                print("invalid input")
        else:
            print ("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")

    print("If you require instructions try typing 'help' ")
main()