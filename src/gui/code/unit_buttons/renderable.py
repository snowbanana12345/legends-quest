
"""
Abstract class renderable
"""
class Renderable:
    def __init__(self, xlength, ylength):
        self.xlength = xlength
        self.ylength = ylength

    """
    scales all images appropriately such that it fits into the box 
    """
    def scale(self):
        pass

    """
    renders onto the Surface at xpos and ypos
    """
    def render(self, surface, xpos, ypos):
        pass