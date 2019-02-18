def large_palindrome():
	a = 999
	b = 999
	
	for x in range(999):
	    for y in range(999):
	        c = a*b
	        c = str(c)
	        if c == c[::-1]:
	            return c
            b-=1
        a-=1
	

print(large_palindrome())  
