s1 = input("Enter String 1 = ")
s2 = input("Enter String 2 = ")
L_1 = []
L_2 = []
for i in range(0, len(s1)):
    L_1.append(s1[i].lower())
for i in range(0, len(s2)):
    L_2.append(s2[i].lower())
if L_1 == L_2:
    print("They are Anagram")
else:
    print("They are not Anagram")
