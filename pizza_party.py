# Identify whether p=64 or not
# If p<64,
# keep calculating...
# If p=64,
# print the result.
n=0
p=1
sen=''
# determine the initial value of n and p
while p<=64:
	p=(n**2+n+2)/2
	sen=sen+str(n)+" "
	n=n+1
print(sen)
