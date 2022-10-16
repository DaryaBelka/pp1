str = 'X-DSPAM-Confidence:0.8475'
start = str.find(":")
a = str[start+1:]
a = float(a)
print(a)