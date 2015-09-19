""" cursors with index support data """

class IteratorCursor(object):
    def __init__(self,iterable):
        self.__o = iterable
        try:
            self.__it = iter(self.__o)
        except TypeError, e:
             raise TypeError('init obj not iterable')

        self.__i = 0
        self.__l = len(self.__o)
        self.__il = self.__l - 1
        self.__curr = self.__it.next()

    def __len__ (self ):
        return self.__l

    def len(self):
        return self.__l

    def len_idx(self ):
        return self.__il

    def current(self):
        return self.__curr

    def current_idx(self):
        return self.__i

    def step_for(self):
        self.__curr = self.__it.next()
        self.__i+=1

    def step_back(self):
        raise TypeError("method step_back is not supported")  

    def forward(self,cnt):
        #self.__i+=cnt
        raise TypeError("method forward is not supported")

    def backward(self,cnt):
        #self.__i-=cnt
        raise TypeError("method forward is not supported")

    def first(self):
        self.__it=iter(self.__o)
        self.__i = 0
        self.__curr = self.__it.next()
        

    def last(self):
        raise TypeError("method last is not supported") 






