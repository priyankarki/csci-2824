Write a Python function ParityParty() that takes in a nonnegative integer 𝚍 and returns a list: the first element of the output list is a 0 if the number d is even, and 1 if d is odd, the second element of the output list is d/2 if d is even, and (d−1)/2 if d is odd.
	
	import array
	def ParityParty(d):
	    arr = []
	    if d%2 == 0:
	        arr.append(0)
	        arr.append(int(d/2))
	    else:
	        arr.append(1)
	        arr.append(int((d-1)/2))
	    return arr



Write a Python function DecToBin() that takes in a nonnegative integer 𝚍 and returns a Python list of 0's and 1's corresponding to the binary representation of 𝚍.  

	def DecToBin(d):
    arr = []
    if d == 0:
        arr.append(0)
    while (d != 0):
        if d % 2 == 0:
            arr.insert(0, 0)
            d = d/2
        else:
            arr.insert(0, 1)
            d = (d-1)/2
    return arr
