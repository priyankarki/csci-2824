Consider the recurrence relation an=n2an−1−an−2 with initial conditions a0=1 and a1=2. Write a Python 
function called sequence_slayer that takes a nonnegative integer argument N less than 50 and returns 
the N-th term in the sequence defined by the above recurrence relation. 
	def sequence_slayer(N):
	    x = []
	    x.append(1)
	    x.append(2)
	    
	    #from 2 to N, continue adding
	    for i in range(2, N+1):
	        x.append(((i**2)*(x[i -1])) - x[i-2])
	    
	    #return that N
	    return (x[N])

Write a Python function called first_D_digit_Lucas that takes an integer argument D less than 30 and returns 
the first D-digit Lucas number.
	def first_D_digit_Lucas(D):
	    x = []
	    x.append(2)
	    x.append(1)
	    i = 1
	    
	    # while the function is less than 10, 100, etc
	    # continue adding
	    while (x[i] <= (10**(D-1))):
	        i +=1
	        x.append((x[i -1]) + x[i-2])

	    #return the i-th one where it is greater
	    return (x[i])

Write a Python function called common_decency that takes a positive integer argument N and returns a Boolean 
(True/False) representing whether or not the input integer is a decent number.
	def common_decency(N):
	    count3 = 0
	    count5 = 0
	    
	    #see if has 3 or 5
	    if (N % 3 != 0) or (N % 5 != 0):
	        return False

	    x = str(N)
	    for i in range(len(x)):
	        if (x[i] == '3'):
	            count3 += 1
	        elif (x[i] == '5'):
	            count5 += 1
	    
	    #check counts of 3 and 5
	    if (count3 % 5 == 0) and (count5 % 3 == 0):
	        return True
	    else:
	        return False
