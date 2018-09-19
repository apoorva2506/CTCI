def isOneEdit(str1,str2):
	cnt=0
	if len(str1)-len(str2)>1:
		print("strings of unequal length")
	elif len(str1)-len(str2)==1:
		
		# for i,j in zip(range(0, len(str1)),range(0, len(str2))):
		# 	print(i)
		# 	print(j)
		# 	j=1
		# 	print(str1[i] + " " + str2[j-1])
		# 	if str1[i]!=str2[j] and cnt < 1:
		# 		cnt+=1
		# 		j=j-1
		# 		print("not equal")
		# 	elif str1[i]==str2[j-1] and cnt == 1:
		# 		cnt+=1
		# 		print("true")
		# 	else:
		# 		print("oops")
			# Dont use for loop as index xhanging is tough in for loops, use while
		i=0
		j=0
		while i < len(str1) and j < len(str2):
			# print(i)
			# print(j)
			# print(str1[i] + " " + str2[j])
			if str1[i]!=str2[j] and cnt < 2:
		 		cnt+=1
		 		i=i+2
		 		j+=1
		 		print("not equal")
		 	elif str1[i]==str2[j]:
				cnt+=1
				i+=1
				j+=1
				print("true")
			else:
				i+=1
				j+=1
				print("False")

	elif len(str1)==len(str2):
		i=0
		j=0
		while i < len(str1) and j < len(str2):
			# print(i)
			# print(j)
			# print(str1[i] + " " + str2[j])
			if str1[i]!=str2[j] and cnt < 2:
		 		cnt+=1
		 		i=i+2
		 		j+=1
		 		print("not equal")
		 	elif str1[i]==str2[j]:
				cnt+=1
				i+=1
				j+=1
				print("true")
			else:
				i+=1
				j+=1
				print("False")


obj=isOneEdit("pale","pam")
#print(obj)
			
