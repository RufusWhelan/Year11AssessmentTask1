# Pokedex
## Requirements Definition
### Functional Requirements
* User can search for a pokemon and have its base stat total and a pokedex entry displayed to them.
* User can add a pokemon to their team if they have less than 6 pokemon on their team.
* Users Team is stored in a json file
* User can remove a pokemon from their team
* User can view their team
* User can add moves learnt by level up or tm to their pokemon
* User can challenge pokemon platinum elite four with their current team, all user and enemy pokemon will be level 50. In combat users can select moves and deal damage or place effects on enemy pokemon accordingly.

### Non-functional Requirements
* System should proccess user input within 3 seconds. If it fails to do this, the system should return an error.
* System should account for capitalisation of letters
* System should always return a searched pokemon that user requests. If it can't be found the system should return an error.
* User should have access to a help function to gain details on how the system works.
* clear options for user should be layed out.

## Determining Specifications

### Functional Specifications
#### __Inputs and Outputs__
* User can input a string. If the the string matches the name of a pokemon, it should return its relevant information.
* User can use the 'add' command followed by a pokemon name. The system should then store that pokemon and its relevant information in a json file.
* User can use the 'remove' command followed by a pokemon name. If the pokemon is currently on the users team the system should remove it from the json file.
* User can use the 'give' command followed by a pokemon and move name name. If the pokemon is currently on the users team and the move exists, the system should add the move to the the pokemons move dictionary in the json file.
* User can use the 'remove from' command followed by a pokemon name and move name. If the pokemon is currently on the users team with the entered move, it should be removed from the json file.
* User can use the 'check' command followed by a pokemon name and type of data. If the pokemon is in the api, the relevant information should be returned.
* User can use the 'challenge' command to challenge the elite four. The system should then take the pokemon inside the users team and simulate a battle.
* In battle, User can select moves available to their pokemon or swap out. The system should be able to take these inputs and make relevant changes or calculations for the battle.

#### __Core Features__
* System needs to be able to search through pokeapi for relevant information
* System needs to be able to store pokemon and their relevant infomation to a json file
* System needs to be able to remove pokemon and their relevant infomation from a json file
* System needs to be able to simulate a pokemon battle by making relevant calcuations

#### __User Interaction__
* User will interact with the system through command-line inputs.
* User can input key words like 'add' or 'challenge' or input numbers as short hands for commands. e.g 1 is add, 2 is remove, ect.
* User can use a 'help' command to gain instructions on how to use the system.

#### __Error Handling__
* System will return an error message to the user when a spelling mistake is made
* System will return an error message to the user if they try to remove a pokemon from their team when they do not have any pokemon
* System will return an error message to the user if relevant information for the pokemon cannot be found
* System will return an error message to the user if they try to view their team when they do not have any pokemon
* System will return an error message to the user if they try to add a pokemon to their team when they already have 6 pokemon

### Non-functional Specifications
* To maintain user engagement, it is important that the system processes all inputs within 3 seconds. To ensure that the program runs effiently, classes and functions will be used to avoid repeating code.
* To improve useability, simple terms wil be used to allow users to gain a clear and concise understanding of the system.
* A potential problem that could need to be adressed is what happens when multiple of the same pokemon are added to the same team.
* Another potential issue the system could run into is if the api it is attempting to retrieve information is down. This should result in an error explaining that the API is down.

