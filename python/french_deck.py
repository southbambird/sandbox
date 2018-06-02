import collections

Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    beer_card = Card('7','diamonds')
#    print(beer_card)
    
    deck = FrenchDeck()
#    print(len(deck))
#    print(deck[0])
#    print(deck[-1])

    # choiceメソッドは、__getitem__と__len__を利用しているため、
    # この2つが実装されていれば利用できる
    # →豊富な標準ライブラリが利用できる
    from random import choice
    choice(deck)

    # __getitem__を実装しているので、スライスが可能
#    print(deck[:3])
#    print(deck[12::13])


    # __getitem__を実装しているため、for文による走査が可能
    for card in deck:
        card
    for card in reversed(deck):
        card


    # __getitem__を実装してイテラブルオブジェクトになっているため
    # in演算子にも対応可能
#    print(Card('Q', 'hearts') in deck)
#    print(Card('7', 'beasts') in deck)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
        
    for card in sorted(deck, key=spades_high):
        print(card)
