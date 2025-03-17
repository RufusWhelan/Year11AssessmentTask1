def main():
    userinput = ""
    while userinput != "end":
        userinput = input("").lower()
        if userinput.startswith("search "):
            userinput = userinput.replace("search ", "")
            print("here's that pokemon's details!")
        else:
            print("invalid input")

print("Hello there! Welcome to the world of pokémon! This world is inhabited by creatures called pokémon! For some people, pokémon are pets. Others use them for fights.")
print("If you require instructions try typing 'help' ")
main()