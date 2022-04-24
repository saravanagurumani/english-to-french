fo = open('t8.shakespeare.txt', 'r')
for x in fo.read():
    y = x.lower()
    fo1 = open('write.txt', 'a')
    fo1.write(y)
	
	