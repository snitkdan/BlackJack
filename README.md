# BlackJack
Welcome to BlackJack! This is me trying to practice core data structures in a fun way. Hopefully, if you come across this, you'll find the result interesting/entertaining. 

## Pre-requisite
Ensure that Python 3.7.0 or higher is installed
* Can be verified by running ```python3.7 --version```. 
* If using anaconda, can ensure this dependency by running ```conda install python=3.7.0```. 

## Playing the Game
Run ```bash -x play.sh``` from the top-level BlackJack folder. 

## Running the Tests
Run ```bash -x test.sh``` from the top-level BlackJack folder. 

## House Rules
This version of BlackJack initially deals 2 cards to all players that are only visible to each player. Hands that are busted are considered more valuable the smaller in value they are, while non-busted hands are valued in increasing order up to and including 21. There can be a maximum of 26 players in a given game. 

## Design Choices
There were 3 main data structures that were used to implement core functionality: a BinaryTree a binary MaxHeap, and a Bitset. 

A BinaryTree was used to represent the possible scores that a player’s hand is worth, where each node is a hand representing a possible score, and each level representing the number of cards in a hand. This choice was made because aces in BlackJack are worth 1 or 11 points, causing a branching factor of 2 for each set of possible scores that would result in a new card being dealt. This not only cleanly represents this branching, but also offers logarithmic time complexity for retrieving leaf nodes (current possible scores), which is the primary operation within this application. 

A binary MaxHeap is used to represent the final rankings of each player. This choice was made because of the Heap property (i.e. children have less priority than their parents), and the time complexity of construction and removing the maximum element. Since the rankings are only necessary at the end of the game, I used Floyd’s Build Heap algorithm to construct the MaxHeap in linear time upon game over, and remove each element in logarithmic time to get the final rankings. This was not only efficient, but led to a clean interface for defining the value of a particular hand, allowing for future extensions with the idea of a “priority”. 

A Bitset was used to represent the current state of the Deck, with each index representing a unique card of the standard 52, where 1 indicates present, and 0 indicates drawn. This choice was made because a standard deck holds 4 suits, and therefore the suit of a card can be derived by assigning each section of the 52 indices to a particular suit. Maintaining the state of which cards were drawn was also a reason for this choice since values of indices that were 1 could be part of the next pool of cards to draw from, and drawing a card becomes a constant time operation. 

