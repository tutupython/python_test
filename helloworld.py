import re
result=re.match('com', 'www.runoob.com')
if result:
    print(re.match('com', 'www.runoob.com').group())
else:
    print(result)