import cv2

def multi_stitch(img_array):
	stitcher = cv2.createStitcher(False)
	ims = []
	for i, img in enumerate(img_array):
		ims.append(cv2.imread(img))

	output = stitcher.stitch(tuple(ims))

	return output


if __name__ == '__main__':
	test_images = ["pcb_0.png","pcb_1.png","pcb_2.png","pcb_3.png","pcb_4.png",
			  "pcb_5.png","pcb_6.png","pcb_7.png","pcb_8.png","pcb_9.png",
			  "pcb_10.png", "pcb_11.png", "pcb_12.png", "pcb_13.png",
			  "pcb_14.png", "pcb_15.png", "pcb_16.png", "pcb_17.png"]
	im = multi_stitch(test_images)
	cv2.imwrite("output.png", im[1])