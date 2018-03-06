import re
content= "hello 1234567 World_This is hi a regex Demo"
pattern=re.compile('h.*? (.)(.)')
result=re.findall(pattern,content)
if result:
    print(result)
    print(type(result))
    for rec in result:
        print(type(rec))
        print(rec)

else:
    print(result)