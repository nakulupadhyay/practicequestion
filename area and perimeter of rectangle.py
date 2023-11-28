def area_of_rect(l,b):
    return l*b


def peri_of_rect(l,b):
    return 2*(l+b)


length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
area=area_of_rect(length,breadth)
peri=peri_of_rect(length,breadth)

print(f'area of the rectangle is {area}')
print(f'perimeter of the rectangle is {peri}')
