class ModAdd:
    def __init__(self,mod,id):
        self.in1 = None
        self.in2 = None
        self.out = None
        self.mod = mod
        self.id = id

    @classmethod
    def noparam(cls):
        mod = None
        id = None
        return cls(mod,id)

    def clock(self):
        assert self.id !=None, f"ModAdd id is invalid"
        assert self.in1!=None, f"in1 is invalid @ ModAdd id:{self.id}"
        assert self.in2!=None, f"in2 is invalid @ ModAdd id:{self.id}"
        assert self.mod!=None, f"mod is invalid @ ModAdd id:{self.id}"
        self.out = (self.in1 + self.in2)%self.mod
    
        

