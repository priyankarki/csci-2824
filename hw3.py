Write a Python function D(i,n) that takes as input i and n, and returns a single logical value (True or False) 
representing the truth value of D(i,n).
	def D(i,n):
    A = [4, 8, 15, 16, 23, 42]
    
    if(A[i] % n == 0):
        return True
    else:
        return False

Write a Python function ABCs that takes in two lists of the same length, 𝚕𝚎𝚝𝚝𝚎𝚛𝚜 and 𝚗𝚞𝚖𝚋𝚎𝚛𝚜, and returns a single 
logical value (True or False) representing the truth value of the following proposition.
	def ABCs(letters, numbers):
    out = False
    vowels = ['A','E','I',"O",'U','Y']
    for i in range(len(letters)):
        if(numbers[i] % 2 == 0):
            if letters[i] in vowels:
                out = True
    return out

Write a function 𝚌𝚑𝚎𝚌𝚔_𝚙𝚛𝚘𝚙𝚘𝚜𝚒𝚝𝚒𝚘𝚗 that takes as its sole argument a Python list of between 0 and 50 integers and returns 
a boolean (i.e. 𝚃𝚛𝚞𝚎 or 𝙵𝚊𝚕𝚜𝚎)  representing the truth value of the the proposition ∀x[E(x)→∃y(x=2y)], where here the 
proposition E(x) means "x is even" and the list of integers is the domain for x and y.
	def check_proposition(numbers):
    out = True
    for i in numbers:
        if (i % 2 == 0):
            y = i/2
            if (y not in numbers):
                out = False
    return out
