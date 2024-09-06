def reverseW(s:str) -> str:
    input = s.split(" ")
    ans  = [words[::-1] for words in input]
    print(ans)
    return ans

s = "Let's take LeetCode contest"
reverseW(s)

s2 = "God Ding"
reverseW(s2)