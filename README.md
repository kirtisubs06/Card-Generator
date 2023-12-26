# Playing Card Class

## Overview
This Python program defines a `PlayingCard` class which can be used to create objects representing standard playing cards. It includes functionality to return a card's rank, suit, and blackjack value.

### Author
- **Author:** Kirti Subramanian
- **CWID:** 20531478
- **Date:** 11/26/2022

## Description
The `PlayingCard` class allows the creation of playing card objects by specifying their rank and suit. It includes methods to get the card's rank and suit, calculate its blackjack value, and to return a string representation of the card.

## Features
- **Rank and Suit:** Initialize a playing card with a specific rank and suit.
- **Get Rank:** Returns the rank of the card.
- **Get Suit:** Translates the suit's abbreviation to its full word form and returns it.
- **Blackjack Value:** Calculates and returns the blackjack value of the card.
- **String Representation:** Provides a string representation of the card in the format "Rank of Suit".

## Usage
### Creating a Playing Card
```python
c1 = PlayingCard(5, "c")
