str ='apoorva'
newlist=[]
for i in list(str):
	if i not in newlist:
		newlist.append(i)
	else:
		print("already exists")
