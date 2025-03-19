def main():
    userinput = "" 
    pokemonName = ""
    moveName = ""
    typeOfData = ""

    while userinput != "end":
        userinput = input("").lower()
        
        if userinput.startswith("search "):
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

        elif userinput == "end":
            print("goodbye")

        else:
            print("invalid input")  

def Search_Pokemon():
    return

def Store_Pokemon():
    return

def Check_Pokemon():
    return  

def View_Team():
    return

def Remove_Pokemon():
    return

def Give_Move():
    return

def Challenge_():
    return

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

#$def Give_Move():

#def Challenge():

#def help():




print("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")
print("If you require instructions try typing 'help' ")
main()