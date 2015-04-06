import subprocess
import schedule
import time


def job():
        execR = subprocess.call(['/usr/bin/Rscript','fb.R'])
	execRails = subprocess.call(['/usr/bin/python','api.py'])

schedule.every().hour.do(job)
c = 0
while True:
        c+=1
	print c
        schedule.run_pending()
        time.sleep(1)

#job()
