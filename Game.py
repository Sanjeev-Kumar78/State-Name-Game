import turtle
import pandas

# Initialize the screen
screen = turtle.Screen()
screen.title("State Game")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=783, height=900)

guessed_states = []  # List to store the guessed states for score
data = pandas.read_csv("indian_states.csv")  # Read the csv file

while len(guessed_states) < 29:
    # Get the answer from the user
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/29 States Correct", prompt="What's another state's name?").title()

    # Check if the answer is correct
    if answer_state in data.State.to_list():
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.State == answer_state].x),
               int(data[data.State == answer_state].y))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
    else:
        if screen.textinput(title="Wrong Answer", prompt="Try Again! Enter Yes or No").title() == "Yes":
            continue
        else:
            print("Good Bye!")

            try:
                turtle.Screen().bye()
                break
            except:
                print("Exit turtle")
                break

        # Hint TODO: Add a hint feature

turtle.write("You Win", align="center", font=("Arial", 8, "normal"))
screen.exitonclick()


# **Get the mouse click coordinates**
"""# def get_mouse_click_coor(x, y):
#     print(f"{x},{y}")
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()"""

