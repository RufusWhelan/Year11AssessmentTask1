from pokedex import *


def main():
    userinput = ""
    pokemonName = ""
   
    start()
    while userinput != "end":
        userinput = input("input: ").lower()
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

        elif userinput.startswith("remove ") and "from" not in userinput:
            pokemonName = userinput.replace("remove ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Remove_Pokemon(pokemonName))
       
        elif userinput.startswith("give "):
            pokemonName = userinput.replace("give ", "") #removes the key term used so that the name of the pokemon can be found by the api
            print(Give_Move(pokemonName))
       
        elif userinput.startswith("remove ")  and "from" in userinput:
            pokemonName = userinput.replace ("remove ", "")
            print(remove_Move(pokemonName))
       
        elif userinput == "challenge":
            print("Goodluck")
            #will implement once rest of project is complete

        elif userinput == "help":
            print(help())

        elif userinput == "end":
            print("goodbye")

        else:
            print("invalid input\n")

main()