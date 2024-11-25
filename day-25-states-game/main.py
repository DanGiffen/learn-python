import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)


turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = []
state_list = data.state.to_list()
print(state_list)
#play_game = True

#while play_game:
while len(correct_guesses) < 50:
    score = len(correct_guesses)
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_guesses]
        # for state in state_list:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        correct_guesses.append(answer_state)
        state_detail = data[data.state == answer_state]
        # x_coord = state_detail.x.values my solution
        # y_coord = state_detail.y.values my solution. could also state_detail.y.item() which is a series method
        text_turt = turtle.Turtle()
        text_turt.penup()
        #text_turt.goto(x_coord[0], y_coord[0]) my solution
        text_turt.goto(int(state_detail.x), int(state_detail.y))
        text_turt.hideturtle()
        text_turt.write(answer_state)
