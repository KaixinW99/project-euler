"""Project Euler Problem 85: Counting rectangles

https://projecteuler.net/problem=85
(Copied verbatim from project_euler.ipynb, cell 85.)
"""

# Problem 85: Counting rectangles
# ! Math: The choices of the row (1+2+...+r); Th choices of the column (1+2+...+c); Total num = (1+2+...+r)*(1+2+...+c)
def counting_rect(x,y): return x*(1+x)*y*(1+y)/4    # That is always even
total = int(2e6)
xrang = int((total*4)**0.25)
yrang = lambda x: int((total*4/x/(1+x))**0.5)
diff_dict = {}
for x in range(1,xrang):
    for y in range(yrang(x)-3,yrang(x)+3):
        diff_dict.update({(x,y):counting_rect(x,y)-total})
sort_diff = sorted(diff_dict.items(),key=lambda x: abs(x[1]))
xc, yc = sort_diff[0][0]
print(xc*yc)
