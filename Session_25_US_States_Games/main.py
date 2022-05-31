# This is a sample Python script.

from turtle import Turtle, Screen
import state as st
import numpy as np
import pandas
from PIL import Image
from game import Game

# Find the size of the background
map_array = np.array(Image.open("blank_states_img.gif"))
width = map_array.shape[1]
height = map_array.shape[0]

#Create the screen
usa_map = Screen()
usa_map.setup(width=width, height=height)
usa_map.bgpic("blank_states_img.gif")
usa_map.title("U.S. States Game")

#Read the list of country
data_usa_states = pandas.read_csv("50_states.csv")

state_list=[]

all_states= data_usa_states["state"].tolist()
new_game = Game(all_states)

while new_game.available_try > 0:
    answer_state = usa_map.textinput(f"{new_game.score}/50 States correct, {new_game.available_try} tries remaining", "Give the name of one of USA's states!")
    new_game.available_try -= 1
  
    #Make the player notice that he already found this country
    if new_game.state_already_found(answer_state):
        for _ in state_list:
            if _.id == answer_state:
                _.emphasize()
                break
    elif new_game.state_is_found(answer_state):
        x = int(data_usa_states[data_usa_states["state"] == answer_state]['x'])
        y = int(data_usa_states[data_usa_states["state"] == answer_state]['y'])

        turtle = st.State(answer_state, x, y)
        turtle.reveal()

        state_list.append(turtle)

new_game.end_of_game()
