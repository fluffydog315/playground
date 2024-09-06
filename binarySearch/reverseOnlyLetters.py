def reverseLetters(s:str) -> str:
    letters = [i for i in s if i.isalpha()]
    #print(letters)
    ans = []
    for c in s:
        if c.isalpha() :
            ans.append(letters.pop())
        else:
            ans.append(c)
    print("".join(ans))
    return "".join(ans)

s = "ab-cd"
reverseLetters(s)
s1 = "a-bC-dEf-ghIj"
reverseLetters(s1)
#Output: "j-Ih-gfE-dCba"