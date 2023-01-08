class Solitare():

    def __init__(self, deck):
        self.deck = deck

    def step_one(self):
        index = self.deck.index(53)
        if index == 53:
            self.deck[0], self.deck[index] = self.deck[index], self.deck[0]
        else:
            self.deck[index], self.deck[index+1] = self.deck[index+1], self.deck[index]

    def step_two(self):
        index = self.deck.index(54)
        self.deck.pop(index)
        if index == 53:
            self.deck.insert(2, 54)
        elif index == 52:
            self.deck.insert(1, 54)
        else:
            self.deck.insert(index + 2, 54)

    def step_three(self):
        index1 = min(self.deck.index(53), self.deck.index(54))
        index2 = max(self.deck.index(53), self.deck.index(54))
        self.deck = self.deck[index2+1:] + self.deck[index1:index2+1] + self.deck[:index1]

    def step_four(self):
        last_card = self.deck[53]
        if last_card != 53 or last_card != 54:
            self.deck =  self.deck[last_card:-1] + self.deck[:last_card] + self.deck[-1:]

    def step_five(self):
        first_card = self.deck[0]
        if first_card == 53 or first_card == 54:
            return None
        return self.deck[first_card]

    def generate_random_number(self):
        done = False
        while done is False:
            self.step_one()
            self.step_two()
            self.step_three()
            self.step_four()
            number = self.step_five()
            if number != None:
                return number
