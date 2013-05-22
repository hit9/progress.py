Progress
======== 

Progress status in the \*nix console.

Example
-------

```python
import time
from progress import Progress

items = ["item_a", "item_b", "item_c", "item_d", "item_e", "item_f", "item_g", "item_h"]

progress = Progress(description="Processing items..", size=len(items))

for item in items:
    # do some tasks i.e. sleep 0.2s
    time.sleep(0.3)
    progress.next_item(item)
progress.finish()

```

And the progress in the console looks like:

```
[ 37%] (item_c) Processing items..
```

Install
-------

```shell
virtualenv venv
. venv/bin/activate
pip install git+git://github.com/hit9/progress.py.git
```
