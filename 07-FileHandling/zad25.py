import re 
message = "To be, or not to be, that is the question" 
a = re.findall('\w+',message)
print(f'the number of words in the text is: {len(a)}')