from ursina import *

#creating more complex object, the class inherits from Entity
class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            #rotation argument, Vec3 is a rotation with a vector of 3
            rotation = Vec3(45,45,45),
            position = (5, -4)
            )

#create class for button, inherit from a in built class called Button
#each of the names, are key words, that have to be used to activate the function
class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.green,
            pressed_color = color.red
        )
    
    #see if button is pressed, check if hovering first, then if the key which is the mouse, pressed down on the left, it prints
    #key is a keyword, so it 'left mouse down
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print("button pressed")

#move entities on the screen
#the key word update will be called by Usina, so it has to be update the frame every time
def update():
    #if you press and hold on specific key, it will do whatever is inside the if statement
    if held_keys['a']:
        test_square.x -= 1 * time.dt

#creates window
app = Ursina()

#a entity in Usina can be anything, anything you see or hear on the screen, when you create it its automatically added to the game, and you can customize it
#model and color are arguements, the color.red is a key word
#'circle is a cirlce 'quad' is a square, 'cube' is a cube
test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,1))

#built in texture
sans_texture = load_texture('crate')
sans = Entity(model = 'quad', texture = sans_texture, color = color.orange, position = (-5,-1))

#calling the class
test_cube = Test_cube()

#calling the button
test_button = Test_button()

#runs the app
app.run()
