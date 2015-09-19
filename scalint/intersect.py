""" scalar sets intersection """


class Intersect(object):
    """ scalar set intersector callable """
    def __init__(self, sets_cursor=None, comparator=None, result_handler=None):
        if sets_cursor is None:
            raise ValueError("sets_cursors is None")
        if comparator is None:
            raise ValueError("comparators is None")
        if result_handler is None:
            raise ValueError("result_handler is None")
 
        self.sets_cursor = sets_cursor #"expect is loop cursor of cursors"
        self.cmpr = comparator 
        self.eq_cnt = 0
        self.sets_cnt = sets_cursor.len()
        self.result_handler = result_handler
        self.result_candidate = None
       
    def __call__(self):
        sets_cursor = self.sets_cursor
        cmpr = self.cmpr
        #"init"
        max_item =  sets_cursor.current().current()
        self.result_candidate = max_item
        sets_cursor.step_for()
        while True:
            item =  sets_cursor.current().current()
            rc = cmpr(item,max_item)
            if rc == cmpr.LT:
                #"move x" 
                sets_cursor.current().step_for()
            if rc == cmpr.GT: 
                #"move y"
                max_item = item
                sets_cursor.step_for()
            if rc ==  cmpr.EQ:
                #"eq move y"
                rcr = cmpr( self.result_candidate, max_item )
                if rcr == cmpr.EQ:
                    self.eq_cnt+=1
                    #
                else:
                    self.eq_cnt =0 
                    self.result_candidate = max_item
                # 
                if self.eq_cnt == sets_cursor.len():
                    self.result_handler.on_result(self,item)
                    i = 0
                    while i < sets_cursor.len_idx():
                        sets_cursor.current().step_for()
                        sets_cursor.step_for()
                        i+=1
                    self.eq_cnt = 0
                #"move y after eq"
                sets_cursor.step_for()

