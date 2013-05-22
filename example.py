# coding=utf8

from progress import Progress

progress = Progress(description="Processing some items..", size=15)

import time

for i in range(15):
    time.sleep(0.2)
    progress.next_item("%d" % (15-i))

progress.finish()

progress.reset(description="Processing another one..", size=20)

for i in range(20):
    time.sleep(0.2)
    progress.next_item("%d" % i)

progress.finish()
