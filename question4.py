it_companies.add('Twitter')
print(it_companies)
it_companies1={'TCS', 'Wipro','Infosis'}
it_companies.update(it_companies1)
it_companies.remove('Google')
print(it_companies)
""" 
Python set remove () method searches for the given element in the set and removes it.  In discard () method, if the element is not present in the set, it does not throw any exception, wherein remove () method if the element is not present in the set, it throws an exception."""
C = A.union(B)
print(C)
A.intersection_update(B)
print(A)
print(A.issubset(B))
# A is subset of B
print(A.isdisjoint(B))
# A and B are not disjoint sets
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
print(len(age))#len of list
s = set(age)
print(s)
print(len(s))#len of list converted to set 
