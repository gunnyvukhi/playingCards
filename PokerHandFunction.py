def findPokerHand(hand):
    ranks = []
    suits = []
    possibleRanks = []
 
    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11
        ranks.append(int(rank))
        suits.append(suit)
 
    sortedRanks = sorted(ranks)
 
    # Royal Flush and Flush
    if suits.count(suits[0]) == 5: # Check for Flush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks \
                and 10 in sortedRanks:
            possibleRanks.append(10)
        else:
            possibleRanks.append(6) # -- Flush
 
    # Straight
    Straight = 0
    for i in range(1, len(sortedRanks)):
        if sortedRanks[i] == sortedRanks[i - 1] + 1:
            Straight += 1
            if Straight == 4:
                possibleRanks.append(5)
                if (6 in possibleRanks):
                    possibleRanks.append(9)  # -- Straight Flush
                break
        else:
            Straight = 0
 
    handUniqueVals = list(set(sortedRanks))
 
    # Four of a kind and Full House
    for val in handUniqueVals:
        if sortedRanks.count(val) == 4:  # --- Four of a kind
            possibleRanks.append(8)
        elif sortedRanks.count(val) == 3:  # --- three of a kind
            possibleRanks.append(4)
            if 2 in possibleRanks:
                possibleRanks.append(7)  # -- Full House
        elif sortedRanks.count(val) == 2: # -- Pair
            if 2 in possibleRanks:
                possibleRanks.append(3)  # -- Two Pair
            if 4 in possibleRanks:
                possibleRanks.append(7)  # -- Full House
            else:
                possibleRanks.append(2)
 
    if not possibleRanks:
        possibleRanks.append(1)
    # print(possibleRanks)
    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
    output = pokerHandRanks[max(possibleRanks)]
    return output
 
 
if __name__ == "__main__":
    print(findPokerHand(["KH", "AH", "QH", "JH", "10H"]))  # Royal Flush
    print(findPokerHand(["QC", "JC", "10C", "9C", "8C"]))  # Straight Flush
    print(findPokerHand(["5C", "5S", "5H", "5D", "QH"]) ) # Four of a Kind
    print(findPokerHand(["2H", "2D", "2S", "10H", "10C"]))  # Full House
    print(findPokerHand(["2D", "KD", "7D", "6D", "5D"]) ) # Flush
    print(findPokerHand(["JC", "10H", "9C", "8C", "7D"]))  # Straight
    print(findPokerHand(["10H", "10C", "10D", "2D", "5S"]))  # Three of a Kind
    print(findPokerHand(["KD", "KH", "5C", "5S", "6D"]) ) # Two Pair
    print(findPokerHand(["2D", "2S", "9C", "KD", "10C"]))  # Pair
    print(findPokerHand(["KD", "5H", "2D", "10C", "JH"]))  # High Card