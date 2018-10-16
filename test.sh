{
# File Paths
SRC_PATH=src
DECK=$SRC_PATH/Deck.py
DECK2=$SRC_PATH/Deck2.py
HAND=$SRC_PATH/Hand.py
HAND2=$SRC_PATH/Hand2.py
GAME=$SRC_PATH/Game.py
GAME2=$SRC_PATH/Game2.py

# Prep Deck
sed 's/from Card/from src.Card/g' < $DECK > $DECK2 && mv $DECK2 $DECK
# Prep Hand
sed 's/from Card/from src.Card/g' < $HAND > $HAND2 && mv $HAND2 $HAND
sed 's/from BinaryTree/from src.BinaryTree/g' < $HAND > $HAND2 && mv $HAND2 $HAND
# Prep Game
sed 's/from Hand/from src.Hand/g' < $GAME > $GAME2 && mv $GAME2 $GAME
sed 's/from Deck/from src.Deck/g' < $GAME > $GAME2 && mv $GAME2 $GAME
sed 's/from MaxHeap/from src.MaxHeap/g' < $GAME > $GAME2 && mv $GAME2 $GAME
} &> /dev/null

# Run unit tests
python3.7 -m unittest discover

{
# Undo Deck
sed 's/from src.Card/from Card/g' < $DECK > $DECK2 && mv $DECK2 $DECK
# Undo Hand
sed 's/from src.Card/from Card/g' < $HAND > $HAND2 && mv $HAND2 $HAND
sed 's/from src.BinaryTree/from BinaryTree/g' < $HAND > $HAND2 && mv $HAND2 $HAND
# Prep Game
sed 's/from src.Hand/from Hand/g' < $GAME > $GAME2 && mv $GAME2 $GAME
sed 's/from src.Deck/from Deck/g' < $GAME > $GAME2 && mv $GAME2 $GAME
sed 's/from src.MaxHeap/from MaxHeap/g' < $GAME > $GAME2 && mv $GAME2 $GAME
} &> /dev/null