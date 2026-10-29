# not True is False, and False and False is False
print(not True and False)  # False

# and is evaluated before or, so False and False is False;
# True or False is True
print(True or False and False)  # True

# 5 is greater than 3, so not True becomes False
print(not (5 > 3))  # False

# 10 == 10 is True, but 4 != 4 is False;
# True and False is False
print(10 == 10 and 4 != 4)  # False

# not False is True, and not True is False;
# True or False is True
print(not False or not True)  # True