## Use Cases
### Actor:
- User (Pokemon Enthusiast)
### Preconditions: 
- access to the internet and to the pokemon api (Pokeapi)
### Main Flow:
- __Search:__ User enters the name of a pokemon. The system retrieves and displays the bst of and a pokedex entry for the pokemon to the User.
- __Store/'Catch' Pokemon:__ User adds the pokemon to their team of 6 pokemon, system confirms this and stores the pokemon in a json file.
- __View Team:__ User can request to see their team, system shows the user their team.
- __Remove/'release' Pokemon:__ User can remove a pokemon from their team, systems confirms this and changers the json file accordingly.
- __Give Move:__ User can give one their pokemon moves. The system checks if the pokemon can learn that move and if it can, the pokemon is given that move.
- __Remove Move:__ User can remove moves from the pokemon on their teams. The systems checks if the pokemon has the entered move and then removes it if it does.
- __Check:__ User can get indepth information on an aspect of a given pokemon. The system processes what type of data the user wants (e.g bst, level up moveset, type and evolution) and displays the relevant information.
- __Challenge:__ User challenges Elite Four with current team. System checks if the user has any pokemon, then transitions to alternate flow.

### Alternate Flow (User Challenges Elite Four)
- __Attacking:__ User can select an attack, relevant effect/damage is calcuated and then applied to opposing pokemon by system.
- __Enememy Turn:__ System selects random move to be used by current enemy pokemon, favouring super effective moves.
- __Effects:__ system applies required effects to every current pokemon at the end of every turn.
- __Switching:__ User can switch between their pokemon on their turn.
- __Fainting:__ When a pokemons hit points reaches zero, it faints and can not be used in battle anymore.
- __Winning:__ when every pokemon is elimated on the user's team, they lose and the user is sent back to Main Flow. When every pokemon on the enemy's team faints, the user wins and the user is moved on to the next battle.

### Postconditions:
- Pokemon data is retrieved, displayed, stored, removed, checked or Elite Four is challenged. A pokemon turn is played out.

## Design
![Ganttchart](/images/Ganttchart.png "Ganttchart")
![structurechart](/images/structurechart.png "structurechart")

### pseudocode
```
BEGIN main()
    choice = ""

    WHILE choice is not "end"
        INPUT choice
        IF API request valid THEN
            If choice begins with "search" THEN
                Search_Pokemon
            ELSEIF choice begins with "store" THEN
                Store_Pokemon 
            ELSEIF choice begins with "check" THEN
                Check_Pokemon
            ELSEIF choice is "view team" THEN
                View_Team
            ELSEIF choice begins with "remove" THEN
                Remove_Pokemon
            ELSFIF choice begins with "give" THEN
                Give_Move
            ELSFIF choice begins with "remove" AND contains "from" THEN
                Give_Move
            ELSEIF choice is challenge THEN
                Challenge_  
            ENDIF
        ELSE DISPLAY "Error connecting to API"
        ENDIF
END main()

BEGIN Search_Pokemon(searchedPokemon)
    IF searchedPokemon is found in API THEN
        DISPLAY searchedPokemon's bst and a pokedex entry for the pokemon
    ELSE
        DISPLAY "pokemon could not be found"        

END Search_Pokemon()

BEGIN View_Team()
    READ Team.json
    DISPLAY  pokemon in team

END View_Team()
```
![mainFlowchart](/images/mainFlowchart.png "mainFlowchart")
![viewTeamFlowchart](/images/viewTeamFlowchart.png "viewTeamFlowchart")
![searchPokemonFlowchart](/images/searchPokemonFlowchart.png "searchPokemonFlowchart")

## Data Dictionary:
|Variable|Data Type|Format for Display|Size in Bytes|Size for Display|Description|Example|Validation|
|---|---|---|---|---|---|---|---|
|name|string|text|12|12|the name of the pokemon|charmander|must be a non empty string|
|move|string|text|27|27|the name of the move on the pokemon|fire-punch|must be a non empty string with dashes(-) instead of spaces|
|hp|integer|whole number|6|3|the hit points stat of the entered pokemon|39|must be a whole number|
|atk|integer|whole number|6|3|the atack stat of the entered pokemon|52|must be a whole number|
|sp.atk|integer|whole number|6|3|the special attack stat of the entered pokemon|60|must be a whole number|
|def|integer|whole number|6|3|the defense stat of the entered pokemon|43|must be a whole number|
|sp.def|integer|whole number|6|3|the special defense stat of the entered pokemon|50|must be a whole number|
|spd|integer|whole number|6|3|the speed stat of the entered pokemon|65|must be a whole number|

