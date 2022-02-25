#Name: Fady Elsayed
#Date: Dec 14th 2021
#File Name: cbutton.py
#Description: A class for a circular button.

from graphics import *
import math

class CButton:
    
    """A button is a labeled circular in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""\

    def __init__(self, win, center, radius, label):
        """ Creates a circular button
        eg: qb = CButton(myWin, centerPoint, Width, height, 'quit') """

        self.center = center
        self.radius = radius
        self.circ = Circle(self.center, self.radius)
        self.circ.setFill('lightgray')
        self.circ.draw(win)
        self.label = Text(self.center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        x1, y1 = p.getX(), p.getY()
        x2, y2 = self.center.getX(), self.center.getY()

        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        return (self.active and distance <= self.radius)        

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circ.setWidth(1)
        self.active = False

    def setFill(self, color):
        "Sets the background colour of the button."
        self.circ.setFill(color)

    def setWidth(self, width):
        "Sets the width of the outline of the button."
        self.circ.setWidth(width)

    def setOutline(self, color):
        "Sets the colour of the outline of the button."
        self.circ.setOutline(color)

    def setFace(self, font):
        "Sets the font of the label."
        self.label.setFace(font)

    def setSize(self, size):
        "Sets the font size of the label."
        self.label.setSize(size)

    def setStyle(self, style):
        "Sets the font style of the label."
        self.label.setStyle(style)

    def setFontColour(self, color):
        "Sets the font style of the label."
        self.label.setFill(color)
            
    def move(self, dx, dy):
        "Moves button dx pixels right and dy pixels down"
        self.circ.move(dx, dy)
        self.label.move(dx, dy)
        self.center = Point(self.center.getX()+ dx, self.center.getY() + dy)
