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

