import os
def MadLibs(what):
    input_text=str(what)
    text=input_text.split()
    j=0
    for j in range(len(text)-1):
        if text[j].lower()=='adjective':
            adj=input('Enter an adjective:\n')
            text[j]=adj
        elif text[j].lower()=='verb':
            vrb=input('Enter a verb:\n')
            text[j]=vrb

        elif text[j].lower()=='adverb':
            adv=input('Enter an adverb:\n')
            text[j]=adv

        elif text[j].lower()=='noun':
            noun=input('Enter a noun:\n')
            text[j]=noun
        
        
    output = ' '.join(text)
    textFile=open('D:\\Python\\Automate stuffs with Python\\ch.8 project2 results.txt','w')
    textFile.write(output)
    textFile.close()
