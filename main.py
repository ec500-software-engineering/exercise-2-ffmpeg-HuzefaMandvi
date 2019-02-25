import queue
import threading
import os
from ffmpeg import encode

in_path = './Videos/'
out_path = './Processed/'

def main():
	vidqueue = queue.Queue()
	folder = os.listdir(in_path)
	for video in folder:
		vidqueue.put(in_path + "/" + video)

	print(vidqueue)

	for i in range(3):
		encode_thread = threading.Thread(target = encode, args=(vidqueue,))
		encode_thread.start()

if __name__ == "__main__":
	main()
