def capitalized(s):
    s = s.split(" ")
    return " ".join(s[0][0].upper())


print(capitalized("jon jones"))
