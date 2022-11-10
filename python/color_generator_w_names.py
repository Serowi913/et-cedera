from requests import get as g
from PIL.ImageColor import getcolor as c # function to convert hex to RGB

class Color:
    def __init__(self):
        clr_request = str(g("https://colornames.org/random/json/").content).split('"') # request JSON, makes list
        self.color = [clr_request[7], clr_request[3]] # make a list of only the name and hex value
        self.name = self.color[0]
        self.hex_code = self.color[1]
        self.rgb = self.con_rgb()
    
    def con_rgb(self):
        return c("#" + self.hex_code, "RGB") # converts hex to RGB
