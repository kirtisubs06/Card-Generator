"""
Assignment 9: "A Playing Card"

Author: Kirti Subramanian
CWID: 20531478
Date: 11/26/2022

Program Description: This program has a class defined from which a playing card object can
be created. If the object's rank and suit is given, then the full name of the card will be
returned in word form.
"""


# This class has methods from which an object (a specific playing card) can be constructed.
# Given the rank and suit of the playing card object, a card can be created as an object
# of the class.
class PlayingCard:
    def __init__(self, rank, suit):
        """
        Constructs an instance of the PlayingCard class given the rank and suit.
        It also initializes a dictionary for the translations.
        :param rank: rank of the card
        :param suit: suit of the card
        """
        self.rank = rank
        self.suit = suit
        self.translations = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                             8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King",
                             "d": "Diamonds", "s": "Spades", "h": "Hearts", "c": "Clubs"}

    def get_rank(self):
        """
        Returns the rank of the card as an integer.
        :return: rank of the card
        """
        # Returns the rank of the card as a number, example 3
        return self.rank

    def get_suit(self):
        """
        Returns the suit of the card as a word after applying translations.
        :return: returns the suit of the card
        """
        return self.translations[self.suit]

    def bj_value(self):
        """
        Returns the blackjack value of the card as an integer.
        :return: the blackjack value of the card
        """
        # Returns the Blackjack value of a card. Ace has a blackjack value of 1,
        # face cards all have blackjack value 10. The rest of the cards have blackjack
        # values that are the same as their rank. The returned value from this method
        # will always be a number.
        return self.rank if self.rank <= 10 else 10

    def __str__(self):
        """
        Returns a string containing the full name of the card.
        :return: full name of card in words
        """
        # Returns a string containing the full name of the card. For example. "Ace of Spades".
        return "{} of {}".format(self.translations[self.rank], self.get_suit())


# test 1
c1 = PlayingCard(5, "c")  # constructs the Card object
print(c1)  # verifies that the Card object got constructed
print(c1.get_rank())  # outputs 5
print(c1.get_suit())  # outputs "Clubs"
print(c1.bj_value())  # outputs 5

"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment9.py 
5 of Clubs
5
Clubs
5

Process finished with exit code 0
"""

# test 2
c2 = PlayingCard(13, "h")  # constructs the Card object
print(c2)  # verifies that the Card object got constructed
print(c2.get_rank())  # outputs 13
print(c2.get_suit())  # outputs "Hearts"
print(c2.bj_value())  # outputs 10

"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment9.py 
King of Hearts
13
Hearts
10

Process finished with exit code 0
"""