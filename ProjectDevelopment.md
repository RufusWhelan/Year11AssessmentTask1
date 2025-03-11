# Pokedex
## Requirements Definition
### Functional Requirements
* User can search for a pokemon and have its base stat total, generation introduced, games it's available in and location found in its native region displayed
* User can add a searched pokemon to their team if they have less than 6 pokemon on their team.
* Users Team is stored in a csv file
* User can remove a pokemon from their team
* User can view their team
* User can add moves learnt by level up or tm to their pokemon, if user doesn't add any moves to their pokemon, then highest level moves it can learn will be selected.
* User can challenge pokemon platinum elite four with their current team, all user and enemy pokemon will be level 50.
* In combat users can select moves and deal damage or place effects on enemy pokemon accordingly.

### Non-functional Requirements
* System should proccess user input within 3 seconds. If it fails to do this, the system should return an error.
* System should account for capitalisation of letters
* System should always return a searched pokemon that user requests. If it can't be found the system should return an error.
* User should have access to a /help function to gain details on how the system works.
* clear options for user should be layed out.

## Determining Specifications

### Functional Specifications
#### __Inputs and Outputs__
* User can input a string. If the the string matches the name of a pokemon, it should return its relevant information.
* User can use the 'add' command followed by a pokemon name. The system should then store that pokemon and its relevant information in a csv file.
* User can use the 'remove' command followed by a pokemon name. If the pokemon is currently on the users team the system should remove it from the csv file
* User can use the 'challenge' command to challenge the elite four. The system should then take the pokemon inside the users team and simulate a battle.
* In battle, User can select moves available to their pokemon or swap out. The system should be able to take these inputs and make relevant changes or calculations for the battle.

#### __Core Features__
* System needs to be able to search through pokeapi for relevant information
* System needs to be able to store pokemon and their relevant infomation to a csv file
* System needs to be able to remove pokemon and their relevant infomation from a csv file
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
- __Search:__ User enters the name of a pokemon. The system retrieves and displays its relevant information to the User. (e.g bst, ability, generation introduced, ect)
- __Store/'Catch' Pokemon:__ User adds the pokemon to their team of 6 pokemon, system confirms this and stores the pokemon in a csv file.
- __View Team:__ User can request to see their team, system shows the user their team.
- __Remove/'release' Pokemon:__ User can remove a pokemon from their team, systems confirms this and changers the csv file accordingly.
- __Give Move:__ User can give one  their pokemon moves. The system checks if the pokemon can learn that move and if it can, the pokemon is given that move.
- __Check:__ User can get indepth information on an aspect of a given pokemon. (e.g Pokedex entries, level up moveset, ect)
- __Challenge:__ User challenges Elite Four with current team.

### Alternate Flow (User Challenges Elite Four)
- __Attacking:__ User can select an attack, relevant effect/damage is calcuated and then  applied to opposing pokemon by system.
- __Enememy Turn:__ System selects random move to be used by current enemy pokemon, favouring super effective moves.
- __Switching:__ User can switch between their pokemon on their turn.
- __Fainting:__ When a pokemons hit points reaches zero, it faints and can not be used in battle anymore
- __Winning:__ when every pokemon is elimated on the user's team, they lose and the user is sent back to Main Flow. When every pokemon on the enemy's team faints, the user wins and the user is moved on to the next battle.

### Postconditions:
- Pokemon data is retrieved, displayed, stored, removed, checked or Elite Four is challenged. A pokemon turn is played out.
https://excalidraw.com/#json=90QKvBRjubT5rLg3aJ884,EOLLJiyodVGkBlCUBxIPTQ