from importlib.resources import path
from ifcopenshell import geom
import pathlib
from utils import Utils 

ut = Utils()
graph = ut.createGraph()

path = pathlib.Path().parent.resolve() / "resources"
files = pathlib.Path(path)

boundingBoxes = []

for file in files.iterdir():
  print(file.name)
  
  boundingBoxes.extend(ut.createBoundingBoxes(path, file))  

# Colision
ut.collisionCheck(boundingBoxes, graph)

graph.serialize(destination='C:/Users/atn/Desktop/output.ttl', format='turtle')