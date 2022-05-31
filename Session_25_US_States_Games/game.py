from pandas import Series
from state import State
import pandas

class Game:

    def __init__(self, countries):
        self.country_to_find = countries
        self.found_country = []
        self. score = 0
        self.available_try = 50

    def state_is_found(self, answer):
        if answer in self.country_to_find :
            self.found_country.append(answer)
            self.score += 1
            return True
        return False


    def state_already_found(self, answer):
        return answer in self.found_country

    def end_of_game(self):
        states_to_learn = []
        for state in self.country_to_find :
            if state not in self.found_country :
                states_to_learn.append(state)

        df = pandas.DataFrame(states_to_learn, columns=["States to remember"])
        df.to_csv("states_to_remember.csv")


