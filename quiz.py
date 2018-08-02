score = 0

print("For this quiz you need to type, A, B, or C")

print("\nQ1.  What is the tallest mountain in the world?")
print("A.  Mount McKinnely")
print("B.  Mount Everest")
print("C.  K2")

answer = input()

if answer == "B" or answer == "b":
	print("Great job, you got it right!")
	score = score + 1
else:
	print("Sorry, you got that incorrect.  The correct answer was B.")	
print("Your score is", score)

print("\nQ2.  What is the smallest country in the world?")
print("A.  Kuwait")
print("B.  Ireland")
print("C.  Vatican City")

answer2 = input()

if answer2 == "C" or answer2 == "c":
	print("Great job, you got it right!")	
	score = score + 1
else:
	print("Sorry, you got that incorrect.  The correct answer was B.")	
print("Your score is", score)	