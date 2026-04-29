def generate(cur, open, closed, n):
    if len(cur) == 2*n:
        print(cur)
        return
    generate(cur + '(', open + '(', closed, n)
    if closed < open:
        generate(cur + ")", open, closed + 1, n)

def parens(n):
    generate(" ", 0, 0, n)
