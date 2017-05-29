from time import time,sleep

class Camera(object):
	def __init__(self):
		#self.frames = [open('static/' + f + '.jpg', 'rb').read() for f in ['img0001','img0010','img0020']]
		self.files = ['img' + str(int(x)).zfill(4) + '.jpg' for x in range(1,251)]

	def get_frame(self):
		return self.frames[int(time()) % 3]
	
	def get_frame_n(self, n):
		print str(n)
		frame = open('static/' + self.files[n]).read()
		return frame

	def get_stream(self):
		for file in self.files:
			sleep(0.041)
			yield open('static/' + file).read()