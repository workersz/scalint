""" cursors with index support data """

class IndexedCursor(object):
    def __init__(self,indexable):
        if '__getitem__' not in dir(indexable):
            raise TypeError('storage not indexable')
        self.__o = indexable
        self.__i = 0
        self.__l = len(self.__o)
        self.__il = self.__l - 1

    def __len__ (self ):
        return self.__l

    def len(self):
        return self.__l

    def len_idx(self ):
        return self.__il

    def current(self):
        return self.__o[self.__i]

    def current_idx(self):
        return self.__i

    def step_for(self):
        self.__i+=1

    def step_back(self):
        self.__i-=1

    def forward(self,cnt):
        self.__i+=cnt

    def backward(self,cnt):
        self.__i-=cnt

    def first(self):
        self.__i=0

    def last(self):
        self.__i = self.__il


class IndexedLoopCursor():
    """ cursor that just loop over index """
    def __init__(self, cursor):
        self.__c = cursor
  
    def len(self):
        return self.__c.len()

    def len_idx(self):
        return self.__c.len_idx()

    def current_idx(self):
        return self.__c.current_idx()

    def current(self):
        return self.__c.current()
    
    def step_for(self):
        if self.__c.current_idx()  >= self.__c.len_idx():
            self.__c.first()
        else:
            self.__c.step_for()

    def step_back(self):
       if self.__c.current_idx() <= 0:
           self.__c.last()
       else:
           self.__c.step_back()




