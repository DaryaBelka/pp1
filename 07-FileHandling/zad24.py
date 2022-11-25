import re 
message = "To be, or not to be, that is the question" 
a = re.findall('[aoeuiy]',message)
print(f'the number of vowels in the text is:  {len(a)}')