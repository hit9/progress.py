# coding=utf8

import sys


class Progress(object):

    def __init__(self, description='', size=0):
        self.reset(description=description, size=size)

    def next_item(self, item=''):
        self.counter += 1
        if self.item:
            sys.stdout.write(
                "\r"+" "*(len(self.description)+11+len(self.item))
            )
        sys.stdout.write("\r")
        sys.stdout.write("[%3d%%] " % int(100 * self.counter / self.size))
        sys.stdout.write("(%s) " % item)
        sys.stdout.write(self.description)
        sys.stdout.flush()
        self.item = item

    def reset(self, description='', size=0):
        self.description = description
        self.size = size
        self.item = None
        self.counter = 0

    def finish(self):
        sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == '__main__':
    import time
    items = ["item_a", "item_b", "item_c", "item_d", "item_e", "item_f", "item_g", "item_h"]
    progress = Progress(description="Processing items..", size=len(items))
    for item in items:
        # do some tasks i.e. sleep 0.2s
        time.sleep(0.3)
        progress.next_item(item)
    progress.finish()
