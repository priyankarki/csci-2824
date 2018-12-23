Write a Python function treasure_hunt that takes as arguments positive integers m, n and p and returns the 
number of valid configurations of the m×n grid world that follows the following rules:
  The "world" has m columns and n rows in it. There is one knight, one treasure chest and p≥0 dragon(s) in the grid-world.
  Dragons cannot share a square with anything else. The knight can share a square with anything. 
  Dragons are indistinguishable from one another.
  
	def treasure_hunt(m,n,p):
	    drag = p
	    squares = m*n
	    remaining = squares
	    dChoice = squares
	    mult = drag
	    if p == 0:
	        return remaining*remaining
	    else:
	        while p != 1:
	            p = p - 1
	            mult = p*mult
	        while drag != 0:
	            drag = drag - 1
	            remaining = remaining - 1
	            if drag != 0:
	                dChoice = dChoice*remaining
	        return int(dChoice*remaining*remaining/mult)

Write a Python function wrangle_rectangles that takes as arguments positive integers m and n and returns the 
number of distinct, non-degenerate rectangles in an integer grid with vertical lines at x=0,1,…,m and horizontal 
lines at y=0,1,…,n. 
	def wrangle_rectangles(m,n):
	    horiz = n +1
	    vert = m+1
	    return int((m*n*horiz*vert)/4)
