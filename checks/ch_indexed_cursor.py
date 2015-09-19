from scalint.indexed_cursor import IndexedCursor
from scalint.indexed_cursor import IndexedLoopCursor

ic = IndexedCursor( (1,2,3,4,5)  )

for i in xrange(0,ic.len() ):
    print ic.current_idx(), ic.current()
    ic.step_for()

ic.first()
print ic.current_idx(), ic.current()
ic.last()
print ic.current_idx(), ic.current()



ilc  = IndexedLoopCursor( IndexedCursor( (1,2,3,4,5)  ) )

for i in xrange(0,11):
    print ilc.current()
    ilc.step_for()


