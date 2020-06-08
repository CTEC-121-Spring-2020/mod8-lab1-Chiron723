#msdie.py
from random import randrange
class MSDie:
    #constructor
    def __init__(self, sides):
        self._sides=sides
        self._value=1
    
    #setters/getters mutators/accessors
    def getSides(self):
        return self._sides
    def setValue(self, value):
        if value >= 1 and value <= self._sides:
            self._value=value
    def getValue(self):
        return self._value

    def roll(self):
        self._value=randrange(1, self._sides+1)