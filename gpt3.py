import os
import openai
import pandas as pd


openai.api_type = "azure"
openai.api_base = "https://aiforgoodlab-scu-openai.openai.azure.com/"
openai.api_version = "2022-03-01-preview"
openai.api_key = '[#add your key here#]'

#function to ignore newlines
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


#Examples gpt-3 davinci completions

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

file='./Examples/banknotes paper.tex'
file = './Examples/Glacial lakes monitoring paper.txt'
file = './Examples/disinformation detection.txt'

#read text file containing prompt
with open(file, 'r') as f:
    prompt=f.read()
pr(davinci(prompt, temperature=1, max_tokens=400))
