#askisi me agroth kai provata

a=[1,2,3]
b=[1,1,1,1,1]
c=[2,3]
d=[4,1]

suma=sumb=sumc=sumd=0

for num in a
	suma += num
	
for num in b
	sumb += num
	
for num in c
	sumc += num
	
for num in d
	sumd += num
	
newlist=[suma,sumb,sumc,sumd]

max(newlist)
min(newlist)

print max(newlist)-min(newlist)
