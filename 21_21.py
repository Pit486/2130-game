import random
from tkinter import *
from tkinter import ttk
from time import *
from PIL import Image, ImageTk

card_value = {'2p':2,'3p':3,'4p':4,'5p':5,'6p':6,'7p':7,'8p':8,'9p':9,'10p':10,'vp':2,'dp':3,'kp':4,'tp':11,
'2k':2,'3k':3,'4k':4,'5k':5,'6k':6,'7k':7,'8k':8,'9k':9,'10k':10,'vk':2,'dk':3,'kk':4,'tk':11,
'2b':2,'3b':3,'4b':4,'5b':5,'6b':6,'7b':7,'8b':8,'9b':9,'10b':10,'vb':2,'db':3,'kb':4,'tb':11,
'2c':2,'3c':3,'4c':4,'5c':5,'6c':6,'7c':7,'8c':8,'9c':9,'10c':10,'vc':2,'dc':3,'kc':4,'tc':11}
nominal = ['2','3','4','5','6','7','8','9','10','v','d','k','t']
mast = ['p','k','b','c']


nh=0#первая сдача-comp
e=False#видимость карт компьютера
card_now_comp = []
card_now_hum = []
ran_c = ''#текущая карта
s_comp = 0 #общий счёт
s_human = 0
sum_c = 0 #сумма очков враунде
sum_h = 0
txt=''
txt_color='white'
cards_c=[]
cards_h=[]
w=''#конец партии

txt_1='Bankroll    computer '
txt_1a=' You'
txt_2='Your Point Count '
txt_b1='Draw'
txt_b2='Stand'
txt_w='You Win!'
txt_l='You lost!'
txt_n='Push.'
txt_w22='Bust! You Win'
txt_l22='Bust! You lost'
txt_l21='Twenty One! You lost'
txt_w21='Twenty One! You Win'


def rrr():#отрисовка карт
    global card_now_hum, card_now_comp, cards_c, cards_h, txt, txt_color
    x=400-((len(card_now_comp)-1)*28)
    cards_c=[]
    cards_h=[]
    for i in card_now_comp:
        if e:
            c_pic = i+'.png'
        else:
            c_pic = 'rub.png'
        card = PhotoImage(file=c_pic)
        cards_c.append(card)
    for i in cards_c:
        crd = c.create_image(x, 100, image=i)
        x=x+43
    x=400-((len(card_now_hum)-1)*28)
    for i in card_now_hum:
        card = PhotoImage(file=i+'.png')
        cards_h.append(card)
    for i in cards_h:
        crd = c.create_image(x, 450, image=i)
        x=x+43
    c.itemconfig(ct, text=txt, fill=txt_color )
    label1['text']=txt_1+str(s_comp)+':'+str(s_human)+txt_1a
    label2['text']=txt_2+str(sum_h)
    c.pack()
    return

def card_now(): #выбор новой карты
    global mast,nominal, card_now_comp, card_now_hum
    cn=random.randint(0,12)
    cm=random.randint(0,3)
    ran_c = nominal[cn]+mast[cm]
    if ran_c in card_now_comp or ran_c in card_now_hum:
        card_now()
    return ran_c


def button_draw(event):
    global card_now_comp, card_now_hum, nh,h,sum_h,sum_c,card_value, s_comp, s_human, w, cards_c, cards_h, w,txt
    e=False
    txt=''
    if w!='':
        card_now_comp = []
        card_now_hum = []
        sum_c = 0 #сумма очков враунде
        sum_h = 0
        ran_c = ''#текущая карта
        cards_c=[]
        cards_h=[]
        label1['text']=txt_1+str(s_comp)+':'+str(s_human)+txt_1a
        label2['text']=txt_2+str(sum_h)
        txt=''
        c.itemconfig(ct, text=txt, fill=txt_color )
        w=''
        e=False
        return
    if nh==0:
        nh0()
        rrr()
        nh=1
        return
    elif card_now_hum==[] and nh==1:
        card_now_hum.append(card_now())
        card_now_hum.append(card_now())
    elif nh==1:
        card_now_hum.append(card_now())
    sum_c,sum_h=0,0
    for k in card_now_comp:
        sum_c = sum_c+card_value[k]
    for k in card_now_hum:
        sum_h = sum_h+card_value[k]
    if e==True:
        chek()
    if sum_h>21:
        nh=0
        w='l22'
        e=True
        rrr()
        win()
        return
    elif sum_h==21:
        nh=1
        w='w21'
        e=True
        rrr()
        win()
        return
    rrr()
    return
        
def chek():
    global card_now_comp, card_now_hum, nh,h,sum_h,sum_c,card_value, s_comp, s_human, w, cards_c, cards_h, w,txt
    rrr()
    if sum_c>21:
        nh=1
        w='w22'
        win()
        return
    elif sum_h==21:
        w='w21'
        nh=1
        win()
        return
    elif sum_h>21 :
        w='l22'
        nh=0
        win()
        return
    elif sum_c==21:
        nh=0
        w='l21'
        win()
        return
    if sum_h<21 and nh==1 and e==False:
        return
    elif sum_c>sum_h and e==True:
        nh=0
        w='los'
        win()
        return
    elif sum_c<sum_h and e==True:
        nh=1
        w='w'
        win()
        return
    elif sum_c==sum_h and e==True:
        w='nnn'
        win()
        return

