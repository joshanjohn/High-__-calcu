import peri
import vol
import math
import arth
import area
import webbrowser
import sys 
n=9
for i in range(0,n+1):

    print("""
            [1] arithematic operation
            [2] calculate area
            [3] calculate perimeter
            [4] calculate volume
            [5] multiplication tables
            [6] even or odd
            [7] number sorting
            [8] HANG IT OUT
            [9] help
                                        """)
            
    choice = int(input("Select operation :"))

    if choice == 1:
        print("""
                |1| addition
                |2| subtraction
                |3| division
                |4| multiplication
                |5| remainder
                |6| integer quoteient
                |7| square root
                                    """)
        ch = int(input("Enter the operation :"))

        if ch ==1:
            lk = float(input("Enter first number :"))
            kj = float(input("Enter second number :"))
            print(lk,"+",kj,"=",arth.add(lk,kj))
        elif ch ==2:
            ok = float(input("Enter first number :"))
            ij = float(input("Enter second number :"))
            print(ok,"-",ij,"=",arth.sub(ok,ij))
        elif ch ==3:
            op = float(input("Enter first number :"))
            po = float(input("Enter second number :"))
            print(op,"/",po,"=",arth.div(op,po))
        elif ch ==4:
            hi = float(input("Enter first number :"))
            ih = float(input("Enter second number :"))
            print(hi,"*",ih,"=",arth.multi(hi,ih))
        elif ch==5:
            lo = float(input("Enter first number :"))
            ol = float(input("Enter second number :"))
            print("remainder =",arth.remain(lo,ol))
        elif ch ==6:
            pi = float(input("Enter first number :"))
            ip = float(input("Enter second number :"))
            print("quotioent =",arth.intgr(pi,ip))
        elif ch ==7:
            a = float(input("Enter the number:"))
            print("square root =",arth.sqrt(a))
        else:
            print("Invalid option!")
    elif choice == 2:
        print("""
                (1) rectangle           (9) cylinder                              
                (2) triangle           (10) hemisphere                           
                (3) circle             (11) frustum of cone                              
                (4) square                                         
                    (5) sphere                                         
                (6) cuboid                                     
                (7) cube                                       
                (8) cone                                      
                
                                                            """)
        opt =int(input("Enter the shape:"))
        if opt ==1:
            lb = float(input("Enter the  lenght (Cm) :"))
            bl = float(input("Enter the breadth (Cm) :"))
            print("Area of rectangle =",area.rectangle(lb,bl),"Cm")
        elif opt ==2:
            hb = float(input("Enter the height (Cm) :"))
            bh = float(input("Enter the base (Cm) :"))
            print("Area of triangle =",area.triangle(bh,hb),"Cm")
        elif opt ==3:
            gf = float(input("Enter the radius (Cm) :"))
            print("Area of circle =", area.circle(gf),"Cm")
        elif opt ==4:
            ss = float(input("Lengthh of side (Cm) :"))
            print("Area of square =",area.square(ss),"Cm")
        elif opt ==5:
            tr = float(input("Enter the radius (Cm) :"))
            print("Area of sphere =",area.sphere(tr),"Cm")
        elif opt ==6:
            ko = float(input("Enter the length (Cm): "))
            ft = float(input("Enter the breadth (Cm) :"))
            rt = float(input("Enter the height (Cm) :"))
            print("Area  of cuboid =",area.cuboid(ko,rt,ft),'Cm')
        elif opt ==7:
            dr = float(input("Enter side length (Cm) : "))
            print("Area of cube =",area.cube(dr),"Cm")
        elif opt ==8:
            ji = float(input("Enter the height (Cm):"))
            hy = float(input("Enter the radius (Cm):"))
            print("Area of cone =",area.cone(ji,hy),'Cm')
        elif opt ==9:
            ft = float(input("Enter the height (Cm):"))
            dek= float(input("Enter the radius (Cm)"))
            fr=ft+dek
            print(("Area of cylinder ="),area.cylinder(ft,dek),"Cm")
        elif opt ==10:
            hy = float(input("Enter the radius (Cm):"))
            print("Area of hemisphere =",area.hemisphere(hy),'Cm')
        elif opt ==11:
            ds = float(input("Enter the Base radius (Cm): "))
            dr = float(input("Enter the height (Cm):"))
            fr = float(input("Enter the Upper radius (Cm):"))
            j=math.sqrt(dr**2+(fr-ds))
            print("Area of frustum of cone = ",round(math.pi*((ds*ds)+(dr*dr)+j*(ds+fr)),2)," Cm")


    elif choice == 3:
        print("""
                    |1| Square                                             
                    |2| Rectandle                                         
                    |3| Circle                                               
                    |4| Triangle                                             
                                                            
                                                                """)
        opt =int(input("Enter the shape :"))
        if opt ==1:
            gb = float(input(" Enter  side lenght (Cm):"))
            print("perimeter of square =",peri.square(gb),'cm')
        elif opt ==2:
            lk = float(input("Enter the lenght(Cm):"))
            lp = float(input("Enter the breadth(Cm):"))
            print("perimeter of Rectangle =",peri.rectangle(lk,lp),'Cm')
        elif opt ==3:
            le = float(input("Enter the radius(Cm):"))
            print("perimeter of circle =",peri.circle(le),'Cm')
        elif opt ==4:
            mk = float(input("Enter first side (Cm):"))
            lp = float(input("Enter second side (Cm):"))
            lk = float(input("Enter the third side (Cm):"))
            print("perimeter of triangle =",peri.triangle(mk,lp,lk),'Cm')

    elif choice ==4:
        print("""
                        <1> Cube              <6> Frustum of cone                                               
                        <2> Cuboid                                               
                        <3> Sphere                                                            
                        <4> Cylinder                                                       
                        <5> Hemisphere                                                     """)
            
        opt =int(input("Select Shape :"))
        if opt ==1:
            hu = float(input("Enter edge length (Cm):"))
            print("Volume of cube =",vol.cube(hu),'Cm')
        elif opt ==2:
            ki = float(input("Enter the length (Cm):"))
            lp = float(input("Enter the base (Cm):"))
            lo = float(input("Enter the heigth (Cm):"))
            print("Volume of cuboid =",vol.cuboid(ki,lp,lo),'Cm')
        elif opt ==3:
            kj = float(input("Enter the radius (Cm):"))
            print("Volume of sphere =",vol.sphere(kj),'Cm')
        elif opt ==4:
            kp = float(input("Enter the radius (Cm):"))
            lm = float(input("Enter the height (Cm):"))
            print("Volume of cylinder =",vol.cylinder(kp,lm),'Cm')
        elif opt ==5:
            nj = float(input("Enter the radius (Cm): "))
            print("Volume of hemisphere",vol.hemisphere(nj),'Cm')
        elif opt ==6:
            kl = float(input("Enter the upper radius (Cm):"))
            nj = float(input("Enter the base radius (Cm):"))
            hj = float(input("Enter the height (Cm):"))
            print("Volume of frustum of cone =",1/3*math.pi*hj*((kl*kl)+(nj*nj)+(kl*nj)))


    elif choice ==5:
        import table
        o=int(input('enter the number:'))
        table.multi(os)

    elif choice ==6:
        g = int(input("enter the number :"))
        if g%2==0:
            print(g,"is an even number -_-")
        else:
            print(g,"is an odd number -_-")

    elif choice ==7:
        l=list(input("Enter the list:"))
        for i in l:
            j = l.index(i)
            while (j<0):
                if l[j-1]>l[j]:
                    l[j-1],l[j]=l[j],l[j-1]
                else:
                    break
                    j=j-1

    elif choice ==8:
        n=0
        j=0
        while n==j:
            webbrowser.open('www.google.com')

    elif choice ==9:
        webbrowser.open('www.github.com/joshanjohn')   
        print(l)




        
