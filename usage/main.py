#!/usr/bin/env python
# secure your script into a glasstext
from glasstext import glass

gc = 'script.txt'
f = glass.load(gc)
exec(f)
print(f)

