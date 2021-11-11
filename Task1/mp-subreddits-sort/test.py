import bisect
a= []
bisect.insort_left(a,8)
bisect.insort_left(a,6)
bisect.insort_left(a,5)
c=bisect.insort_left(a,9)
print(a)
print(c)