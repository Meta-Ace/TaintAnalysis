inputs_am = [5, 19, 30]
inp = ["a","b", "c"]
out = ["d"]

def orderInputs(inputs):
    inputs.sort(reverse=True)
    return inputs;

def prevTaint(prevArr, i):
    prev = prevArr[i]
    return prev;

def calcTaint(arr, taint):
    
    taintArr = []
    top_bott_taint = 0
    
    if len(arr) == 0:
        return;
    
    if len(arr) == 1:
        taintArr = [100]
        return
    
    if len(arr) == 2:
        taintArr = [50,50]
        return;
    
    if len(arr) > 2:
        top_bott_taint = (taint * .7)/2
        taintArr.append(top_bott_taint)
        leftover = (taint * 0.3) / (len(arr) - 2)
        while len(taintArr) <= (len(arr) - 2):
            taintArr.append(leftover)
        taintArr.append(top_bott_taint)
        print(taintArr)
        
    return taintArr;

#global variables
taint = 100
i = 0
j = 0
inputs = orderInputs(inputs_am)

# tester method when inputs are 3 or higher, otherwise use base cases 
# wip - handle multiple flows

#driver/tester
while j < len(inp):
    print(inputs)
    taint = prevTaint(calcTaint(inputs, taint), 0)
    j += 1
