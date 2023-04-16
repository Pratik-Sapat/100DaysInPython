import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() #get all states.
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() #title case ->convert First letter capital for user type.

    #if answer is one of the states in all the states of the 50_state.csv. 
    if answer_state == "Exit": #bcz title case E should be capital.
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pull out row of state.
        t.goto(int(state_data.x), int(state_data.y)) #goto location of states using axis point.
        t.write(answer_state) #or t.write(state_data.state.item())

#states to learn.csv ->states which user not guessed.


# turtle.mainloop() => #keep screen open :-alternate to exitonclick.