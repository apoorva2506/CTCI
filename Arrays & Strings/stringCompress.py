str1="aaaabbbbbcckkrrr"
comp_word=""

if len(str1) == 0:
	print("0 length")
if len(str1) == 1:
    print(str1 + "1")

cnt=1
i=1

while i < len(str1):
	#print str1[i]
	if str1[i]==str1[i-1]:
		cnt+=1


	else:
		comp_word+= str1[i-1]+str(cnt)
		cnt=1

	i+=1

comp_word+= str1[i-1]+str(cnt)
print(comp_word)
	

	



