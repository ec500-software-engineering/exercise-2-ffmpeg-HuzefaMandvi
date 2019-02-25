import subprocess

in_path = './Videos/'
out_path = './Processed/'

def encode(queue, path):
	while not queue.empty():
		video = queue.get()
		480_command = 'ffmpeg -i ' + video + ' -s 640x480 -b:v 1M -r 30 ' + video[:-4] + '_480p.mp4'
		720_command =  'ffmpeg -i ' + video + ' -s 1280x720 -b:v 1M -r 30 ' + video[:-4] + '_720p.mp4'

		subprocess.call(480_command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		subprocess.call(720_command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)

