txt = """""value":0.10042671494995892"""
txt2 = """""value":0.80042671494995892"""
txt3 = """""value":0.42680770292345938"""
txt4 =  """""value":0.68400704549073121"""
def spliting (txt):
    x = txt.split(':')
    zeta = float(x[1])
    return (zeta)

def windowmake(walue):
    warray = [walue,walue,walue,walue,walue]
    return warray
def windowpeek(window,walue):
    window.append(walue)
    window.pop(0)
    return window

walue = spliting(txt)
walue2 = spliting(txt2)
array = windowmake(walue)
print(array)
array = windowpeek(array,walue2)
print(array)
array = windowpeek(array,walue2)
print(array)
array = windowpeek(array,walue2)
print(array)
