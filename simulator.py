from modAdd import ModAdd
from modMul import ModMul
from PE import PE



#----------------------# 
def test_modAdd():
    test_add = ModAdd.noparam()
    test_add.id = 1
    test_add.in1 = 5
    test_add.in2 = 5
    test_add.mod = 2
    try:
        test_add.clock()
        print(f"test_add.out = ",test_add.out)
    except AssertionError as e:
        print(f"Error: {e}")

    test_add_parameter = ModAdd(1,2)
    print(f"mod for parameter add: ",test_add_parameter.mod)
    print(f"id for parameter add: ",test_add_parameter.id)

def test_PE():
    try:
        unit = PE(5,200)

        unit.add.in1=5
        unit.add.in2=5

        unit.clock()
    except AssertionError as e:
        print(f"Error: {e}")
    
def init_PE(mod,id,PE_Array):
    PE_Array.append(PE(mod,id))

def init_MTU(num_PE,PE_Array,mod):
    for i in range(0,num_PE):
        init_PE(mod,i,PE_Array)
        
#---------------------#

PE_Array=[]
init_MTU(4,PE_Array,5)
print("PE at index 3 has id: ",PE_Array[3].id)



