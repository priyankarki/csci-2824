# Write a Python function check_subset() that takes in two Python lists, representing sets of integers, A and B. 
# Your function should return a single Boolean (True or False) for whether or not either set is a subset of the other. 
# A and B are sets, and not necessarily non-empty.

def check_subset(A, B):
    if len(A) == 0 or len(B) == 0:
        return True
    return (set(B) < set(A))


# Write a Python function cardinality() that takes in three Python set objects, representing sets of between 0 and 50 
# integers, A, B, and U. Your function should return a single non-negative integer value for the 
# cardinality of the set below. A and B are subsets (not necessarily proper) of the universal set U.

# |P(A ∩ B)|, where A is A complement

# Note 1: You can copy-paste the code declaring the various visible test cases below. We strongly encourage you to do this 
# 	to test your code.
# Note 2: Your function should take in the sets in the order: A, B, U.

def cardinality(A, B, U):
    sub = A.difference(B)
    diff = U.difference(sub)
    l = len(diff)
    return (2**l)
