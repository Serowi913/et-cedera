from requests import get as g
from PIL.ImageColor import getcolor as c

class Color:
    def __init__(self):
        self.color = str(g("https://colornames.org/random/json/").content).split('"')
        self.name = self.color[7]
        self.hex_code = self.color[3]
        self.rgb = self.con_rgb()
    
    def con_rgb(self):
        return c("#" + self.hex_code, "RGB")
