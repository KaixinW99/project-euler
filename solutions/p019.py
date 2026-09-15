"""Project Euler Problem 19: Counting Sundays

https://projecteuler.net/problem=19
(Copied verbatim from project_euler.ipynb, cell 19.)
"""

# Problem 19: Counting Sundays
# a normal year has 4*30+7*31+28=365 days, but leap year 366 days 
def spec_day(e):
    s=1900
    mon_1st=[1] # 1900/01/01 is Monday
    norm = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    while s<=e:
        if s%100==0 and s%400==0:
            for x in leap:
                mon_1st.append(mon_1st[-1]+x)
        elif s%100!=0 and s%4==0:
            for x in leap:
                mon_1st.append(mon_1st[-1]+x)
        else:
            for x in norm:
                mon_1st.append(mon_1st[-1]+x)
        s+=1
    return mon_1st
#print(spec_day(2000))
l_day = spec_day(2000)
for x in spec_day(1900):
    l_day.remove(x)
l_spec_day=[x for x in l_day if x%7==0]
print(len(l_spec_day))
