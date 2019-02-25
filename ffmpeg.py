import subprocess

def encode(queue):
	while not queue.empty():
		video = queue.get()
		command_480 = 'ffmpeg -i ' + video + ' -s 640x480 -b:v 1M -r 30 ' + video[:-4] + '_480p.mp4'
		command_720 =  'ffmpeg -i ' + video + ' -s 1280x720 -b:v 1M -r 30 ' + video[:-4] + '_720p.mp4'

		subprocess.call(command_480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		subprocess.call(command_720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)

