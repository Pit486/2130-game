with open('jok.png','r', encoding='UTF-8') as file:
    f=file.read()
    f=f.replace('#','')
with open('jok.png','w', encoding='UTF-8') as file:
    file.write(f)
print('ok')
