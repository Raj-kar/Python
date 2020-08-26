def check_strength(password):
    upper_case = 0
    lower_case = 0
    numeric = 0
    special_char = 0
    total = 0

    for ch in password:
        if 'A' <= ch <= 'Z':
            upper_case += 1
        elif 'a' <= ch <= 'z':
            lower_case += 1
        elif '1' <= ch <= '9':
            numeric += 1
        else:
            special_char += 1

    total = upper_case + lower_case + numeric + special_char
    if total > 7 and upper_case >= 1 and lower_case >= 4 and numeric >= 2 and special_char >= 1:
        return True
    else:
        return False
