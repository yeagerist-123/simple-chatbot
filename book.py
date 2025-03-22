import re
'''
with open("The_Verdict.txt","r",encoding="utf-8") as f:
    raw_txt=f.read()
print("total no of char:",len(raw_txt))
print(raw_txt[:99])
'''
text='hi friends, today is. holy'
result=re.split(r'([.,]|\s)',text)
print(result)

