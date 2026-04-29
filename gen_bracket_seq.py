import sys

n = int(input())

if n == 0:
	sys.exit()

seq = []

def gen(opened, closed):
	if len(seq) == 2 * n:
		sys.stdout.write(''.join(seq) + '\n')
		return

	if opened < n:
		seq.append('(')
		gen(opened + 1, closed)
		seq.pop()

	if closed < opened:
		seq.append(')')
		gen(opened, closed + 1)
		seq.pop()

gen(0,0)