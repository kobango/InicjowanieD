import numpy
size = [30,30]
minenumber = 30
raw = []
raw[0:size[0],0:size[1]] = '1'

raw[1:size[1]-1,1:size[1]-1] = '.'
mines = numpy.random.randint(1,size[1]-1,[minenumber,2])
i = 0
print (mines)
print (mines[1])
while i <minenumber:
    raw[mines[i][0],mines[i][1]] =1
    i= i+1

raw[numpy.random.randint(3,size[1]-3),numpy.random.randint(2,size[1]/2)] = 'P'




print (raw)
print (mines)

numpy.savetxt('test.txt', raw, delimiter=" ", fmt="%s")

