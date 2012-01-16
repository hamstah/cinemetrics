# -*- coding: utf-8 -*-
import sys
import os
import os.path
import glob
import xml.etree.ElementTree as et
import utils

OUTPUT_DIR_NAME = "shot_snapshots"


def main():

	tree = utils.import_project(sys.argv)
	if tree == None:
		return

	#frames = [os.path.splitext(file)[0] for file in os.listdir(os.getcwd() + "\\" + OUTPUT_DIR_NAME) if not os.path.isdir(file)]
	
	frames = [os.path.splitext( os.path.basename(file) )[0] for file in glob.glob(os.path.join(OUTPUT_DIR_NAME,"*.png"))] #os.getcwd() + "\\" +
	frames = [int(frame) for frame in frames]

	movie = tree.getroot()
	# frame count 
	movie.set("frames", str( frames[-1] - frames[0] ))
	movie.set("start_frame", str( frames[0] ))
	movie.set("end_frame", str( frames[-1] - 1 ))
	tree.write("project.xml")
	
	f = open(os.path.join(os.getcwd(), "shots.txt"), "w")
	
	for i, frame in enumerate(frames):
		if i == len(frames)-1:
			break
		
		f.write(str(frame) + "\t" + str(frames[i+1]-1) + "\t" + str(frames[i+1] - frame) + "\n")
		
		if i > 0:
			diff = frames[i] - frames[i-1]
			if abs(diff) <= 5:
				print "%d -> %d: %d" % (frames[i-1], frames[i], diff)
	
	f.close()
	print "don't forget to add FPS information!"
	raw_input("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################
