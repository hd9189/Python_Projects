#do basic 2d operations
import turtle
import time
import random

'''Note that the screen will dissapear once program is finsihed'''

#define width and height of screen, all caps mean that values are constant
WIDTH, HEIGHT = 500, 500

#list of colours for turtles
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

#Input number of turtles
def get_number_of_racers():
    racers = 0
    #use while loop to continue to loop untill we get a valid input
    while True:
        racers = input("Enter the number of racers (2-10): ")
        #checks if string is completely numeric or not
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            #brings us back to the beginning of while loop
            continue

        if 2 <= racers <= 10:
            #return breaks the while loop
            return racers
        else:
            print("Number not in range 2-10. Try Again!")
            #no need continue because its the end already

#make a function for screen, so that screen won't show unless we call this function first
def init_turtle():
    # makes a screen using turtle
    screen = turtle.Screen()
    # sets up screen height and width, screen created is a cartesian plain with a middle point of (0,0)
    screen.setup(WIDTH, HEIGHT)
    # sets title of window
    screen.title("Turtle Racer!")

#parameter will be colors that are gotten from the shuffle
def create_turtles(colors):
    #use list because don't know how many turtles will have
    turtles = []
    #spacing so that the objects can be evenly spread
    spacingx = WIDTH //(len(colors)+1)
    #enumerate gives the index then the object value
    for i, color in enumerate(colors):
        #initialize or create turtle object
        racer = turtle.Turtle()
        #set color
        racer.color(color)
        #set shape
        racer.shape('turtle')
        #rotates the object 90 degrees left
        racer.left(90)
        #lift up the line from the back of the racer
        racer.penup()
        #set position of turtle
        racer.setpos(-WIDTH//2+(i+1)*spacingx, -HEIGHT//2+20)
        #set the position, without having the lines drawn then have pen down
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    #put the function inside the function so that once everything is set the funtion will create turtle for us
    turtles = create_turtles(colors)
    #keep moving the turtles until one reaches the top of screen
    while True:
        for racer in turtles:
            #for every iteration, we will move the turtle from the range of 1-20, dicatates the speed
            distance = random.randrange(1, 20)
            racer.forward(distance)

            #give position of the object
            x,y = racer.pos()
            if y >= HEIGHT//2-30:
                #get index for turtle to return the turtle color
                return colors[turtles.index(racer)]
def play():
    racers = get_number_of_racers()
    init_turtle()
    #randomize the items in list
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print("{w} is the winner of the race!!!".format(w = winner))
    time.sleep(5)
    again = input("Would you like to play agian? (Y/N): ")
    if again.lower() == "y":
        play()

print(play())