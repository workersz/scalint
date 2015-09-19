from scalint.scalar_comparator import NativeComparator
from scalint.indexed_cursor import IndexedCursor as IC
from scalint.indexed_cursor import IndexedLoopCursor as ILC
from scalint.intersect import Intersect

sets_cursor = ILC( IC ( (
IC ( ( 1,2,3,4,5,6,100,101,102,105 ) ), #0
IC ( (1,3,6,12,19,50,60,99,101,105 ) ),    #1
IC( (1,3,6,41,50,101,105) ), #2
IC( (1,3,6,8,9,10,11,12,50,51,90,101,105 )) #3
) ) )

expected_result =  [1, 3, 6, 101, 105]
comparator = NativeComparator()

class ResultHandler(object):
    def __init__(self):
        self.store=list()
    def on_result(self,intersector,item):
        self.store.append( item )


r_handler = ResultHandler()
sect = Intersect( sets_cursor= sets_cursor , 
                  comparator=comparator, 
                  result_handler=r_handler )

try:
    sect()
except Exception, e:
    if type(e) is IndexError:
        print "sect done"
        print r_handler.store
        assert expected_result == r_handler.store
    else:
        raise e    


