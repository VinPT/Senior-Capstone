import os
import shutil

i = 0

def main():
	if(not os.path.exists("splitting")):
		os.mkdir("splitting")
	shutil.copyfile("camera_folder/image_example_0.JPG", "splitting/001.jpg")
	splitting()
	if(not os.path.exists("testing")):
		os.mkdir("testing")
	#shutil.copytree("splitting", "testing")
	sp_to_ts()
	testing()
	#shutil.rmtree("testing")

def splitting():
	for j in range(0, 10):
		shutil.copyfile("splitting/001.jpg", "splitting/split_"+str(j)+".jpg")
	os.remove("splitting/001.jpg")
	#os.chdir("..")

def testing():
	os.mkdir("used/00"+str(i))
	count = 0
	#shutil.rmtree("splitting")
	while os.path.isfile("testing/split_"+str(count)+".jpg"):
		shutil.move("testing/split_"+str(count)+".jpg", "used/00"+str(i)+"/split_"+str(count)+".jpg")
		count+=1
	
def sp_to_ts():
	#empty = False
	count = 0
	while os.path.isfile("splitting/split_"+str(count)+".jpg"):
		shutil.move("splitting/split_"+str(count)+".jpg", "testing/split_"+str(count)+".jpg")
		count+=1

	
if __name__ == '__main__':
	if(os.path.exists("used")):
		shutil.rmtree("used")
		os.mkdir("used")
	for k in range(0, 5):
		main()
		i+=1
	print("Move complete")
	