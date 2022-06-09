import argparse
from importlib.resources import path
from ifcopenshell import geom
import pathlib
from pathlib import Path
from utils import Utils as ut

def main(input_folder, output_path):

	# Create empty list for the bounding boxes
	boundingBoxes = []
	# Create empty graph
	graph = ut.createGraph()
	
	# Get path, get files from the directory
	#folder = pathlib.Path().parent.resolve() / "resources"
	path = pathlib.Path(input_path)
	files = [f for f in path.iterdir() if ".ifc" in f.name.lower()]
	# Open all files in the directory
	# Generate bounding boxes for all ifc products and add them to the list
	for f in files:
		print("Parsing " + f.name + "...")
		boundingBoxes.extend(ut.createBoundingBoxes(path,f))  

	# Collision check
	ut.collisionCheck(boundingBoxes, graph)
	
	# Creation of the graph
	graph.serialize(destination=output_path, format='turtle')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input_folder",
						required = True,
						help = "Path to the folder containing the ifc files",
						type = str)
	parser.add_argument("-o","--output_file",
                        required = True,
                        help = "Path to the output file",
                        type = str)

	args = parser.parse_args()
	
	input_folder = args.input_folder
	output_path = args.output_file

	main(input_path, output_path)