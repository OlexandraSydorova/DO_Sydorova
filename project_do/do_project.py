
from tkinter import *
from PIL import ImageTk, Image

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)

        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


def knapsack(cap, values, weights):
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total += item['weight'] * item['vpw']
            cap_left -= item['weight']

    return total
p = 0
sum = 0
lst = []
cap = 6
values = [150, 300, 310,170,140,600,200,320,120]
weights = [0.4,1.5,2,0.5,0.1,2.5,1,3,0.2]
total = knapsack(cap,values,weights)
def click1():
    global sum
    global total
    global lst
    lst.append(1)
    sum+=150
    global p
    p+=0.400
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click2():
    global sum
    global lst
    lst.append(2)
    sum+=170
    global p
    p+=0.500
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = " + str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click3():
    global sum
    global lst
    lst.append(3)
    sum+=200
    global p
    p+=1
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click4():
    global sum
    global lst
    lst.append(4)
    sum+=300
    global p
    p+=1.5
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click5():
    global sum
    global lst
    lst.append(5)
    sum+=140
    global p
    p+=0.100
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click6():
    global sum
    global lst
    lst.append(6)
    sum+=320
    global p
    p+=3
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click7():
    global sum
    global lst
    lst.append(7)
    sum+=310
    global p
    p+=2
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click8():
    global sum
    global lst
    lst.append(8)
    sum+=600
    global p
    p+=2.5
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)
def click9():
    global sum
    global lst
    lst.append(9)
    sum+=120
    global p
    p+=0.200
    lbl = Label(root, text = "Сума вартості: " + str(sum)+"$\nСума ваги: "+str(round(p,3))+"кг", font=("Arial Bold", 18)).place(x=770, y=100)
    if p>6:
        lbl = Label(root, text="Місію провалено\nВагу рюкзака перевищено", font=("Arial Bold", 18), fg = "red").place(x=770, y=100)
    if 5 in lst and 9 in lst and 1 in lst and 2 in lst and 8 in lst and 3 in lst:
        lbl = Label(root, text="Місію виконано\nЗагальна вартість \nвкраденого = "+str(total)+"$", font=("Arial Bold", 18), fg="green").place(x=770, y=100)
        anim = MyLabel(root, 'salut.gif')
        anim.place(x=800, y=250)


root = Tk()
root.title("ХОЧУ 100!!!")
root.geometry('1400x700')
img = ImageTk.PhotoImage(Image.open("2.png"))
panel = Label(root, image = img)
panel.place(x=1100, y=150)
lbl = Label(root, text="Максимальна місткість \nрюкзака крадія = 6кг", font=("Arial Bold", 18)).place(x=1050, y=25)
image1 = Image.open("kamera.jpg")
image1 = image1.resize((220,140))
image1 = ImageTk.PhotoImage(image1)
lbl1 = Label(root, text="Вартісь: 150$\nВага: 400г", font=("Arial Bold", 16)).place(x=60, y=0)
Button(root, image=image1, command=click1).place(x=10, y=50)

image2 = Image.open("kar.jpg")
image2 = image2.resize((220,140))
image2 = ImageTk.PhotoImage(image2)
lbl2 = Label(root, text="Вартісь: 170$\nВага: 500г", font=("Arial Bold", 16)).place(x=60, y=200)
Button(root, image=image2, command=click2).place(x=10, y=250)

image3 = Image.open("kofe.jpg")
image3 = image3.resize((220,140))
image3 = ImageTk.PhotoImage(image3)
lbl3 = Label(root, text="Вартісь: 200$\nВага: 1кг", font=("Arial Bold", 16)).place(x=60, y=400)
Button(root, image=image3, command=click3).place(x=10, y=450)

image4 = Image.open("nout.jpg")
image4 = image4.resize((220,140))
image4 = ImageTk.PhotoImage(image4)
lbl4 = Label(root, text="Вартісь: 300$\nВага: 1кг 500г", font=("Arial Bold", 16)).place(x=300, y=0)
Button(root, image=image4, command=click4).place(x=250, y=50)

image5 = Image.open("kol.jpg")
image5 = image5.resize((220,140))
image5 = ImageTk.PhotoImage(image5)
lbl5 = Label(root, text="Вартісь: 140$\nВага: 100г", font=("Arial Bold", 16)).place(x=300, y=200)
Button(root, image=image5, command=click5).place(x=250, y=250)

image6 = Image.open("plita.jpg")
image6 = image6.resize((220,140))
image6 = ImageTk.PhotoImage(image6)
lbl6 = Label(root, text="Вартісь: 320$\nВага: 3кг", font=("Arial Bold", 16)).place(x=300, y=400)
Button(root, image=image6, command=click6).place(x=250, y=450)

image7 = Image.open("tel.jpg")
image7 = image7.resize((220,140))
image7 = ImageTk.PhotoImage(image7)
lbl7 = Label(root, text="Вартісь: 310$\nВага: 2кг", font=("Arial Bold", 16)).place(x=540, y=0)
Button(root, image=image7, command=click7).place(x=490, y=50)

image8 = Image.open("tree.jpg")
image8 = image8.resize((220,140))
image8 = ImageTk.PhotoImage(image8)
lbl8 = Label(root, text="Вартісь: 600$\nВага: 2кг 500г", font=("Arial Bold", 16)).place(x=540, y=200)
Button(root, image=image8, command=click8).place(x=490, y=250)

image9 = Image.open("clock.jpg")
image9 = image9.resize((220,140))
image9 = ImageTk.PhotoImage(image9)
lbl9 = Label(root, text="Вартісь: 120$\nВага: 200г", font=("Arial Bold", 16)).place(x=540, y=400)
Button(root, image=image9, command=click9).place(x=490, y=450)


root.mainloop()
