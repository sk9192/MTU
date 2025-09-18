from modAdd import ModAdd
from modMul import ModMul
from PE import PE


# note: we have to think about how to clock better
# unsure whether we should consider the sub modules to have a clock delay (register at either end)
# if we do: then it is easier to see the flow of data \ but cannot accurately asses the scheduling mechanics of the DFS Unit
# if we dont: then it is harder to see the flow of data (would need to inspect registers instead of being able to print at every computation (harder to see whats going on))
# it doesnt hurt to try both but we should think more about which one makes sense 
# ideally: works combinationally and models the scheduling mechanics of the DFS module (but were a while away from that lets get this part perfect)
# i think there should be both modes : 
# case 1: the register doesnt read the right value -> go to "testing mode", check where things are going wrong
# case 2: the register reads correctly -> move to next piece (but still nice to have this debug measurement)


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



