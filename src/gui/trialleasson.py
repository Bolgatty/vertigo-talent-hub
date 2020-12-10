import re
str="hitech institution a:b and hitech a:b group a:b of company"
var=re.split(r"a:\w",str)
print(var)