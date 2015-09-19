""" scalar compartor generics """
class Comparator(object):
    """ generic bi-relational scalar comparation function
        generic protocol
        lower LT, greater GT, equal EQ
        constants LT  EQ  GT   UNKNOWN 
        codes,   1 <, 3==, 5>, 6 err
    """
    LT   = 1
    EQ   = 3
    GT   = 5
    UNKNOWN  = 6 #in case when impl don't know

    def __init__(self, *args, **kwargs ):
        # init when needed
        pass

    def __call__( self, a, b ):
        # default behaviour
        return Comparator.UNKNOWN

# why
class NativeComparator(Comparator):
    """ native python comparator """
    def __call__(self, a, b ):
        if a < b: return Comparator.LT 
        elif a > b: return Comparator.GT
        else: return Comparator.EQ






