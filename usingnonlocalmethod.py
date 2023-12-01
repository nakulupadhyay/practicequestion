
def add():
    def fun():
        a=12
    def fun1():
        nonlocal a
        a=24
    def fun2():
        global a
        a=56
    a=10
    fun()
    print(a)
    fun1()
    print(a)
    fun2()
    print(a)
#global scope
a=23
add()
print(a)
