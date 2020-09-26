def a():
    d = 1
    def c():
        nonlocal g
        print(g)
    c()

a()
