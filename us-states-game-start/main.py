import turtle
import pandas


class State(turtle.Turtle):
    def __init__(self, x, y, staten):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(staten, False, align='left', font=("Courier New", 8, 'normal'))


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed = 0
states_data = pandas.read_csv("50_states.csv")

# if "Alaska" in list(states_data["state"]):
#     print(states_data[states_data["state"] == "Alaska"]['x'].item())
#     print(states_data[states_data["state"] == "Alaska"]['y'].item())
#     print(type(int(states_data[states_data["state"] == "Alaska"].index[0])))
#     states_data = states_data.drop(index=states_data[states_data["state"] == "Alaska"].index[0])

#     print(states_data)

try:
    while guessed <= 50 or len(states_data) < 1:
        titles = str(guessed) + " / 50 States correct"
        answer_state = screen.textinput(titles, "Please Enter Name of the State").title()
        if answer_state in list(states_data["state"]):
            newturtle = State(states_data[states_data["state"] == answer_state]['x'].item(),
                              states_data[states_data["state"] == answer_state]['y'].item(),
                              answer_state)
            states_data = states_data.drop(index=states_data[states_data["state"] == answer_state].index[0])
            guessed += 1
        if answer_state.lower() == "exit":
            break
except Exception as e:
    print(e)
print("You missed next States")
states_data.to_csv("States that left")
