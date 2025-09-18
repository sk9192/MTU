from modAdd import ModAdd
from modMul import ModMul

class PE:
    def __init__(self,mod,id): 
        self.add = ModAdd(mod,id)
        self.mul = ModMul(mod,id)
        self.id = id
        assert self.add != None, "PE FAIL @ init : add unit NULL"
        assert self.mul != None, "PE FAIL @ init : mul unit NULL"
        assert self.id != None, "PE FAIL @ init : id NULL"
    def clock(self):
        assert self.add != None, "PE #{self.id} has a modAdd of NULL"
        assert self.mul != None, "PE #{self.id} has a modMul of NULL"
        self.add.clock()
        self.mul.clock()

