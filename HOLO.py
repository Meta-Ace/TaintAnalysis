inputs_am = [5,7,8, 5, 7, 5, 3, 4, 10, 23, 47]

def orderInputs(inputs):
    inputs.sort(reverse=True)
    print(inputs)
    return inputs;

def calcTaint(arr):
    
    taint = 100
    taintArr = []
    top_bott_taint = 0
    
    if len(arr) == 0:
        return;
    if len(arr) > 2:
        top_bott_taint = (taint * .7)/2
        taintArr.append(top_bott_taint)
        leftover = (taint * 0.3) / (len(arr) - 2)
        while len(taintArr) <= (len(arr) - 2):
            taintArr.append(leftover)
        taintArr.append(top_bott_taint)
        print(taintArr)
        
    return;

calcTaint(orderInputs(inputs_am))
