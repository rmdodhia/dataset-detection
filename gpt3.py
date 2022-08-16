import os
import openai
import pandas as pd

rcw=pd.read_csv('./RCW.csv')

openai.api_type = "azure"
openai.api_base = "https://aiforgoodlab-scu-openai.openai.azure.com/"
openai.api_version = "2022-03-01-preview"
openai.api_key = '[#add your key here#]'


def pr(x):
    print(x, end='\n')

def davinci(prompt,temperature=0.70,max_tokens=60,p=0.9,full=False):
    print(temperature,max_tokens,p)
    response = openai.Completion.create(
        engine="RCW-2",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=p,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if full:
        return response
    else:
       return response.choices[0].text



print(prompt,end='\n')

response = davinci(prompt, max_tokens=220,temperature=.9,p=0.9)
response.choices[0].text




prompt = "which of the following comments is most similar to the original comment?"+ "\n original comment:"+c[0]+"\n comment 1:"+c[1]+"\n comment 2:"+c[3]


rcw.loc['19 310 040']

prompt="### Python code to write a transformer deep learning model"

# prompt='Complete this poem: Roses are red, violets are blue, I...'
# sendPrompt(prompt)


c1 = list(rcw[(rcw.TitleNumber == '10') & (rcw.ChapterNumber ==
          '64') & (rcw.SectionNumber == '100')]['P'])[0]
c1 = list(rcw[(rcw.TitleNumber == '19') & (rcw.ChapterNumber ==
          '310') & (rcw.SectionNumber == '040')]['P'])[0]
prompt = "Classify the following clause into one of these[Court, Property, Rules, Finance]\n\nClause: "+c1
pr(prompt)
pr(davinci(prompt[0:500], temperature=1, max_tokens=400, p=.4))

prompt = 'Are there any books about Admiral Zheng He?'
pr(davinci(prompt, temperature=1, max_tokens=400, p=.4))



c0 = "\nOriginal comment: In the event of an amergency, please follow the flight attendants' instructions."
c1 = '\nComment 1: the inflatable raft will deploy automatically.'
c2 = "\nComment 2: The attendants' job is to make sure all passengers are safe, everything else is secondary."
c3 = "\nComment 3: The attendants' are hired from countries all over the world."
prompt = "which of the following comments is most similar to the original comment"+c0+c1+c2+c3
pr(prompt)
pr(davinci(prompt, temperature=.7, max_tokens=400, p=.4))

c0 = "\nOriginal clause: The three branches of government balance each other, and check each other."
c1 = "\nClause 1: Dictators and tyrants ruled most of the ancient world"
c2 = "\nClause 2: The president works in concert with the judiciary and the legislators."
c3 = "\nClause 3: The three parts of godhood are equal but all powerful."
prompt = "which of the following clauses is most similar to the original clause"+c0+c1+c2+c3
prompt = "Why are each of the following clauses similar to the original clause?"+c0+c1+c2+c3
pr(prompt)
pr(davinci(prompt, temperature=.7, max_tokens=400, p=.8))


#Controversial
prompt='Complete the following sentence: The engineer was married to '
prompt ='What can Asians do better than others?\nAsians can '
prompt = 'Did the life of Africans improve after Europeans colonized the continent?'
pr(davinci(prompt, temperature=1, max_tokens=100,p=.5))

#Coding
prompt="### C# code to open a file"
prompt = "C# code to open a file"
prompt = "### Python code to write an image classification deep learning model"
prompt = "### Machine code decrease a variable by 1"
pr(davinci(prompt, temperature=1, max_tokens=800))

#Summarize RCW clause
a = list(rcw.P)
b = [p for p in a if type(p) == type(a[0])]
c = [p for p in b if 'dogs' in p.split()]
prompt = c[13]+'\n Tl;dr'
pr(davinci(prompt, temperature=1, p=.5,max_tokens=100))


### classify into category
sentence = 'The Broadway play was mired in lawsuits.'
prompt = "Categorize the following sentence into at least two of the following categories: categories: [Finance, Art, Legal, Science]\n\n" + sentence + "\n\nClassified category 1:\nClassified category 2: \n\n"
pr(davinci(prompt))

sentence = 'The newly discovered extrasolar planet was bought by a Martian for $10,000.'
prompt = "Categorize the following sentence into at least two of the following categories: categories: [Finance, Art, Legal, Science]\n\n" + \
    sentence + "\n\nClassified category 1:\nClassified category 2: \n\n"
pr(prompt)
pr(davinci(prompt,temperature=0.7))


#Rewrite different styles
prompt="Rewrite the following paragraph in the style of Mark Twain.\nParagraph: The world is becoming warmer. It is dangerous for humans. Indeed, it is dangerous for all life. we need to change our behavior.\n\nNew paragraph:"
prompt ="Rewrite the following paragraph in the style of an environmental activist.\nParagraph: The world is becoming warmer. It is dangerous for humans. Indeed, it is dangerous for all life. we need to change our behavior.\n\nNew paragraph: "
prompt = "Rewrite the following paragraph in the style of conservative politician.\nParagraph: The world is becoming warmer. It is dangerous for humans. Indeed, it is dangerous for all life. we need to change our behavior.\n\nNew paragraph:"
prompt = "Rewrite the following paragraph in the style of a dispassionate scientist.\nParagraph: I can't believe this is happening to the world, my only home! The pollution and disrespect to the environement is evil. Politicians are corrupt and don't care about saving our lives!\n\nNew paragraph: "
prompt = "Rewrite the following paragraph in the style of a Shakespeare.\nParagraph: I can't believe this is happening to the world, my only home! The pollution and disrespect to the environement is evil. Politicians are corrupt and don't care about saving our lives!\n\nNew paragraph: "
#Try Bob Dylan, Eminem
pr(prompt)
pr(davinci(prompt,temperature=.7,p=.7,max_tokens=100))

#Content generation
prompt="How do you start an essay on the existence of free will?\n\nParagraph:\n"
prompt = "How do you start an essay on the origins of lfe on earth?\n\nParagraph:\n"
pr(davinci(prompt,temperature=1,max_tokens=400,p=.7))


#AI for Good Foundation
#Disinformation Detection paper Section 2.1

file='./banknotes paper.tex'
file = './Glacial lakes monitoring paper.txt'
file = './disinformation detection.txt'
with open(file, 'r') as f:
    prompt=f.read()
pr(davinci(prompt, temperature=1, max_tokens=400))
