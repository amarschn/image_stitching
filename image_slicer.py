import cv2
import numpy as np
import ipdb

def slice_image(img, output_size, overlap):
	im = cv2.imread(img)
	input_height = im.shape[0]
	input_width = im.shape[1]
	h = output_size[0]
	w = output_size[1]
	h_o = overlap[0]
	w_o = overlap[1]
	rows = input_height / h
	cols = input_width / w

	if input_height % h > 0:
		rows += 1
	if input_width % w > 0:
		cols += 1

	im_array = []

	# ipdb.set_trace()

	for r in range(rows):
		for c in range(cols):
			h_begin = r * h - h_o
			h_end = (r + 1) * h - 1 + h_o
			w_begin = w * c - w_o
			w_end = (c + 1) * w - 1 + w_o


			if h_begin < 0:
				h_begin = 0
			if w_begin < 0:
				w_begin = 0
			if h_end > input_height:
				h_end = input_height
			if w_end > input_width:
				w_end = input_width

			im_slice = im[h_begin:h_end, w_begin:w_end, :]

			im_array.append(im_slice)

	return im_array

if __name__ == '__main__':
	images = slice_image('pcb_whole.png', [1000, 1000], [100,100])
	for i, image in enumerate(images):
		cv2.imwrite("pcb_%d.png" % i, image)