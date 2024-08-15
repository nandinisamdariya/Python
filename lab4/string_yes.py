def check_yes(s):
    if s.lower() == "yes":
        return "Yes"
    else:
        return "No"

s = input("Enter a string: ")
print(check_yes(s))
