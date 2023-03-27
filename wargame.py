from random import shuffle

class Card:
    suits=["spades","hearts","diamonds","clubs"]
    values=[None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self,v,s):
        """suitsとvalueは整数"""
        self.value=v
        self.suit=s
        
    def __lt__(self,c2):
        if self.value<c2.value:
            return True
        elif self.value==c2.value:
            if self.suits<c2.suits:
                return True
            else :
                return False
        else:
            return False
    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        elif self.value==c2.value:
            if self.suits>c2.suits:
                return True
            else :
                return False
        else:
            return False
    def __repr__(self):
        return "{} of {}".format(self.values[self.value],self.suits[self.suit])

class Deck:
    def __init__(self):
        self.card=[]
        for i in range(2,15):
            for j in range(4):
                self.card.append(Card(i,j))
        shuffle(self.card)
    def rm_card(self):
        if len(self.card)==0:
            return
        return self.card.pop()
    
class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        name1=input("Type player1's name")
        name2=input("Type player2's name")
        self.p1=Player(name1)
        self.p2=Player(name2)
        self.deck=Deck()
        
    def wins(self,winner):
        print("このラウンドは{}が勝ちました".format(winner))
        
    def draw(self,p1n,p1c,p2n,p2c):
        print("{} は {} , {} は {} を引きました".format(p1n,p1c,p2n,p2c))

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        elif p1.wins<p2.wins:
            return p2.name
        else:
            return "引き分け"
        
    def play_game(self):
        cards=self.deck.card
        print("戦争を始めます")
        while(len(cards)>=2):
            response=input("qで終了，それ以外のキーでPLAY")
            if response=="q":
                break
            p1c=self.deck.rm_card()#カードをドロー
            p2c=self.deck.rm_card()
            p1n=self.p1.name#これはおそらくループから外すべき
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(p1n)
            else:
                self.p2.wins+=1
                self.wins(p2n)
        win=self.winner(self.p1,self.p2)
        print("ゲーム終了！{}の勝ち".format(win))
g1=Game()
g1.play_game()