## Installation
### README
``` 
# Pokedex
    This program allows you to retrieve information from the pokeapi such as pokedex entries, movesets, types, evolution lines and the base stat totals of pokemon. Additionally, you add pokemon to your party. From here you can give them moves.

## Features:
- Fetch information reguarding an entered pokemon
- store and remove pokemon from your team
- add and remove moves to your pokemon
- Check an array of things reguarding an entered pokemon

## Requirments
To run this program you need requests so that HTTP requests can be made to the pokeapi. (all other modules used come with python)

### Installing
To install requests you can run:
pip install -r requirements.txt
```
### requirements
```
requests
```
## Maintenance
1. If issues occured as a result of changes in the Pokeapi over time, I would update the program accordingly to account for improvements in the api. Due how the system has been developed, it is unlikely that the addition of new pokemon or moves would result in bugs, however if the system were to change how it handled the syntax of moves and or pokemon, changes would need to be made in how the system makes requests. for example if they changed from using dashes '-' to using underscores '_' it would be necessary to update the help instructions to the player because, attempting to input names or moves into the system the old way would no longer work. Errors could also occur if the api were to drastically change how data reguarding individual pokemon is stored. Currently, pokedex entries for a given pokemon are stored in a seperate "species" directory, if this were to be removed and these values stored somewhere else instead, what URL's the system uses for the search and check functions would need to change to prevent the system from crashing or giving an incorrect output when these functions are used.
2. To ensure that system continues to work with future versions of python, json, os and requests, routine upgrade testing will be completed. Every 3-4 months I would upgrade to the latest version of python and the affermentionned libraries and then test the entire system, noting any errors that occur. If any errors occur I would make relevant changes to the code so that the system functions correctly on the latest sofware.
3. If a bug was discovered in the program after its deployment, I would methodically debug my code to determine what was causing the bug, and how to fix it.  I would analyse the bug to determine what function resulted in the error and what kind of error it was (runtime, syntax or logical) then I would use the vs code debugger to analyse short blocks of code within the function. Once an error occured I would attempt to determine why it has happened and then implement a solution before pushing the fixed program to github.
4. in the future I would continue to use the waterfall method to ensure that new changes are built from the ground up and implemented overtime, additionally I would continue to make regular github updates to keep a log of all changes made to the project.

## Final Evaluation
1. For the most part, the current program adresses the functional and non functional requirements successfully. All but one of the originally planned functions was implemented and 6 of the 7 functional requirements are met and overall the system functions as intended. However, the one function that was not implemented was the challenge function, which built on the outputs given from several of the other functions with the program. The challenge was to use the json file that was filled by the store and give functions. Since the challenge function was never implemented, several of the values stored through the use of these functions are useless and the give move function is almost entirely redundant. This means, that despite the project living up to majority of its requirments, it lacks its most useful feature and some of the features that do exist are less important.
2. In the future, I would implement the challenge function, and add a GUI. In its current state, the program despite having some features, lacks the gameplay I had intended the system to have. Implementing the challenge function would remedy this and turn the system into what it was originally meant to be. Addtionally, implementing a GUI would improve the user experience drastically and allow for the challenge function to use actual pokemon sprites to communicate to the user more concisely during battle.
3. For most part, this projects development was successfull managed. I used time given for assessment in class effectivly to complete large amounts of my program at school. If at any point I felt that I was behind, I would work on the project from home until I felt that it was at the point it should be at. If at any point I ran into a problem that I did not have a solution for, I would research online until I found a method that suited my program. Aditionally, I had some troubles during the design phase due to a lack of understanding of alglorithms and data dictionaries. I remedied this by looking back through available resources on the gitbook provided by Mr Scott.