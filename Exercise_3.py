text=str(input('Введите текст: '))
b=[]
d={}
for keys in text:
    if keys.isalpha(): b.append(keys)
for keys in b:
    count=d.get(keys)
    if count is None: d[keys]=1
    else: d[keys]=count+1
print(d)
