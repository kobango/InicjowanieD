txt = """""{value":0.10042671494995892}"""
txt2 = """""{value":0.80042671494995892}"""
txt3 = """""{value":0.42680770292345938}"""
txt4 =  """""{value":0.68400704549073121}"""
txt5 = """""{status":"Stopped}"""
def spliting (txt):
    x = txt.split(':')
    x = x[1]
    x = x[1:len(x)-1]
    zeta = float(x)
    return (zeta)

def windowmake(walue):
    warray = [walue,walue,walue,walue,walue]
    return warray

def windowpeek(window,walue):
    window.append(walue)
    window.pop(0)
    return window

def iscorect(txt):
    status =True
    if("Stopped"in txt):
        status = None
    else:
        status=True
    return  status
def windowmean(array):
    sum = 0
    for i in array:
        sum =sum + i
    mean = sum/len(array)
    return mean

def makenum(rawarray):
    array = []

    for i in rawarray:

        if(iscorect(i)):
            array.append(spliting(i))
    return array

def addnum(array,rawtxt):
    if(iscorect(rawtxt)):

        value = spliting(rawtxt)
        array = windowpeek(array,value)
    return  array







walue = spliting(txt)
walue2 = spliting(txt2)
array = windowmake(walue)
print(array)
array = windowpeek(array,walue2)
print(array)
print(windowmean(array))
array = windowpeek(array,walue2)
print(array)
array = windowpeek(array,walue2)
array = addnum(array,txt5)
print(array)
print(windowmean(array))
