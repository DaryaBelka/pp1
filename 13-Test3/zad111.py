d = "Mark is 24 and Ann is 27"
import re
a = re.findall(r'\d+', d)
print(a)
