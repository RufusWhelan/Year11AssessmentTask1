def main():
    userinput = ""

    userinput = "" 
    pokemonName = ""
    moveName = ""
    typeOfData = ""
    

    while userinput != "end":
        userinput = input("").lower()
        if userinput.startswith("search "):
            userinput = userinput.replace("search ", "")
            print("here's that pokemon's details!")
            pokemonName = userinput.replace("search ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Search_Pokemon(pokemonName))


        elif userinput.startswith("store "):
            pokemonName = userinput.replace("store ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Store_Pokemon(pokemonName))
        
        elif userinput.startswith("check "):
            pokemonName = userinput.replace("check ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Check_Pokemon(pokemonName))
        
        elif userinput == "view team":
            print(View_Team())

        elif userinput.startswith("remove "):
            pokemonName = userinput.replace("remove ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Remove_Pokemon(pokemonName))
        
        elif userinput.startswith("give "):
            pokemonName = userinput.replace("give ", "")
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
    return "here's" + pokemon + "'s details!"

def Store_Pokemon(pokemon):
    return pokemon + "has been added to party!"

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
    return pokemon + "has been removed from party!"

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




print("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")
print("If you require instructions try typing 'help' ")
main()