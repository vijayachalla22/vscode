import difflib
def string_similarity(s1, s2):
    result =  difflib.SequenceMatcher(a=s1.lower(), b=s2.lower())
    return result.ratio()

s1 = input("Enter 1st String : ")
s2 = input("Enter 2nd String : ")
sim = string_similarity(s1,s2)
print(f"{s1} , {s2} are similar by {sim*100} %")
# print()