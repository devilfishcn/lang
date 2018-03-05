# -*- coding: utf-8 -*-


class ObjectDict(dict):
    """Makes a dictionary behave like an object, with attribute-style access.
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value
        
        
        
class LoanUser(ObjectDict):
    '''
    通常情况下loanuser的属性为：age,birth,mobile,sex,name等五项内容
    '''
    pass

class DBRecord(ObjectDict):
    pass
