# Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.

vowel_or_consonant = lambda letter : True if letter.lower() in "aeiou" else False

letter = input("\n Input a letter of the alphabet: ")

if(vowel_or_consonant(letter)):
	print(f"\n {letter} is a vowel.")
else:
	print(f"\n {letter} is a consonant.")


# Input a letter of the alphabet: k
#  k is a consonant.


#  Input a letter of the alphabet: a
#  a is a vowel.