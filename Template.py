"""
CTEC 121
<Stephen Guild>
<Mod 8 Lab 1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
from dog import Dog
from msdie import MSDie
import docTest

def main():
    #Mod 7 assignment review
    '''
    myDict={}
    #key - value
    #create element
    myDict["key"]="value"
    myDict["key"]="new value"
    print(myDict.keys())
    print(myDict.values())
    print(myDict.items())
    '''

    '''
    fileHandle=open("sample.txt","r")
    #print(fileHandle.read())
    readReturn=fileHandle.read()
    print(type(readReturn))
    print("*",fileHandle.read(),"*")
    print()
    '''
    '''
    print()
    print(5*"All that")
    print()
    '''
    #section 1
    
    '''win=GraphWin("demo",800,800)
    myCircle=Circle(Point(400,400),200)
    myCircle.setFill("green")
    myCircle.draw(win)
    win.getMouse()'''
    
    #section 2
    d=Dog("Dog")
    print(d)
    #print(d._name)
    print(d.getName())
    d.setName("Godzilla")
    print(d.getName())

    d.bark()
    print()

    #section 3
    die=MSDie(6)
    print("number of sides", die.getSides())
    print("value:", die.getValue())
    die.setValue(5)
    print("value:", die.getValue())
    die.setValue(12)
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())

    print()
    #print module/file header documentation
    print(docTest.__doc__)
    #print class docs
    print(docTest.DocTest.__doc__)
    #print method docs
    print(docTest.DocTest.method.__doc__)
    print()
    

main()    