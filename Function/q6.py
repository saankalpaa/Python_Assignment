def check_range(num, lower_range, upper_range):
    if num in range(lower_range, upper_range):
        print("%s is in the range" % str(num))
    else:
        print("%s is outside the given range." % str(num))


check_range(12, 2, 21)
check_range(3, 4, 8)