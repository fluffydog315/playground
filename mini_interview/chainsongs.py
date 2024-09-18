# Find the longest playlist
#chain condition: the last word is the first word in the list
from collections import defaultdict
def chainsongs(songs, song1) -> list:
    pre = defaultdict(list)
    sur = defaultdict(list)
    for s in songs:
        name = s.split(" ")
        head = name[0].lower()
        tail = name[-1].lower()
        pre[head].append(s)
        sur[tail].append(s)
    #res = []
    mx = []
    def getTail(songname):
        return songname.split(" ")[-1].lower()


    
    def backtracking(curr, songname, mx):
        lastword = getTail(songname)
        if lastword not in pre:
            #print('key not found', lastword)
            #print(curr)
            mx[:] = curr if len(mx) < len(curr) else mx
            return curr 
        

        for i in pre[lastword]:
            #print('current song:', i)
            
            if i not in curr:
                curr.append(i)              
                backtracking(curr, i, mx)
                curr.pop()
            
          
    backtracking([song1], song1,mx)
    return mx

            
    



songs = ['bye bye love', 'Take my money','bay bay Olivia', 'Every breath you take', 'Take forever love', 'Love the baby', 'baby live in bay']
song1 = 'Every breath you take'

print("output:", chainsongs(songs, song1))