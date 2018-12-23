Write a Python function filterFun to classify an input message as spam or ham (not spam). In class, we went 
over how Bayes' theorem can be used to obtain probabilities for a given message being spam or ham, based on the 
presence of particular words. Here, we will do a simpler example based on numbers instead of words. Similarly to 
the example in class, we will assume that numbers are conditionally independent, given the class (spam/ham) of email.

Input:
  message - a list of integers of length at least 1 and at most 100. This is the message we must classify as spam or ham.
  spam - a list of lists of integers that corresponds to messages we have classified as spam.  Each sub-list corresponds to 
    a different message, all of which are known to be spam. Length of spam will be at least 1.
  ham - a list of lists of integers that corresponds to messages we have classified as ham.  Each sub-list corresponds to 
    a different message, all of which are known to be ham. Length of ham will be at least 1.
  Only consider each number once; do not double count if a number is repeated within a message.

Output:
  Boolean (True/False) for whether the input message should be classified as spam. This should be based only on whether 
  the message is more or less likely to be spam than ham. In the event of a tie, classify the message as spam.

	def filterFun(message,spam,ham):
	    numMessage = len(message)
	    numSpam = len(spam)
	    numHam = len(ham)
	    
	    totalMessage = numMessage + numSpam + numHam
	    probS = numSpam / totalMessage
	    probHam = numHam / totalMessage
	    cSpam = 1
	    cHam = 1
	    
	    for i in message:
	        spamNum = count(i, spam)
	        cSpam = cSpam * (spamNum/numSpam)
	        hamNum = count(i, ham)
	        cHam = cHam*(hamNum/numHam)
	    
	    if cSpam >= cHam:
	        return True
	    else:
	        return False
        
	def count(check, spam):
	    num = 0
	    for i in spam:
	        i = list(set(i))
	        for j in i:
	            if j == check:
	                num += 1
	    return num

Write a Python function binom_product that takes integer arguments a and b and positive integer argument n and returns 
the product of the coefficients in the expansion of (ax+by)^n.
	def fact(n):
	    a = 1
	    for i in range(2, n+1):
	        a *= i
	    return a
	    
	def binom_product(a,b,n):
	    pro = 1
	    for k in range(0, n+1):
	        pro *= ( fact(n) / ( fact(n-k)* fact(k) ) )* pow(a, n-k) * pow(b,k)
	    return pro
    
Write a Python function mega_digit that takes positive integer arguments N and k and returns the "mega digit" of P = the 
number N repeated k times.

For example, if N=123 and k=3, then your function should return the mega digit of P=123123123.

What is a "mega digit" you ask?  Great question!

If P is a single digit (1≤P≤9), then the mega digit of P is equal to P.
If P is more than one digit (P≥10), then the mega digit of P is equal to the mega digit of the sum of the digits of P.
	
  def mega_digit(n, k):
	    total = 0
	    while n > 0:
	        total += n%10
	        n //= 10
	    total *= k
	    if total < 10:
	        return total
	    else:
	        return mega_digit(total, 1)
