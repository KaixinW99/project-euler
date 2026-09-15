"""Project Euler Problem 39: Integer right triangles

https://projecteuler.net/problem=39
(Copied verbatim from project_euler.ipynb, cell 39.)
"""

# Problem 39: Integer right triangles
""" triangle rule(a+b>c) & non-repetition: a<b<c -> a<p/3 and a<b
    (a^2+b^2=c^2) a and b are odd -> c even -> p even
    (a^2+b^2=c^2) either a or b is odd -> c odd -> p even
    (a^2+b^2=c^2) a and b are even -> c even -> p even
    take a+b+c=p and (a^2+b^2=c^2) together"""
def RightTriangle(p):
    num, triangle_list=0,[]
    for a in range(1,int(p/3)):
        maybe = (p*p-2*p*a)/(2*(p-a))
        if (p*p-2*p*a)%(2*(p-a))==0 and a<maybe:
            b = int(maybe)       
            c = int(p-a-b)
            triangle_list.append((a,b,c))
            num+=1
    return num, triangle_list

if __name__=="__main__":
    num_list=[]
    for p in range(12,1000,2):
        num, trilist = RightTriangle(p)
        #print(num,trilist)
        num_list.append((p,num))
    print(max(num_list,key=lambda m: m[1]))
    print(max(num_list,key=lambda m: m[1])[0])
