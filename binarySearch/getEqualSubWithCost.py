#leetcode 1208
def getEqualSubWithCost(s:str, t:str, maxCost:int) -> int:

    curr, left, ans = 0, 0, 0
    for i in range(len(s)):
        curr += abs(ord(s[i]) - ord(t[i]))

        while curr > maxCost:
            curr -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        ans = max(0, i - left + 1)
    
    print(ans)
    return ans

s = "abcd" 
t= "bcde"
buget = 3

getEqualSubWithCost(s,t,buget)

    