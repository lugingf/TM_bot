from datetime import datetime
import os

LOGDIR_NAME = 'logs'

def start_log():
	curdate = str(datetime.now().date())
	curtime =  datetime.now().time()
	print(curdate, str(curtime)[:-7])
	try:
		os.mkdir('./' + LOGDIR_NAME, mode=0o777, dir_fd=None)
		print('Folder {} created'.format(LOGDIR_NAME))
	except FileExistsError:
		print('Directory {} already exists'.format(LOGDIR_NAME))
	filename = './' + LOGDIR_NAME + '/' + 'TM_bot_' + curdate  # + 'T' + str(curtime)[:-7]
	print(filename)
	log_file = open(filename, 'a')
	log_file.write('BOT Tovarishch major started at %s \n' % str(curtime)[:-7])
	log_file.close()



def to_log(message):
	filename = str(datetime.now().date()) + 'T' + str(datetime.now().time())
	log_file = open()


if __name__ == '__main__':
	start_log()