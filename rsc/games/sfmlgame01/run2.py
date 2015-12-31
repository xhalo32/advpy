from __future__ import division

from random import randint
from math import cos
from pygame.time import Clock

from sfml import sf

class Effect(sf.Drawable):
    def __init__(self, name):
        sf.Drawable.__init__(self)

        self._name = name
        self.is_loaded = False

    def _get_name(self):
        return self._name

    def load(self):
        self.is_loaded = sf.Shader.is_available() and self.on_load()

    def update(self, time, x, y):
        if self.is_loaded:
            self.on_update(time, x, y)

    def draw(self, target, states):
        if self.is_loaded:
            self.on_draw(target, states)
        else:
            error = sf.Text("Shader not\nsupported")
            error.font = sf.Font.from_file("data/sansation.ttf")
            error.position = (320, 200)
            error.character_size = 36
            target.draw(error, states)

    name = property(_get_name)



class StormBlink(Effect):
    def __init__(self):
        Effect.__init__(self, 'storm + blink')

        self.points = sf.VertexArray()

    def on_load(self):
        # create the points
        self.points.primitive_type = sf.PrimitiveType.POINTS

        for i in range(40000):
            x = randint(0, 32767) % 800
            y = randint(0, 32767) % 600
            r = randint(0, 32767) % 255
            g = randint(0, 32767) % 255
            b = randint(0, 32767) % 255
            self.points.append(sf.Vertex(sf.Vector2(x, y), sf.Color(r, g, b)))

        try:
            # load the shader
            self.shader = sf.Shader.from_file("data/storm.vert", "data/blink.frag")

        except: pass

        return True

    def on_update(self, time, x, y):
        radius = 200 + cos(time) * 150
        self.shader.set_parameter("storm_position", x * 800, y * 600)
        self.shader.set_parameter("storm_inner_radius", radius / 3)
        self.shader.set_parameter("storm_total_radius", radius)
        self.shader.set_parameter("blink_alpha", 0.5 + cos(time*3) * 0.25)

    def on_draw(self, target, states):
        states.shader = self.shader
        target.draw(self.points, states)

            ## --- ##

class WaveBlur(Effect):
    def __init__(self):
        Effect.__init__(self, 'wave + blur')

    def on_load(self):
        with open("data/text.txt") as file:
            self.text = sf.Text(file.read())
            self.text.font = sf.Font.from_file("data/sansation.ttf")
            self.text.character_size = 22
            self.text.position = (30, 20)

        self.texture = sf.Texture.from_file("data/background.jpg")
        self.sprite = sf.Sprite(self.texture)

        try:
            # load the shader
            self.shader = sf.Shader.from_file("data/wave.vert")#, "data/blur.frag")

        except: pass
        return True

    def on_update(self, time, x, y):
        self.shader.set_parameter("wave_phase", time)
        self.shader.set_parameter("wave_amplitude", x * 40 - self.text.position[ 0 ] / 40., y * 40 - self.text.position[ 0 ] / 40.)
        self.shader.set_parameter("blur_radius", (x + y) * 0)

    def on_draw(self, target, states):
        states.shader = self.shader
        target.draw(self.text, states)



window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML - Shader")
window.vertical_synchronization = True

# create the effects
effect = WaveBlur(  )

# initialize them
effect.load()

# create the message background
try:
    text_background_texture = sf.Texture.from_file("data/text-background.png")
except: pass

# load the messages font
try:
    font = sf.Font.from_file("data/sansation.ttf")

except IOError as error:
    print("An error occured: {0}".format(error))
    exit(1)

clock = sf.Clock()
c = Clock(  )

# start the game loop
while window.is_open:

    # update the current example
    x = sf.Mouse.get_position(window).x / window.size.x
    y = sf.Mouse.get_position(window).y / window.size.y
    effect.update(clock.elapsed_time.seconds, x, y)

    # process events
    for event in window.events:

        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()

        if type(event) is sf.KeyEvent and event.pressed:
            # escapte key: exit
            if event.code == sf.Keyboard.ESCAPE:
                window.close()
    if sf.Keyboard.is_key_pressed( sf.Keyboard.RIGHT ):
        effect.text.position += ( 5, 0 )

    if sf.Keyboard.is_key_pressed( sf.Keyboard.LEFT ):
        effect.text.position += ( -5, 0 )

    if sf.Keyboard.is_key_pressed( sf.Keyboard.UP ):
        effect.text.position += ( 0, -5 )

    if sf.Keyboard.is_key_pressed( sf.Keyboard.DOWN ):
        effect.text.position += ( 0, 5 )


    # clear the window
    window.clear(sf.Color(255, 128, 0))

    # draw the current example
    window.draw(effect)

    # finally, display the rendered frame on screen
    window.display()
    c.tick( 60 )