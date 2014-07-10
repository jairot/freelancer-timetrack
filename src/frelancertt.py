import os
import csv
import sys

from random import random
from datetime import datetime
from time import sleep
from subprocess import check_output

SHOTINTERVAL = 600

if os.path.isfile("worksheet.csv"):
    fp = open("worksheet.csv", "a")
    writer = csv.writer(fp)
else:
    fp = open("worksheet.csv", "w")
    writer = csv.writer(fp)
    writer.writerow(["Project", "Start", "End", "Sum[min]"])

workingon = sys.argv[1]
startdate = datetime.now()

try:
    while True:
        splitat = random()
        sleep(SHOTINTERVAL*splitat)
        now = datetime.now().isoformat().split(".")[0]
        check_output(['scrot', '%s_%s.png' % (now, workingon)])
        print "Saving scrot %s_%s.png" % (now, workingon)
        sleep(SHOTINTERVAL*(1 - splitat))
except KeyboardInterrupt:
    enddate = datetime.now()
    delta = enddate - startdate
    acumulated = int(round(delta.total_seconds() / 60, -1))
    print "%d minutes Worked" % acumulated
    writer.writerow([workingon, startdate.isoformat().split(".")[0],
                     enddate.isoformat().split(".")[0], acumulated])
