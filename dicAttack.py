
dictionayFile = open("dictionary.txt","r")
inDictionary = False

print("Can your password survive a dictionary attack?")

test_password = input("Type in a trial password: ")

for line in dictionaryFile :
	if line.strip() ==test_password.strip():
		inDictionary= True
		print("oh no. you need to work on that. Match found for: ", line.strip())
		break
		

if not inDictionary:
	print("Good job! No match found")