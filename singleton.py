class mysingleton(object):
    _instance=None
    def __new__(self):
        if not self._instance:
            self._instance= super(mysingleton,self).__new__(self)
            self.y=10
        return self._instance
x=mysingleton()
print (x.y)
x.y=20
z=mysingleton()
print (z.y)
