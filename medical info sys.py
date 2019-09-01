import requests as rt
import bs4
from tkinter import *
def scrap(name):
    dt=rt.request('get','https://www.1mg.com/search/all?name={}'.format(name))
    s=bs4.BeautifulSoup(dt.text,'html.parser')
    for i in s.findAll('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
        x=i.find('a')
        dts=rt.request('get','https://www.1mg.com'+x.get('href'))
        s1=bs4.BeautifulSoup(dts.text,'html.parser')
        mn=s1.find('div',{'class':'ProductDescription__product-description___1PfGf'})
        yield mn.text
def get(name,mess):
    global obj
    try:
        obj=scrap(name)
        mess.config(text=next(obj))
    except:
        mess.config(text='invalid name')
def datas(mess):
    global obj
    try:
        mess.config(text=next(obj))
    except:
        mess.config(text='end')
def mygui():
    scr=Tk()
    scr.geometry('1200x600+0+0')
    l=Label(scr,bd=4,text='MEDICAL INFORMATION SYSTEM',font=('times',20,'bold'),bg='orange')
    l.pack(fill=X,side=TOP)
    f=Frame(scr,bg='grey')
    f.pack(fill=BOTH,expand=12)
    e=Entry(f,bd=4,font=('times',20,'bold'),bg='orange')
    e.place(x=500,y=100)
    l=Label(f,bd=4,text='Name',font=('times',20,'bold'),bg='orange')
    l.place(x=400,y=100)
    b=Button(f,bd=4,text='get',font=('times',20,'bold'),bg='orange',command=lambda :get(e.get(),m))
    b.place(x=400,y=200)
    m=Message(f,bd=4,bg='orange',font=('times',15,'bold'),relief=RAISED)
    m.place(x=150,y=350)
    b1=Button(f,bd=4,text='next',font=('times',20,'bold'),bg='orange',command=lambda :datas(m))
    b1.place(x=600,y=200)
    scr.mainloop()




def login(us,ps):
        user=us.get()
        password=ps.get()
        data=open('user.txt').readlines()
        x=[i for i in data if (i.split(',')[1]==user) and (i.split(',')[2].replace('\n','')==password)]
        if len(x)>0:
            print("logged in\n")
            mygui()
        else:
           us.delete(0,END)
           ps.delete(0,END)

def register(us,ps):
        user=us.get()
        password=ps.get()
        if len(user)>0 and len(password)>=8:
            data=open('user.txt').readlines()[-1]
            num=int(data.split(',')[0])+1
            s='\n{},{},{}'.format(num,user,password)
            open('user.txt','a').write(s)
            print("user updated sucessfully and id is: {} save for further refrence \n".format(num))
            mygui()
        else:
            us.delete(0,END)
            ps.delete(0,END)
            


def mygui2():
    scr2=Tk()
    scr2.geometry('1200x600+0+0')
    l=Label(scr2,bd=4,text='LOGIN PAGE',font=('times',20,'bold'),relief=RAISED,bg='orange')
    l.pack(fill=X,side=TOP)
    f=Frame(scr2,bg='grey')
    f.pack(fill=BOTH,expand=12)
    e=Entry(f,bd=4,font=('times',20,'bold'),relief=RAISED,bg='orange')
    e.place(x=600,y=100)
    l=Label(f,bd=4,text='username',font=('times',20,'bold'),relief=RAISED,bg='orange')
    l.place(x=400,y=100)
    l2=Label(f,bd=4,text='Password',font=('times',20,'bold'),relief=RAISED,bg='orange')
    l2.place(x=400,y=200)
    ps=Entry(f,bd=4,show='*',font=('times',20,'bold'),relief=RAISED,bg='orange')
    ps.place(x=600,y=200)
    b=Button(f,bd=4,text='login',font=('times',20,'bold'),bg='orange',relief=RAISED,command=lambda:login(e,ps))
    b.place(x=400,y=400)
    b1=Button(f,bd=4,text='Register',font=('times',20,'bold'),bg='orange',relief=RAISED,command=lambda :register(e,ps))
    b1.place(x=600,y=400)
    scr2.mainloop()
mygui2()
    
    
    
    
