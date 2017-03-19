def singleton(myClass):
    instances ={}
    def getInstance(*args,**kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args,**kwargs)
        return instances[myClass]
    return getInstance

@singleton    #decorator
class TestClass(object):
    pass

x=TestClass()
