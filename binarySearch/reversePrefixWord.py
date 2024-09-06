def reversePrefix(s:str, ch:str) -> str:
    # idx = s.find(ch) + 1
    # ans = s[:idx][::-1] + s[idx:]

    for i in range(len(s)):
        if s[i] == ch:
            break
    ans = s[:i+1][::-1]+s[i+1:]
    print(ans)
    return ans

word = "abcdefd"
ch = "d"
#Output: "dcbaefd"
word1 = "xyxzxe"
ch1 = "z"
#Output: "zxyxxe"
reversePrefix(word, ch)
reversePrefix(word1,ch1)