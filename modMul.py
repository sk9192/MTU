class ModMul:
    
    def __init__(self,mod,id):
        self.in1 = None
        self.in2 = None
        self.out = None
        self.mod = mod
        self.id = id

    @classmethod
    def noparam(self):
        self.in1 = None
        self.in2 = None
        self.out = None
        self.mod = None
        self.id = None
    
    def clock(self):
        assert self.in1!=None, f"in1 is invalid @ ModMul id:{self.id}"
        assert self.in2!=None, f"in2 is invalid @ ModMul id:{self.id}"
        assert self.mod!=None, f"mod is invalid @ ModMul id:{self.id}"
        self.out = (self.in1 * self.in2)%self.mod