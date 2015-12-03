from message import Messages
import pygame as pg, math

class Slider(object):
    
    def __init__(self,
                 scr,
                 colour = (255, 255, 255),
                 secondary_colour = (200, 200, 200),
                 pos_size = [100, 100, 100, 20],
                 steps = 10):
        
        self.scr = scr
        self.pos_size = pos_size
        self.steps = steps
        self.color = colour
        self.secondary_color = secondary_colour
        self.dragging = False
        self.sliderpos = math.floor((steps)/2.0)
        
        self.steplen = pos_size[2] / float(steps)
        self.center = pos_size[0] + pos_size[2] / 2, \
                      pos_size[1] + pos_size[3] / 2
        
        self.button = self.center[0]
        
        self.msg = Messages(self.scr)
    
    def run(self, name=""):
        
        self.action()
        
        if self.dragging:
            pg.draw.rect(self.scr, self.secondary_color, self.pos_size)
            
            pg.draw.circle(self.scr, self.half(self.secondary_color),
                       [int(self.button), self.pos_size[1] + self.pos_size[3] / 2],
                       self.pos_size[3] / 2)
        else:
            pg.draw.rect(self.scr, self.color, self.pos_size)
            
            pg.draw.circle(self.scr, self.half(self.color),
                       [int(self.button), self.pos_size[1] + \
                            self.pos_size[3] / 2],
                       int(self.pos_size[3] / 2.2))
        
        self.msg.message(name,
                         [self.button,
                         self.pos_size[1] + self.pos_size[3] / 2],
                         self.invert(self.color), 30)
        
        return self.sliderpos
        
    def action(self):
        
        self.rel = pg.mouse.get_rel()[0]
        
        mclick = pg.mouse.get_pressed()
        mpos = pg.mouse.get_pos()
        
        if mclick[0]:
            if mpos[0] < self.pos_size[0] + self.pos_size[2] and\
               mpos[0] > self.pos_size[0]:
               
                if mpos[1] > self.pos_size[1] and\
                  mpos[1] < self.pos_size[1] + self.pos_size[3]:
                   
                    self.dragging = True
                    
        else: 
            self.dragging = False
        
        if self.dragging:
            
            for i in range(self.steps):
                
                if mpos[0] > self.pos_size[0] + (i) * self.steplen and \
                   mpos[0] < self.pos_size[0] + (i + 1) * self.steplen:
                    
                    self.sliderpos = i
                    
                    self.button = self.pos_size[0] + (i + 1) \
                     * self.steplen - self.steplen / 2
            
    def invert(self, color):
        rcolor = []
        try:
            for c in color:
                rcolor.append(255 - c)
            return rcolor
        except:
            return color
    
    def half(self, color):
        rcolor = []
        try:
            for c in color:
                rcolor.append( int( c**(math.sqrt(0.7)) ) )
            return rcolor
        except:
            return color
        
        
        
        
        
        
        
            
            
            