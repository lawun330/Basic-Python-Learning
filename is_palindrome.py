'''Palindrome is a string that can be read from left to right or right to left.
This script uses a function to check if a string is a palindrome.'''

def is_palindrome(input_string):
	# create two strings, to compare them
	new_string = ""
	reverse_string = ""
	
	# traverse through each letter of the input string
	for letter in input_string:
		# add any non-blank letters to the end of one string, and to the front of the other string.
		if letter != " ":
			new_string += letter.lower()
			reverse_string = letter.lower() + reverse_string
	
	# compare the strings
	if new_string == reverse_string:
		return True
	
	return False

# example
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print(is_palindrome("rador")) # Should be False
