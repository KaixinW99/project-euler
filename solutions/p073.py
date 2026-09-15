"""Project Euler Problem 73: Counting fractions in a range

https://projecteuler.net/problem=73
(Copied verbatim from project_euler.ipynb, cell 73.)
"""

# Problem 73: Counting fractions in a range
def num_farey_sequence(n: int, startn: int, startd: int, endn: int, endd: int) -> int:
    """ The detailed algorithm of next term is https://en.wikipedia.org/wiki/Farey_sequence """
    a, b, c, d=startn,startd,(startn*n)//startd,n-1 
    # This one only works when figuring out the closest fraction; e.g., 1/3 and 4000/11999 with 12000 boundary
    result = 0
    while not ((c==endn) and (d==endd)):
        result+=1
        k = (n+b)//d
        a,b,c,d=c,d,int(k*c-a),int(k*d-b)
    return result
if __name__=="__main__":
    print(num_farey_sequence(12000,1,3,1,2))
