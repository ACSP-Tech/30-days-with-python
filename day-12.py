# Day 12/30 days with Python

# String Methods



# isalpha Method
only_letter = "abcde"
print('Only Letter: ', only_letter.isalpha())

has_letter = "123mn4"
print('Has Letter: ', has_letter.isalpha())

no_letter = "1234"
print('No Letter: ', no_letter.isalpha())


# isspace Method
print('\n\n===== IsSpace Method ====')

only_space = "   "
print('Only Space: ', only_space.isspace())

has_space = "12  3"
print('Has Space: ', has_space.isspace())

no_space = "abcd"
print('No Space: ', no_space.isspace())


# isalnum Method

print('\n\n===== isalNum Method ====')

only_digits = "1234"
print('Only Digits: ', only_digits.isalnum())

only_letters = "abcdefg"
print('Only Letters: ', only_letters.isalnum())

has_digit = "1234@"
print('Has Digit: ', has_digit.isalnum())

has_letter = "instincthub"
print('Has letter: ', has_letter.isalnum())

has_digits_letters = "123instincthub32"
print('Has Digits Letters: ', has_digits_letters.isalnum())

no_digits_letters = "@ @ @ @ $ !"
print('No Digits Letters: ',no_digits_letters.isalnum())







