def main():
    userinput = ""
    pokemonName = ""
    moveName = ""
    while userinput != "end":
        userinput = input("").lower()
        
        if userinput.startswith("search "):
            pokemonName = userinput.replace("search ", "")
            print("here's " + pokemonName + "'s, details!")
            Search_Pokemon()

        elif userinput.startswith("store "):
            pokemonName = userinput.replace("store  ", "")
            print(pokemonName + " has been added to party!")
            Store_Pokemon()
        
        elif userinput == "view team":
            print("viewing team")
            Check_Pokemon()
        
        elif userinput.startswith("remove "):
            pokemonName = userinput.replace("remove ", "")
            print( pokemonName + " has been removed from party!")
            Remove_Pokemon()
        elif userinput.startswith("give move "):
            pokemonName = userinput.replace("give move", '')
   
        elif userinput == "end":
            print("Goodbye")

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

print("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")
print("If you require instructions try typing 'help' ")
main()