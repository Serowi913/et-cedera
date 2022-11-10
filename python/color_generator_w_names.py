from requests import get as g
from PIL.ImageColor import getcolor as c # function to convert hex to RGB

class Color:
    def __init__(self):
        clr_request = str(g("https://colornames.org/random/json/").content).split('"') # request JSON, makes list
        self.color = [clr_request[7], self.con_rgb(clr_request[3])] # make a list of only the name and RGB value
        self.name = self.color[0]
        self.rgb = self.color[1]
        self.hex_code = clr_request[3] # index of the hex code in the inital request list
    
    def con_rgb(self, hex=None):
        if hex is None:
            return c("#" + self.hex_code, "RGB") # converts self hex into RGB
        else:
            return c("#" + hex, "RGB") # converts argument hex to RGB

        
#-----------------------------------------------------------------------------------------------------------------------------------------------        

# Below code uses pygame to display a window that can generate different colors (press F), display them, and save them to "colors.txt" (press S)
# However, the above Color file can be used completely separately on its own

#-----------------------------------------------------------------------------------------------------------------------------------------------
        
import pygame as pg
import sys
from color import Color

class Main:

    def __init__(self):
        self.window_size = (400, 400)
        self.window = pg.display.set_mode(self.window_size)
        self.clock = pg.time.Clock()
        self.bg_color = (255, 255, 255)
        self.running = True
        self.rect = pg.Rect(20, 20, 360, 360)
        y = Color()
        self.rect_color = y.rgb
        print(y.name, y.rgb)
        self.current_color = y.rgb
        self.current_color_name = y.name
        with open("colors.txt", "a") as t:
            t.write('\n')
    
    def run(self):
        while self.running:
            self.window.fill(self.bg_color)

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.running = False
                    sys.exit()
                
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_f:
                        x = Color()
                        self.rect_color = x.rgb
                        print(x.name, x.rgb)
                        self.current_color = x.rgb
                        self.current_color_name = x.name

                    if e.key == pg.K_s:
                        with open("colors.txt", "a") as f:
                            f.write(f"{self.current_color_name}: {self.current_color}\n")
                            print(f"saved: {self.current_color_name}")
            

            pg.draw.rect(self.window, self.rect_color, self.rect)

            
            pg.display.flip()
            self.clock.tick(60)

Main().run()
