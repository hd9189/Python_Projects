from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/soil_block.png')
glass_texture = load_texture('assets/light_blue_block.png')
red_dirt_texture = load_texture('assets/red_dirt_block.png')
stone_brick_texture = load_texture('assets/stone_brick_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound.wav', loop = False, autoplay = False)
#takes away fps counter and exit button
window.fps_counter.enabled = False
window.exit_button.visible = False
block_pick = 1

#run on every single frame
def update():
    global block_pick

    #update function use left mouse instead of left mouse down
    '''if held_keys['left mouse'] or held_keys['right mouse']: 
        hand.active()
    else: 
        hand.passive()'''

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7


#creating sky entity
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            #creates double sided
            double_sided = True
        )

#creating hand
'''class Hand(Entity):
    def __init__(self):
        super().__init__(
            #attached to camera not the game itself
            parent = camera.ui,
            model = 'cube',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10.0),
            position = Vec2(0.4,-0.6)
        )
    
    #arm movement
    def active(self):
        self.postion = Vec2(0.3,-0.5)
    
    def passive(self):
        self.postion = Vec2(0.4,-0.6)'''

#create it to inherit button, because we need to know where each voxel is, and click on them to add another
class Voxel(Button):
    #has position, so it can change with every input
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            #the actual scene of the game
            parent = scene,
            position = position,
            model = 'cube',
            #height and 3d space of the cueb
            origin_y = 0.5,
            #so we can acutally see the cube
            #need texture and color always
            texture = texture,
            #use RGB values
            color = color.color(0,0,random.uniform(0.9,1))
        )
    
    #create new button press function to add block
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: 
                #the .normal is what face of the cube our mouse is point at
                    voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = red_dirt_texture)
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = stone_brick_texture)

            #destroying self is destroying the block
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

for z in range(40):
    for x in range(40):
        voxel = Voxel(position = (x,0,z))

#create first person, automatically gives basic controls
player = FirstPersonController()
#create sky and run the class
sky = Sky()
#create hand
'''hand = Hand()'''
app.run()