#leetcode 1456
def maxVowels(s:str, k:input) -> int:
    ans = 0
    curr = 0
    left = 0
    vos = {'a','e','i','o','u'}
    for i in range(k):
        if s[i] in vos:
            curr +=1 
    
    print(curr)
    
    for j in range(k, len(s)):
        print(left, j)
        curr -= 1 if s[left] in vos else 0
        curr += 1 if s[j] in vos else 0
        ans = max(curr, ans )
        left += 1
    
    print(ans)
    return ans

# s = "abciiidef"
# k = 3

# s = "aeiou"
# k = 2


s = "leetcode"
k = 3

maxVowels(s,k)
