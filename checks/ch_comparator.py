
from scalint.scalar_comparator import NativeComparator


cmpr = NativeComparator()

#simple checks for native py comparsion numerical and tuples

assert cmpr(1,3) == cmpr.LT
assert cmpr(2,2) == cmpr.EQ
assert cmpr(3,1) == cmpr.GT


assert cmpr( (1,1), (1,3) ) == cmpr.LT
assert cmpr( (2,2), (2,2) ) == cmpr.EQ
assert cmpr( (3,1), (2,1) ) == cmpr.GT


assert cmpr( (1,) , (1,3) ) == cmpr.LT
assert cmpr( (1,3), (1,3)  ) == cmpr.EQ
assert cmpr( (1,1,1), (1,1) ) == cmpr.GT
