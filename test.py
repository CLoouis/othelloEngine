# import anytree
from legal import *
from game import *
from anytree import Node, RenderTree

def makeTree():
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    return udo

boas = makeTree()
print(RenderTree(boas))