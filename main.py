import glass

sc = """
def recursive(value):
	if value >= 0:
		print('recursive loop:',value)
		recursive(value-1)

recursive(777)
"""

gc = 'script.txt'

f = glass.load(gc)
exec(f)
print(f)

