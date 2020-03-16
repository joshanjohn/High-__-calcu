# Area modules


import  math



def circle(radius):
    return round(math.pi*radius*radius,2)

def square(side):
    return round(side*side,2)

def rectangle(length,breadth):
    return round(length*breadth,2)

def triangle(base,heigth):
    return round(heigth*base/2,2)

def sphere(radius):
    return round(4*math.pi*radius*radius,2)

def cube(side):
    return round(6*side*side,2)

def cuboid(length,height,breadth):
    return round(2*length*breadth+2*length*height+2*breadth*height,2)

def cone(height,radius):
    l=math.sqrt(height*height+radius*radius)
    p=l+radius
    return round(math.pi*radius*p,2)

def cylinder(height,radius):
    j=height+radius
    return round(2*math.pi*j*radius,2)

def hemisphere(radius):
    return round(3*math.pi*radius*radius,2)