'''
Tugas Besar 1 [IF2211] Strategi Algoritma
Nama File : frontend.py
Deskripsi : Engine front-end untuk input dari file pertama dan mengeluarkan hasilnya pada file kedua
            dan engine front-end GUI untuk input random dari deck kartu dan mengeluarkan hasilnya pada GUI.
Nama Kelompok    : Hmm...
Anggota Kelompok :
    Ariel Ansa Razumardi    13517040
    Leonardo                13517048
    Vincent Chuardi         13517103
'''
#memakai kivy untuk GUI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
#untuk pemakaian kartu, dibuat library kartu
import kartu
#sys untuk menambahkan argumen pada compiling
import sys
#mengimport backend
import backend

class MyApp(App):
    def build(self):
        # title
        self.title = "Tugas Besar 1 IF2211 Strategi Algoritma Front End 1"
        #layout
        self.layout = BoxLayout(orientation = 'vertical')
        layout2 = BoxLayout(orientation = 'horizontal', size=(800,250), size_hint=(None, None))
        layout3 = BoxLayout(orientation = 'horizontal')
        layout4 = BoxLayout(orientation = 'horizontal')

        self.text1 = Label(text = '[size=40]Take 4 cards![/size]', markup = True)
        self.layout.add_widget(self.text1)
        self.pic1 = Image(source = kartu.card_pic['default'])
        self.pic2 = Image(source = kartu.card_pic['default'])
        self.pic3 = Image(source = kartu.card_pic['default'])
        self.pic4 = Image(source = kartu.card_pic['default'])
        layout2.add_widget(self.pic1)
        layout2.add_widget(self.pic2)
        layout2.add_widget(self.pic3)
        layout2.add_widget(self.pic4)
        self.layout.add_widget(layout2) #nested layout
        self.kartu1 = Label(color = (1,1,1,1), markup = True)
        self.kartu2 = Label(color = (1,1,1,1), markup = True)
        self.kartu3 = Label(color = (1,1,1,1), markup = True)
        self.kartu4 = Label(color = (1,1,1,1), markup = True)
        layout3.add_widget(self.kartu1)
        layout3.add_widget(self.kartu2)
        layout3.add_widget(self.kartu3)
        layout3.add_widget(self.kartu4)
        self.layout.add_widget(layout3) #nested layout
        self.btn1 = Button(text = "[size=20]Take Cards[/size]",
                           background_color = (0,1,1,1), markup = True,
                           on_press = self.kocokkartu)
        self.btn2 = Button(text = "[size=20]Submit[/size]",
                           background_color = (0,0,1,1), markup = True,
                           on_press = self.solve) #implementasi solve yang memanggil Greedy24Solver dari backend
        self.btn3 = Button(text = "[size=20]Cancel[/size]",
                           background_color = (1,0,0,1), markup = True,
                           on_press = self.clear_txt)
        self.btn4 = Button(text = "[size=20]Quit[/size]",
                           background_color = (0.5,0.6,0.7,1), markup = True,
                           on_press = exit)
        layout4.add_widget(self.btn1)
        layout4.add_widget(self.btn2)
        layout4.add_widget(self.btn3)
        layout4.add_widget(self.btn4)
        self.layout.add_widget(layout4) #nestedlayout
        self.jmlkartu = Label(text = "Sisa kartu pada deck anda : " + str(kartu.deck.size))
        self.layout.add_widget(self.jmlkartu)
        self.out = Label(text = '', markup = True)
        self.layout.add_widget(self.out)
        return self.layout
    
    def clear_txt(self, instance):
        #untuk reset
        self.text1.text = "[size=40]Take 4 cards![/size]"
        self.kartu1.text = ''
        self.kartu2.text = ''
        self.kartu3.text = '' 
        self.kartu4.text = ''
        self.pic1.source = kartu.card_pic['default']
        self.pic2.source = kartu.card_pic['default']
        self.pic3.source = kartu.card_pic['default']
        self.pic4.source = kartu.card_pic['default']
        self.out.text = ''
    
    def kocokkartu(self, instance):
        self.text1.text = "[size=40]Submit or take another 4 cards![/size]"
        if (kartu.deck.size > 0):
            kartu.deck.shuffle()
            self.hand = kartu.deck.deal(4)
            self.kartu1.text = str(self.hand[0])
            self.kartu1.color = (1,0,0,1) if (str(self.kartu1.text).split()[2] == 'Hearts' or 
                                              str(self.kartu1.text).split()[2] == 'Diamonds') else (1,1,1,1)
            self.kartu2.text = str(self.hand[1])
            self.kartu2.color = (1,0,0,1) if (str(self.kartu2.text).split()[2] == 'Hearts'or
                                              str(self.kartu2.text).split()[2] == 'Diamonds') else (1,1,1,1)
            self.kartu3.text = str(self.hand[2])
            self.kartu3.color = (1,0,0,1) if (str(self.kartu3.text).split()[2] == 'Hearts'or
                                              str(self.kartu3.text).split()[2] == 'Diamonds') else (1,1,1,1)
            self.kartu4.text = str(self.hand[3])
            self.kartu4.color = (1,0,0,1) if (str(self.kartu4.text).split()[2] == 'Hearts'or
                                              str(self.kartu4.text).split()[2] == 'Diamonds') else (1,1,1,1)
            self.pic1.source = kartu.card_pic[self.kartu1.text]
            self.pic2.source = kartu.card_pic[self.kartu2.text]
            self.pic3.source = kartu.card_pic[self.kartu3.text]
            self.pic4.source = kartu.card_pic[self.kartu4.text]
            self.jmlkartu.text = "Remaining cards on your deck : " + str(kartu.deck.size)
            self.out.text = ""
        else:
            self.out.text = "[size=40]The card on your deck runs out![/size]"

    def solve(self, instance):
        try:
            has = [0,0,0,0]
            has[0] = int(kartu.ranks[str(self.kartu1.text).split()[0]])
            has[1] = int(kartu.ranks[str(self.kartu2.text).split()[0]])
            has[2] = int(kartu.ranks[str(self.kartu3.text).split()[0]])
            has[3] = int(kartu.ranks[str(self.kartu4.text).split()[0]])
            self.out.text = "[size=40]" + backend.Greedy24Solver(has) + "[/size]"
        except IndexError:
            self.out.text = "[size=40]Take your cards first![/size]"
#endclass

if __name__ == "__main__":
    if len(sys.argv) > 1: #front end 2
        fin = sys.argv[1]
        fout = sys.argv[2]

        ffin = open(fin,"r")
        ffout = open(fout,"w")

        has = ffin.read()
        has = has.split(' ')

        for i in range(0,4):
            has[i] = int(has[i])

        ffout.write(backend.Greedy24Solver(has))

        ffin.close()
        ffout.close()
    else: #front end 1
        MyApp().run()