
#Solution 2:
s = list(input())
t = list(input())
 
for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        s[i] = 'a'
    else:
        s[i] = chr(ord(s[i]) + 1)
        break
 
print(''.join(s) if s != t else "No such string")
"""
Solution 1:

s = list(map(ord, list(input())))
t = list(map(ord, list(input())))

for i in range(len(s)):
  s[i] = s[i] - ord("a") + 1
for i in range(len(t)):
  t[i] = t[i] - ord("a") + 1
##
for i in range(len(s) - 1, -1, -1 ):
	if s[i] == 26:
		s[i] = 1
	else:
		s[i] += 1
		break
def compare(s,t):
	for i in range(len(s)):
		if s[i] == t[i]:
			continue
		else: return s[i] < t[i]
  
if compare(s,t) == True:
	for i in range(len(s)):
		s[i] = chr(s[i] + ord("a") - 1)
	print("".join(s))

else:
  print("No such string")
  
"""
  

     
    
