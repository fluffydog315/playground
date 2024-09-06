import pandas as pd
import random
import webbrowser
class RandomQ:
    
    def __init__(self):
        self.qs = []

    def getOneQuestion(self) -> None:
        cols = ["question", "link"]

        df = pd.read_csv('leetcode.cvs')
        random_index = random.randint(0, len(df)-1)
 
        df1 = df.iloc[random_index]
        url = str(df1['link']).strip()
        # MacOS
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open(url)




        
q1 = RandomQ()
df = q1.getOneQuestion()