def button_stand(event):# pass
    global card_now_comp, card_now_hum, nh, s_comp, s_human, sum_c,sum_h, w, e
    if card_now_comp ==[]: #если у компьютера нет карт-переход хода
        nh=0
        nh0()
        rrr()
        e=True
    e=True
    chek()
    return
       
def win():
    global sum_c, sum_h, nh, e, s_comp, s_human, txt, txt_color,w
    e=True
    if w.find('l')>=0 and w!='nnn':
        s_comp=s_comp+1
    elif w.find('w')>=0 and w!='nnn':
        s_human=s_human+1
    if w=='w':
        txt=txt_w
        nh=1
        rrr()
    elif w=='los':
        txt=txt_l
        nh=0
        rrr()
    elif w=='nnn':
        txt=txt_n
        rrr()
    elif w=='w22':
        txt=txt_w22
        nh=1
        rrr()
    elif w=='l22':
        txt=txt_l22
        nh=0
        rrr()
    elif w=='l21':
        txt=txt_l21
        nh=0
        rrr()
    elif w=='w21':
        txt=txt_w21
        nh=1
        rrr()
    else:
        print('w error')
    return
    
def nh0():
    global nh, sum_c, sum_h, txt, txt_color, e, card_now_comp, w, s_human, s_comp, card_now_hum
    while sum_c < (random.randint(15,18)):
        card_now_comp.append(card_now())
        if len(card_now_comp)<2:
            card_now_comp.append(card_now())
        sum_c=0
        sum_h=0
        for k in card_now_comp:
            sum_c = sum_c+card_value[k]
        for k in card_now_hum:
            sum_h = sum_h+card_value[k]
    e=False
    if sum_c>21:
        nh=1
        w='w22'
        e=True
        win()
        return
    elif sum_c==21:
        nh=0
        w='l21'
        e=True
        win()
        return
    return

tk = Tk()
tk.iconbitmap('i21.ico')
tk.title("21 v2.1")
tk.geometry("800x700")
tk.configure(background="#22B14C")


tk.update_idletasks()
s = tk.geometry()
s = s.split('+')
s = s[0].split('x')
width = int(s[0])
height = int(s[1])

c = Canvas(tk, width=width, height=(height-150), bg='#22B14C', highlightthickness=0)

img = Image.open('stol.jpg')
img = img.resize((width, height))
img_tk = ImageTk.PhotoImage(img)
fon = c.create_image(400, 230, image=img_tk)

def check():
    global jaz, txt_1, txt_1a,txt_2,txt_b1,txt_b2,txt_w,txt_l,txt_n,txt_w22,txt_l22,txt_l21,txt_w21,bt3
    with open('ru.txt','r') as f:
        txt_1 = (str(f.readline())).replace('\n',' ')
        txt_1a = (str(f.readline())).replace('\n',' ')
        txt_2 = (str(f.readline())).replace('\n',' ')
        txt_b1 = (str(f.readline())).replace('\n',' ')
        txt_b2 = (str(f.readline())).replace('\n',' ')
        txt_w= (str(f.readline())).replace('\n',' ')
        txt_l=(str(f.readline())).replace('\n',' ')
        txt_n=(str(f.readline())).replace('\n',' ')
        txt_w22=(str(f.readline())).replace('\n',' ')
        txt_l22=(str(f.readline())).replace('\n',' ')
        txt_l21=(str(f.readline())).replace('\n',' ')
        txt_w21=(str(f.readline())).replace('\n',' ')
        btn1 = Button(text = txt_b1, width=12, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'20'))
        btn1.bind('<Button-1>', button_draw)
        btn1.place(x=8,y=620)
        btn2 = Button(text = txt_b2, width=12, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'20'))
        btn2.bind('<Button-1>', button_stand)
        btn2.place(x=250,y=620)
        c.delete(bt3Id)
        rrr()
    return
 
 
bt3=Button(text="RUS")
bt3.bind('<Button-1>', check)
bt3 = ttk.Button(text="RUS", command=check)
bt3Id = c.create_window(30, 20, window=bt3, width=50, height=25)

btn1 = Button(text = txt_b1, width=12, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'20'))
btn1.bind('<Button-1>', button_draw)
btn1.place(x=8,y=620)

btn2 = Button(text = txt_b2, width=12, height=1, bg="grey", fg="yellow", font=('Arial Black' ,'20'))
btn2.bind('<Button-1>', button_stand)
btn2.place(x=250,y=620)

label1 = ttk.Label()
label1.configure(foreground=txt_color, background='#22B14C', width=30, anchor="center", font=("Arial", 18)) 
label1.place(x=60,y=575)
label1['text']=txt_1+str(s_comp)+':'+str(s_human)+txt_1a

label2 = ttk.Label()
label2.configure(foreground=txt_color, background='#22B14C', width=20, anchor="center", font=("Arial", 18)) 
label2.place(x=515,y=575)
label2['text']=txt_2+str(sum_h)

ct = c.create_text(395, 260, text=txt, justify=CENTER, font="Arial 32", fill=txt_color)

    
mainloop()

