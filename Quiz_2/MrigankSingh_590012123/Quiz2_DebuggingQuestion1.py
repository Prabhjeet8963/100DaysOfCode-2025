# Correct answer is A) Empty string should return False since it contains no digits.

#Correct Code:
def is_digits_only(s):
    if len(s) == 0:
        return False
    for char in s:
        if char < '0' or char > '9':
            return False
    return True