inputs_am = [5, 19, 30, 31, 45, 56]
inp = ["a","b", "c","y","z", "aa"]
out = ["e", "e", "d", "e", "e"]
canAdd = []
taintArr = [4, 5, 10, 10, 10]


def sumOf(arr):
    num = 0
    i = 0
    while i < len(arr):
        num += arr[i-1]
        i+=1
    return num

#function to find any pairs // unfinished
def sameAddr(arrAddr, taintArr):
    i = 0
    # base item
    j = 0
    totTaint = []
    usedArrs = []
    a = 0
    # iterate through every item in the list
    while i < len(arrAddr):
        if j == i:
            j+=1
            a += j
        if arrAddr[i] == arrAddr[j]:
            a += taintArr[i]
            
            
    return
    

#check if neighboring addresses are the same
def sameAdd(arrAddr):
    i = 0
    sameAddr = False
    while i < len(arrAddr) - 1:
        if out[i] == out[i + 1]:
            sameAddr = True 
            canAdd.append(1)
            i+=1
        elif out[i] != out[i + 1]:
            sameAddr = False
            canAdd.append(0)
            i+=1
    print(canAdd)

#handle unordered lists        
def addCorrTaint(Addrs, taintArr):
    totTaint = []
    i = 0
    a = taintArr[0]
    while i < len(canAdd) - 1:
        if canAdd[i] == 1:
            a += taintArr[i+1]
            i+=1
        elif canAdd[i] == 0:
            totTaint.append(a)
            i+=1
            a = taintArr[i]
            totTaint.append(a)
            if canAdd[i] == 1:
                a += taintArr[i+1]
                totTaint.append(a)
                i+=1
            elif canAdd[i] == 0:
                totTaint.append(taintArr[i])
                i+=1
    if len(totTaint) == 0:
        totTaint.append(a)
    
    if i == len(canAdd) - 1:
        if canAdd[i] == 0:
            totTaint.append(taintArr[i])
        elif canAdd[i] == 1:
            if len(totTaint) == 0:
                a = taintArr[i + 1]
                totTaint[0] = a
            elif len(totTaint) != 0:
                a = totTaint[len(totTaint) - 1] + taintArr[i + 1]
                totTaint[len(totTaint) - 1] = a
    return totTaint;
                        

print(taintArr)
print(out)
sameAdd(out)
print(addCorrTaint(out, taintArr))
