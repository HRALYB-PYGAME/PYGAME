from random import*
import math
import time
from tkinter import*
perc = int(0)
root = Tk()
w = Label(root, text = "Vítej v mé hře je zde spousta věcí k dělání a vytváření. Je plná pracovních příležitostí, které vám pomůžou vstát z nuly. Dále například banka, clicker či boss fight, speciální i normální úroveň, propracovaný obchod a mnoho dalšího")
w.pack()
root.mainloop()
#odpocet loadingu
while perc != 101:
    print ("loading ", perc, "%")
    perc = perc + 1
    time.sleep(0.02)
#na zacatku prirazene hodnoty f  a  q
# print (Delka)
f = int(0)
money = 0
xp = 0
ach1 = 0
ach2 = 0
ach3 = 0
ach4 = 0
ach5 = 0
ach6 = 0
ach7 = 0
ach8 = 0
ach9 = 0
ach10 = 0
ach11 = 0
ach12 = 0
ach13 = 0
ach14 = 0
ach15 = 0
ach16 = 0
ach17 = 0
ach18 = 0
ach19 = 0
ach20 = 0
ach21 = 0
ach22 = 0
ach23 = 0
ach24 = 0
ach25 = 0
ach26 = 0
ach27 = 0
ach28 = 0
ach29 = 0
ach30 = 0
ach31 = 0
ach32 = 0
ach33 = 0
ach34 = 0
ach35 = 0
ach36 = 0
ach37 = 0
ach38 = 0
ach39 = 0
ach40 = 0
ach41 = 0
ach42 = 0
ach43 = 0
ach44 = 0
ach45 = 0
ach46 = 0
ach47 = 0
ach48 = 0
ach49 = 0
ach50 = 0
ach51 = 0
ach52 = 0
ach53 = 0
ach54 = 0
ach55 = 0
ach56 = 0
ach57 = 0
ach58 = 0
ach59 = 0
ach60 = 0
ach61 = 0
ach62 = 0
ach63 = 0
ach64 = 0
ach65 = 0
ach66 = 0
ach67 = 0
ach68 = 0
ach69 = 0
ach70 = 0
ach71 = 0
ach72 = 0
ach73 = 0
ach74 = 0
ach75 = 0
ach76 = 0
ach77 = 0
ach78 = 0
ach79 = 0
ach80 = 0
ach81 = 0
ach82 = 0
ach83 = 0
ach84 = 0
ach85 = 0
ach86 = 0
nav0 = 0
nav1 = 0
nav2 = 0
nav3 = 0
nav4 = 0
nav5 = 0
nav6 = 0
nav7 = 0
nav8 = 0
nav9 = 0
nav10 = 0
nav11 = 0
nav12 = 0
nav13 = 0
nav15 = 0
a = int(0)
caspuj = 0
pocgame1 = 0
reccord = 0
vyleps = 1
ngc = 3000
ngs = 1
playerhp = 100
bosshp = 100
urok = 0
q = 5
mocnina = 1
bubla = 0
lucifer = 0
kámen = 0
bonusmoney = 0
hralyb = 0
unik = 0
celkem = 0
diamond = 0
g = 0
prace = 0
zajednoho = 5
zplaceno = 1
gems = 0
Cas_Start = round(time.monotonic(),1)
cena = 100
cenaprc = 500
vzlepseni = 0
bank = 0
cenob = 0.1
perce = 0
pole = 0
rekord = 0
record = 0
win = 0
spewin = 0
lose = 0
obili = 0
spelose = 0
while(f != 1):
    while(g != 1):
        a = int(input("napis heslo: "))
        if(a == 0):
            ach86 = ach86 + 1
        if(a == q):
            print("spravne heslo muzes pokracovat")
            g = 1
        else:
            ach68 = ach68 + 1
            print("spatne heslo musis znovu")
        f = 1
    while(f == 1):
        stare = int(4)
        print(" __| |____________________________________________| |__")
        print("(__   ____________________________________________   __)")
        print("   | |                                            | |")
        print("   | |                                            | |")
        print("   | |                                            | |")
        print("   | |                       HRA                  | |")
        print("   | |                                            | |")
        print("   | |                                            | |")
        print(" __| |____________________________________________| |__")
        print("(__   ____________________________________________   __)")
        print("   | |                                            | |")
        cislo = int(input("vyber si cislo"))
        test = cislo + vzlepseni       
        print ("obtiznost musí být větší nebo stejná jako", test)
        obtiznozt = int(input("obtiznost"))
        obtileps = obtiznozt - vzlepseni
        if(cislo <= obtileps):         
            random = randint(1,obtiznozt - vzlepseni)
        if(cislo > obtileps):
            print("chyba")
        if(random == cislo):
            print("zvládl si level", obtiznozt)
            money = money + obtiznozt * obtiznozt + bonusmoney * 10
            monhra = obtiznozt * obtiznozt + bonusmoney * 10
            print("za tuto hru si získal", monhra,"peněz")
            win = win + 1
        else:
            print("nezvládl si level",obtiznozt)
            lose = lose + 1
        g = 0
        print("mas", money, "peněz")
        tele = 0
        if(obtiznozt > rekord):
            if(cislo == random):
                rekord = obtiznozt
                print("mas novy rekord", rekord)
        while(tele == 0):
            tele = 1
            if(money > record):
                record = money
            print(" __| |____________________________________________| |__")
            print("(__   ____________________________________________   __)")
            print("   | |                                            | |")
            print("   | |                                            | |")
            print("   | |       HERNÍ                                | |")
            print("   | |                       MENU                 | |")
            print("   | |                                            | |")
            print("   | |                                            | |")
            print(" __| |____________________________________________| |__")
            print("(__   ____________________________________________   __)")
            print("   | |                                            | |")
            print("0 shop")
            print("100 lottery")
            print("1 hrat")
            print("2 change password")
            print("3 bank")
            print("4 odhlášení")
            print("5 tvé staty")
            print("6 kup pracovníka")
            print("7 gem shop")
            print("8 prodat obilí")
            print("9 diamond shop")
            print("10 opisování čísel")
            print("11 idle clicker")
            print("12 boss fight")
            print("13 pracovní příležitosti")
            print("14 pro tvé achievementy")
            print("15 pro dovážení zásilek")
            shop = int(input(""))
            if(shop == 666):
                ach70 = ach70 + 1
            if(shop > 10000):
                ach71 = ach71 + 1
            if(shop < 0):
                ach72 = ach72 + 1
            if(shop == 16):
                ach73 = ach73 + 1
            if(shop == 100):
                print("vítej v lotterii")
                lotterynumber = int(input("číslo (1,2)"))
                lotterymoney = int(input("kolik chceš vsadit"))
                if(lotterymoney > money):
                    print("co to meleš ty vořechu")
                if(lotterymoney <= money):
                    rand1lot = randint(1,2)
                    print(rand1lot)
                    time.sleep(3)
                    rand1lot = randint(1,2)
                    print(rand1lot)
                    time.sleep(3)
                    rand1lot = randint(1,2)
                    print(rand1lot)
                    time.sleep(3)
                    rand1lot = randint(1,2)
                    print(rand1lot)
                    time.sleep(3)
                    rand1lot = randint(1,2)
                    print(rand1lot)
                    time.sleep(3)
                    if(rand1lot == lotterynumber):
                        money = money + lotterymoney
                        print("máš", money, "peněz")
                    else:
                        money = money - lotterymoney
                        print("máš pouze", money, "peněz")
            if(shop == 15):
                nav15 = nav15 + 1
                print("ahoj vyber si jednu z těchto zásilek")
                zas1 = print("zásilka 1 za", randint(100,500))
                zas2 = print("zásilka 2 za", randint(200,800))
                zas3 = print("zásilka 3 za", randint(400,1200))
                zas4 = print("zásilka 4 za", randint(700,1500))
                zask = int(input())
                if(zask == 1):
                    vzd1 = print("vzdálenost na dojezd je",randint(200,450), "km chceš jet pokud ano zmáčkni 1")
                    vzd1a = int(input())
                    if(vzd1a == 1):
                        time1 = randint(200,450)
                        print("bude to trvat",time1 * 1.5,"minut")
                        timetruck1 = time.monotonic()
                        truck1 = 1
                        time1truck = time.monotonic()
                        while(truck1 == 1):
                            int(input("cislo pro kontrolu"))
                            timetruck1 = time.monotonic()
                            if(timetruck1 >= time1truck + time1 * 60):
                                truck1 = 0
                                print("dokončil si svoji práci")
                                money = money + zas1
                if(zask == 2):
                    vzd2 = print("vzdálenost na dojezd je",randint(400,750), "km chceš jet pokud ano zmáčkni 1")
                    vzd2a = int(input())
                    if(vzd2a == 1):
                        time2 = randint(400,750)
                        print("bude to trvat",time2 * 1.5,"minut")
                        timetruck2 = time.monotonic()
                        truck2 = 1
                        time2truck = time.monotonic()
                        while(truck2 == 1):
                            int(input("cislo pro kontrolu"))
                            timetruck2 = time.monotonic()
                            if(timetruck2 >= time2truck + time2 * 60):
                                truck2 = 0
                                print("dokončil si svoji práci")
                                money = money + zas2
                if(zask == 3):
                    vzd3 = print("vzdálenost na dojezd je",randint(200,450), "km chceš jet pokud ano zmáčkni 1")
                    vzd3a = int(input())
                    if(vzd3a == 1):
                        time3 = randint(200,450)
                        print("bude to trvat",time3 * 1.5,"minut")
                        timetruck3 = time.monotonic()
                        truck3 = 1
                        time3truck = time.monotonic()
                        while(truck3 == 1):
                            int(input("cislo pro kontrolu"))
                            timetruck3 = time.monotonic()
                            if(timetruck3 >= time3truck + time3 * 60):
                                truck3 = 0
                                print("dokončil si svoji práci")
                                money = money + zas3
                if(zask == 5):
                    ach74 = ach74 + 1
                if(zask == 4):
                    vzd4 = print("vzdálenost na dojezd je",randint(200,450), "km chceš jet pokud ano zmáčkni 1")
                    vzd4a = int(input())
                    if(vzd4a == 1):
                        time4 = randint(200,450)
                        print("bude to trvat",time4 * 1.5,"minut")
                        timetruck4 = time.monotonic()
                        truck4 = 1
                        timečtruck = time.monotonic()
                        while(truck4 == 1):
                            int(input("cislo pro kontrolu"))
                            timetruck4 = time.monotonic()
                            if(timetruck4 >= time4truck + time4 * 60):
                                truck4 = 0
                                print("dokončil si svoji práci")
                                money = money + zas4
            if(shop == 14):
                print("toto je seznam tvých achievemntů:")
                print("start the game")
                if(ach1 > 0):
                    print("classic gamer")
                if(ach1 > 25):
                    print("classic hacker")
                if(ach2 > 0):
                    print("professional gamer")
                if(ach2 > 25):
                    print("professional hacker")
                if(ach3 > 0):
                    print("village business man")
                if(ach4 > 0):
                    print("business man gold")
                if(ach5 > 0):
                    print("shibal")
                if(ach6 > 0):
                    print("bečan")
                if(ach7 > 0):
                    print("banker")
                if(ach8 > 0):
                    print("banker with shit")
                if(ach9 > 0):
                    print("long time player")
                if(ach10 > 0):
                    print("very long time player")
                if(ach11 > 0):
                    print("information is more than salt")
                if(ach12 > 0):
                    print("information is more than information")
                if(ach13 > 0):
                    print("start the company")
                if(ach14 > 0):
                    print("international company")
                if(ach15 > 0):
                    print("riskman")
                if(ach16 > 0):
                    print("risk is my life")
                if(ach17 > 0):
                    print("farmer")
                if(ach18 > 0):
                    print("company farmer")
                if(ach19 > 0):
                    print("more than gems")
                if(ach20 > 0):
                    print("i am so rich")
                if(ach21 > 0):
                    print("keyboard master")
                if(ach22 > 0):
                    print("i am just racing with light")
                if(ach23 > 0):
                    print("clicks")
                if(ach24 > 0):
                    print("double clicks")
                if(ach25 > 0):
                    print("i hate my boss")
                if(ach26 > 0):
                    print("builder hat")
                if(ach27 > 0):
                    print("i go out from university")
                if(ach28 > 0):
                    print("money money money, but hard work")
                if(ach29 > 0):
                    print("first profit")
                if(ach30 > 0):
                    print("i am a thousandlionare")
                if(ach31 > 0):
                    print("it like dream")
                if(ach31 > 25):
                    print("bath with money")
                if(ach32 > 0):
                    print("this amount is a godly epic")
                if(ach32 > 25):
                    print("THE impossible CHALLENGE!")
                if(ach33 > 0):
                    print("you are under zero")
                if(ach33 > 25):
                    print("long-time")
                if(ach33 > 50):
                    print("uncountable")
                if(ach34 > 0):
                    print("savings")
                if(ach35 > 0):
                    print("Savings")
                if(ach36 > 0):
                    print("SAVINGS")
                if(ach37 > 0):
                    print("saving error")
                if(ach37 > 25):
                    print("saving error 2")
                if(ach38 > 0):
                    print("yellow car!")
                if(ach39 > 0):
                    print("i am better than you")
                if(ach40 > 0):
                    print("winner winner chicken dinner")
                if(ach41 > 0):
                    print("YELLOW CAR!")
                if(ach42 > 0):
                    print("yellow monster truck!")
                if(ach43 > 0):
                    print("ů)-§§ů§§)..§íííí")
                if(ach44 > 0):
                    print("20% chance")
                if(ach45 > 0):
                    print("10% chance")
                if(ach45 > 25):
                    print("1% chance")
                if(ach46 > 0):
                    print("you must use upgrades")
                if(ach47 > 0):
                    print("hack confirmed")
                if(ach48 > 0):
                    print("ready to spam")
                if(ach49 > 0):
                    print("money from clicking?")
                if(ach50 > 0):
                    print("how much upgrades do you have")
                if(ach51 > 0):
                    print("half a meloun")
                if(ach51 > 25):
                    print("half a melon")
                if(ach52 > 0):
                    print("you have IQ sprouting grass")
                if(ach53 > 0):
                    print("upgrader")
                if(ach54 > 0):
                    print("money factory")
                if(ach55 > 0):
                    print("print the money for upgrades!")
                if(ach56 > 0):
                    print("start experience")
                if(ach57 > 0):
                    print("free xp points")
                if(ach58 > 0):
                    print("windows xp")
                if(ach58 > 25):
                    print("LINUX xp")
                if(ach59 > 0):
                    print("xantypa provokuje")
                if(ach60 > 0):
                    print("first step farmer")
                if(ach61 > 0):
                    print("hectars")
                if(ach62 > 0):
                    print("your fields everywhere")
                if(ach63 > 0):
                    print("farmers has no stop")
                if(ach64 > 0):
                    print("wheat have high price lets sell!")
                if(ach65 > 0):
                    print("MEGA wheat")
                if(ach66 > 0):
                    print("truck is my friend")
                if(ach67 > 0):
                    print("driving is my life")
                if(ach68 > 0):
                    print("YOU HAVE VERY LOW IQ")
                if(ach69 > 0):
                    print("dont change IT!")
                if(ach70 > 0):
                    print("hell number 666")
                if(ach70 > 2):
                    print("hell numbers 666")
                if(ach71 > 0):
                    print("stop spamming")
                if(ach72 > 0):
                    print("you have IQ as stone falling from cliff")
                if(ach73 > 0):
                    print("never wait for next update")
                if(ach73 > 19):
                    print("WHEN?")
                if(ach74 > 0):
                    print("why only 4")
                if(ach75 > 0):
                    print("first gem")
                if(ach76 > 0):
                    print("sack of gems")
                if(ach77 > 0):
                    print("bag of gems")
                if(ach77 > 9):
                    print("two bags of gems")
                if(ach77 > 29):
                    print("ten bags of gems")
                if(ach78 > 0):
                    print("GEMS")
                if(ach79 > 0):
                    print("truck of gems")
                if(ach80 > 0):
                    print("dont mine it with gold pickaxe")
                if(ach81 > 0):
                    print("luck master")
                if(ach82 > 0):
                    print("lottery winner")
                if(ach83 > 0):
                    print("Einstein win 100 diamonds")
                if(ach84 > 0):
                    print("You must hack this game")
                if(ach85 > 0):
                    print("1 is not 2")
                if(ach85 > 9):
                    print("1 is not 99908")
                if(ach86 > 0):
                    print("You are nothing")
                time.sleep(10)
            if(shop == 13):
                nav13 = nav13 + 1
                print("0 pro odchod")
                print("1 pro práci na 1 minutu (5 money)")
                print("2 pro práci na 5 minut (20 money)")
                print("3 pro práci na 30 minut (105 money)")
                print("4 pro práci na 5 hodin (950 money)")
                cas = int(input())
                if(cas == 4):
                    print("zmáčkni cokoliv pro pokračování")
                    input()
                    print("tvoje práce začala vyčkej 5 hodin")
                    timejob4 = time.monotonic()
                    fofaf = 1
                    time4while = time.monotonic()
                    while(fofaf == 1):
                        int(input("cislo pro kontrolu"))
                        timejob4 = time.monotonic()
                        if(timejob4 >= time4while + 18000):
                            fofaf = 0
                            print("dokončil si svoji práci")
                            money = money + 950
                if(cas == 1):
                    print("zmáčkni cokoliv pro pokračování")
                    input()
                    print("tvoje práce začala vyčkej minutu")
                    timejob1 = time.monotonic()
                    fofa = 1
                    time1while = time.monotonic()
                    while(fofa == 1):
                        int(input("cislo pro kontrolu"))
                        timejob1 = time.monotonic()
                        if(timejob1 >= time1while + 60):
                            fofa = 0
                            print("dokončil si svoji práci")
                            money = money + 5
                if(cas == 2):
                    print("zmáčkni cokoliv pro pokračování")
                    input()
                    print("tvoje práce začala vyčkej 5 minut")
                    timejob2 = time.monotonic()
                    fofo = 1
                    time2while = time.monotonic()
                    while(fofo == 1):
                        int(input("cislo pro kontrolu"))
                        timejob2 = time.monotonic()
                        if(timejob2 >= time2while + 300):
                            fofo = 0
                            print("dokončil si svoji práci")
                            money = money + 20
                if(cas == 3):
                    print("zmáčkni cokoliv pro pokračování")
                    input()
                    print("tvoje práce začala vyčkej půl hodiny")
                    timejob3 = time.monotonic()
                    fofu = 1
                    time3while = time.monotonic()
                    while(fofu == 1):
                        int(input("cislo pro kontrolu"))
                        timejob3 = time.monotonic()
                        if(timejob3 >= time3while + 1800):
                            fofu = 0
                            print("dokončil si svoji práci")
                            money = money + 105
                            
                            
                        
            if(shop == 12):
                nav12 = nav12 + 1
                class Appl:

                    
                    def reset(self):
                       
                        global bosshp
                        global playerhp
                        global randboss
                        global money
                        randboss = randint(1,10)
                        playerhp = playerhp - randboss
                        randboss = randint(1,10)
                        bosshp = bosshp - randboss
                        print("máš ještě",playerhp,"životů")
                        print("boss má ještě",bosshp,"životů")
                        if(playerhp <= 0):
                            if(bosshp > 0):
                                print("boss tě porazil")
                                playerhp = 100
                                bosshp = 100
                                money = money - 70
                                print("máš pouze",money,"peněz")
                            if(bosshp <= 0):
                                print("remíza")
                                playerhp = 100
                                bosshp = 100
                        if(bosshp <= 0):
                            if(playerhp > 0):
                                print("porazil si bosse")
                                playerhp = 100
                                bosshp = 100
                                money = money + 100
                                print("máš",money,"peněz")
                            if(playerhp <= 0):
                                print("remíza")
                                playerhp = 100
                                bosshp = 100


                    
                    def __init__(self, master):

                        kocka = Frame(master)
                        kocka.pack()

                        self.hi_there = Button(kocka, text="attack", fg="green", command=self.reset)
                        self.hi_there.pack(side=LEFT)
                        
                        self.button = Button(kocka, text="KONEC", fg="red", command=master.destroy)
                        self.button.pack(side=LEFT)

                if __name__=="__main__":

                    root = Tk ()
                    app = Appl(root)
                    root.mainloop()    
            if(shop == 11):
                nav11 = nav11 + 1
                class Apph:
    
                    def rekni_ahoj(self):
                        
                        randomahoj = randint(1,5)
                        if(randomahoj == 1):
                            print("čus kámo")
                        if(randomahoj == 2):
                            print("dobrý den pane Profesore")
                        if(randomahoj == 3):
                            print("Čusák busák autobusák")
                        if(randomahoj == 4):
                            print ('Ahoj všici!')
                        if(randomahoj == 5):
                            print("Čus Voe")
                    

                    def vylepseni(self):
                       
                        global vyleps
                        vyleps = vyleps + 1
                        print ("vylepšení číslo:",vyleps )
                    
                    def rekni_ne(self):
                       
                        global pocgame1
                        pocgame1 = pocgame1 + vyleps
                        print ('klikl si',pocgame1,"x")
                    
                    def reset(self):
                       
                        global pocgame1
                        global money
                        money = money + pocgame1 / 1000
                        pocgame1 = 0
                        print ("zresetování počtu")
                        print("máš", money, "peněz")

                    
                    def rekord(self):
                        global reccord
                        global pocgame1
                        if(pocgame1 <= reccord):
                            print("rekord si nepřekonal")
                        if(pocgame1 > reccord):
                            reccord = pocgame1
                            print ("tvůj nový rekord je:", reccord)

                    
                    def __init__(self, master):

                        kocka = Frame(master)
                        kocka.pack()
                        global pocgame1
                        self.button = Button(kocka, text="KONEC", fg="red", command=master.destroy)
                        self.button.pack(side=LEFT)

                        self.hi_there = Button(kocka, text="Pozdrav!", fg="blue", command=self.rekni_ahoj)
                        self.hi_there.pack(side=LEFT)
                        
                        global pocgame1    
                        self.hi_there = Button(kocka, text="CLICK", fg="green", command=self.rekni_ne)
                        self.hi_there.pack(side=LEFT)
                        
                        self.hi_there = Button(kocka, text="reset", fg="red", command=self.reset)
                        self.hi_there.pack(side=LEFT)
                        
                        self.hi_there = Button(kocka, text="rekord", fg="orange", command=self.rekord)
                        self.hi_there.pack(side=LEFT)
                        
                        self.hi_there = Button(kocka, text="vylepseni", fg="pink", command=self.vylepseni)
                        self.hi_there.pack(side=LEFT)

                    




                if __name__=="__main__":

                    root = Tk ()
                    app = Apph(root)
                    root.mainloop()

            if(shop == 10):
                nav10 = nav10 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       OPISOVÁNÍ                            | |")
                print("   | |                       ČÍSEL                | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("vítej v přidané hře opisování čísel")
                print("každé kolo ti hra vypíše náhodné číslo")
                print("které musíš do 10 sekund opsat")
                print("když se ti to povede postupuješ do dalšího levelu, kde je číslo delší")
                print("když to do 10 sekund nezvládneš napíše ti hra, žes prohrál")
                print("když opíšeš číslo s chybou prohráváš též")
                print("až napíšeš jakékoliv číslo hra začne běžet")
                int(input())
                mocnina = 1
                while(unik == 0):
                    
                    
                    mucnina = 10 ** mocnina
                    micnina = 1 * 10 ** (mocnina - 1)
                    levelrand = randint(micnina,mucnina)
                    print(levelrand)
                    actualtime = time.monotonic()
                    stejne = int(input())
                    if(stejne == levelrand):
                        aftertime = time.monotonic()
                        casurovne = aftertime - actualtime
                        print("stihl si to za",casurovne, "sekund")
                        if(casurovne <= 10):
                            print("vyhral jsi pokracujeme")
                            mocnina = mocnina + 1
                        if(casurovne > 10):
                            unik = 1
                            print("prohrál si")
                    if(stejne != levelrand):
                        unik = 1
                        ach85 = ach85 + 1
                        print("nezvládl jsi opsat číslo")                    
                print("si pryč ze hry")
                unik = 0
                if(mocnina > 19):
                    print("dostal ses do", mocnina, "levlu výborná práce!")
                if(14 < mocnina < 20):
                    print("dostal ses do", mocnina, "levlu skvělá práce!")
                if(9 < mocnina < 15):
                    print("dostal ses do", mocnina, "levlu dobrá práce!")
                if(4 < mocnina < 10):
                    print("dostal ses do", mocnina, "levlu dostatečná práce!")
                if(0 < mocnina < 5):
                    print("dostal ses do", mocnina, "levlu hrozná práce!")
                money = money + mocnina ** 2
                monhad = mocnina ** 2
                print("získal jsi", monhad, "peněz")
                print("máš", money, "peněz")
                int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 9):
                nav9 = nav9 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       DIAMOND                              | |")
                print("   | |                       SHOP                 | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("vítej v diamond shopu")
                print("0 pro odchod")
                print("1 pro základní prodej")
                print("1 diamant za 100 money")
                print("2 pro speciální prodej")
                print("1 diamant za 300 nebo za nic")
                diahop = int(input())
                if(diahop == 0):
                    print("děkujeme za vaši návštěvu")
                    int(input("napis jakékoliv číslo pro pokračování"))
                if(diahop == 1):
                    print("kolik chces prodat diamantu", "mas jich", diamond)
                    pocdia = int(input())
                    if(pocdia < 0):
                        print("co to zkoušíš za kraviny")
                    if(pocdia > diamond):
                        print("tolik diamantů na prodej nemáš")
                        int(input("napis jakékoliv číslo pro pokračování"))
                    if(0 <= pocdia <= diamond):
                        money = money + pocdia * 100
                        diamond = diamond - pocdia
                        print("mas", money, "a", diamond, "diamantů")
                        int(input("napis jakékoliv číslo pro pokračování"))
                if(diahop == 2):
                    print("kolik chces prodat diamantu", "mas jich", diamond)
                    pocdias = int(input())
                    if(pocdias < 0):
                        print("nemůžeš prodat záporné diamanty")
                    if(pocdias > diamond):
                        print("co to zase zkoušíš?")
                        int(input("napis jakékoliv číslo pro pokračování"))
                    if(0 <= pocdias <= diamond):
                        diarand = randint(1,2)
                        if(diarand == 1):
                            print("litujeme, ale prohráváte")
                            money = money
                            diamond = diamond - pocdias
                            print("mas", money, "a", diamond, "diamantů")
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(diarand == 2):
                            print("litujeme, ale vyhráváte")
                            money = money + pocdias * 300
                            diamond = diamond - pocdias
                            print("mas", money, "a", diamond, "diamantů")
                            int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 8):
                nav8 = nav8 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       PRODEJ                               | |")
                print("   | |                       OBILÍ                | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("máš", obili, "obilí")
                print("aktuální cena 1 kusu obilí je", cenob)
                kolilí = int(input("kolik chces prodat obilí"))
                if(kolilí < 0):
                    print("tak to vážně ne!")
                if(kolilí > obili):
                    print("bohužel nemáš tolik obilí")
                    int(input("napis jakékoliv číslo pro pokračování"))
                if(0 <= kolilí <= obili):
                    celob = kolilí * cenob
                    print("prodal jsi", kolilí, "za celkovou cenu", celob, "peněz")
                    money = money + celob
                    print("tvá suma peněz je", money)
                    obili = obili - kolilí
                    print("zbylo ti", obili, "obilí")
                    int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 7):
                nav7 = nav7 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       GEM                                  | |")
                print("   | |                       LOTTERY              | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("máš", gems, "gemů")
                print("a",diamond, "diamantů")
                print("1 pro gem loterii")
                print("cena 2 gemy")
                if(gems < 2):
                    print("máš málo peněz")
                    int(input("napis jakékoliv číslo pro pokračování"))
                if(gems >= 2):
                    lot = int(input())
                    gems = gems - 2
                    if(lot == 1):
                        lotran = randint(1,3)
                        if(lotran == 1):
                            print("bohužel nic nevyhráváš")
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(lotran == 2):
                            print("vyhráváš 2 gemy")
                            gems = gems + 4
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(lotran == 3):
                            print("vyhráváš 100 money")
                            money = money + 100
                            int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 6):
                nav6 = nav6 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       OBCHOD                               | |")
                print("   | |                       S                    | |")
                print("   | |                PRACOVNÍKY                  | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("máš", money, "peněz k útratě")
                mist = pole * 3 - celkem
                print("mas", mist, "míst na pracovníky")
                prace = int(input("kolik chces koupit pracovníků"))
                if(prace < 0):
                    print("blbost")
                if(prace >= 0):
                    if(prace <= mist):
                        money = money - prace * 50
                        if(money < 0):
                            money = money + prace * 50
                            prace = 0
                            print("mas malo peněz")
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(money >= 0):
                            celkem = celkem + prace
                            print("celkem mas", celkem, "pracovniku")
                            int(input("napis jakékoliv číslo pro pokračování"))
                    if(prace > mist):
                        print("nemas dost mista musis koupit nove pole")
                        int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 5):
                nav5 = nav5 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       YOUR                                 | |")
                print("   | |                       STATS                | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("tvuj rekord je", rekord)
                xp = rekord * win + spewin * vzlepseni
                print("your experience level je",xp)
                print("největší množství peněz, který si kdy měl byl",record)
                suma = bank + money
                print("tvoje aktuální suma peněz je", suma)
                print("koupils", vzlepseni, "vylepšení")
                print("vyhrál jsi" , win, "her")
                print("vyhrál jsi" , spewin, "speciálních her")
                print("prohrál jsi" , lose, "her")
                print("prohrál jsi" , spelose, "speciálních her")
                print("tvůj rekord v idle clickru je", reccord)
                time.sleep(10)
            if(shop == 4):
                nav4 = nav4 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       ODHLAŠOVACÍ                          | |")
                print("   | |                       PORTÁL               | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("0 pro odhlášení")
                print("1 pro pokračování")
                f = int(input())
                int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 0):
                nav0 = nav0 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       NORMAL                               | |")
                print("   | |                       SHOP                 | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("mas", money, "peněz k útratě")
                print("0 pro hru")
                print("1 pro vylepseni")
                print("     ",cena, "money")
                print("2 pro speciální úroveň")
                print("      2000 money")
                print("3 pro speciální úroveň easy")
                print("      200 money")
                print("4 pro nové pole")
                print("      50 money")
                print("5 pro vylepšení pracovníků")
                print("     ",cenaprc, "money")
                print("6 pro skin shop")
                chces = int(input())
                if(chces == 6):
                    print("vítej ve skin shopu")
                    if(bubla == 0):
                        print("1 pro bubla skin za 500 money")
                    if(kámen == 0):
                        print("2 pro kámen skin za 1000 money")
                    if(lucifer == 0): 
                        print("3 pro lucifer skin za 1500 money")
                    if(hralyb == 0):
                        print("4 pro hralyb skin za 2000 money")
                    print("5 pro natural game skin number",ngs,"za",ngc,"money")
                    skin = int(input())
                    if(skin == 5):
                        if(ngc > money):
                            print("nemáš dost peněz")
                        if(ngc <= money):
                            print("koupil jsi skin za", ngc,"money")
                            money = money - ngc
                            ngc = ngc + 1000
                            ngs = ngs + 1
                            bonusmoney = bonusmoney + 1
                            print("máš ještě",money,"peněz")
                    if(skin == 1):
                        if(bubla == 1):
                            print("tento skin si již koupil")
                        if(bubla == 0):
                            if(money >= 500):
                                print("utratil jsi 500 money za tento skin")
                                bubla = bubla + 1
                                money = money - 500
                                print("zbylo ti",money, "money")
                                bonusmoney = bonusmoney + 1
                            if(money < 500):
                                print("máš málo peněz")
                    if(skin == 2):
                        if(kámen == 1):
                            print("tento skin si již koupil")
                        if(kámen == 0):
                            if(money >= 1000):
                                print("utratil jsi 1000 money za tento skin")
                                kámen = kámen + 1
                                money = money - 1000
                                print("zbylo ti",money, "money")
                                bonusmoney = bonusmoney + 1
                            if(money < 1000):
                                print("máš málo peněz")   
                    if(skin == 3):
                        if(lucifer == 1):
                            print("tento skin si již koupil")
                        if(lucifer == 0):
                            if(money >= 1500):
                                print("utratil jsi 1500 money za tento skin")
                                lucifer = lucifer + 1
                                money = money - 1500
                                print("zbylo ti",money, "money")
                                bonusmoney = bonusmoney + 1
                            if(money < 1500):
                                print("máš málo peněz")
                    if(skin == 4):
                        if(hralyb == 1):
                            print("tento skin si již koupil")
                        if(hralyb == 0):
                            if(money >= 2000):
                                print("utratil jsi 500 money za tento skin")
                                hralyb = hralyb + 1
                                money = money - 2000
                                print("zbylo ti",money, "money")
                                bonusmoney = bonusmoney + 1
                            if(money < 2000):
                                print("máš málo peněz")
                    int(input("zmackni jakekoli cislo pro pokracovani"))
                if(chces == 5):
                    if(cenaprc > money):
                        print("nemáš dost peněz na vylepšení")
                        int(input("napis jakékoliv číslo pro pokračování"))
                    if(cenaprc <= money):
                        print("právě si zlepšil své pracovníky")
                        zajednoho = zajednoho + 1
                        print("jeden pracovník pozbírá", zajednoho, "obilí")
                        money = money - cenaprc
                        cenaprc = cenaprc * 1.5
                        cenaprc = round(cenaprc,0)
                        print("zbylo ti", money, "peněz")
                if(chces == 1):      
                    if(money >= cena):
                        money = money - cena
                        print("zbylo ti", money, "peněz")
                        cena = cena * 2
                        vzlepseni = vzlepseni + 1
                        int(input("napis jakékoliv číslo pro pokračování"))
                    if(money < cena):
                        print("nemas dost peněz")
                        int(input("napis jakékoliv číslo pro pokračování"))
                if(chces == 2):
                    if(money >= 2000):
                        money = money - 2000
                        print("zbylo ti", money, "peněz")
                        special = int(input("vyber si cislo od 1 do 5"))
                        if(special < 1):
                            print("asi neumíš číst že?")
                            money = money + 2000
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(5 < special):
                            print("asi neumíš číst že?")
                            money = money + 2000
                            int(input("napis jakékoliv číslo pro pokračování"))
                        else:
                            print("vítej ve speciální úrovni")
                            rands = randint(0,6)
                            if(rands - 1 == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 4000
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            if(rands + 1 == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 4000
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            if(rands == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 4000
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            else:
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("prohrál si ztrácíš svých 2000 mincí")
                                print("mas", money, "penez")
                                spelose = spelose + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                    if(money < 2000):
                        print("nemáš dost peněz")
                        int(input("napis jakékoliv číslo pro pokračování"))
                if(chces == 4):
                    if(money >= 50):
                        print("kolik chceeš koupit polí")
                        pospol = int(input())
                        if(pospol < 0):
                            print("další blbost")
                        if(pospol >= 0):
                            money = money - 50 * pospol
                            print("zbylo ti", money, "peněz")
                            pole = pole + pospol
                            print("právě koupils", pole, ". pole")
                            int(input("napis jakékoliv číslo pro pokračování"))
                    if(money < 50):
                        chybi = (money - 50)*-1
                        print("máš málo peněz na další" , "chybí ti" , chybi)
                        int(input("napis jakékoliv číslo pro pokračování"))
                if(chces == 3):
                    if(money >= 200):
                        money = money - 200
                        print("zbylo ti", money, "peněz")
                        special = int(input("vyber si cislo od 1 do 5"))
                        if(special < 1):
                            print("asi neumíš číst že?")
                            money = money + 200
                            int(input("napis jakékoliv číslo pro pokračování"))
                        if(5 < special):
                            print("asi neumíš číst že?")
                            money = money + 200
                            int(input("napis jakékoliv číslo pro pokračování"))
                        else:
                            print("vítej ve speciální úrovni")
                            rands = randint(0,6)
                            if(rands - 1 == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 400
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            if(rands + 1 == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 400
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            if(rands == special):
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("vyhrál si speciální úroveň")
                                print("zde je tvá odměna")
                                money = money + 400
                                print("mas", money, "peněz")
                                spewin = spewin + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                            else:
                                while perce != 101:
                                    print ("loading ", perce, "%")
                                    perce = perce + 1
                                    time.sleep(0.01)
                                print("prohrál si ztrácíš svých 200 mincí")
                                print("mas", money, "penez")
                                spelose = spelose + 1
                                int(input("napis jakékoliv číslo pro pokračování"))
                    if(money < 200):
                        print("nemáš dost peněz")
                        int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 1):
                nav1 = nav1 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       STANDART                             | |")
                print("   | |                       GAME                 | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("dobre pokracujeme")
                int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 2):
                nav2 = nav2 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       ZMĚNA                                | |")
                print("   | |                       HESLA                | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                while(stare != a):
                    zmena = int(input("chces zmenit heslo zmackni 0 pokud ne zmackni 1"))
                    if(zmena == 0):
                        stare = int(input("stare heslo"))
                    if(stare == a):
                        print("spravne muzes zadat nove heslo")
                    if(stare != a):
                        ach69 = ach69 + 1
                        print("spatne heslo zkus znovu")
                    if(stare == a):
                        a = (int(input("nove heslo")))
                        stare = a
                    if(zmena == 1):
                        stare = a
                    int(input("napis jakékoliv číslo pro pokračování"))
            if(shop == 3):
                nav3 = nav3 + 1
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print("   | |       BANKA                                | |")
                print("   | |                INFO O TVÝCH ÚSPORÁCH       | |")
                print("   | |                                            | |")
                print("   | |                                            | |")
                print(" __| |____________________________________________| |__")
                print("(__   ____________________________________________   __)")
                print("   | |                                            | |")
                print("mas", money, "peněz")
                print("mas", bank, "peněz v bance")
                print("1 pro výběr")
                print("2 pro vklad")
                print("3 pro půjčku")
                print("4 pro zplacení půjčky")
                banka = int(input())
                if(banka == 4):
                    print("musiíš zplatit",urok,"peněz")
                    if(urok > money):
                        print("stále nemáš na zplacení")
                    if(urok <= money):
                        print("splatil si půjčku")
                        money = money - urok
                        print("zbylo ti",money,"money")
                        zplaceno = 1
                        urok = 0
                if(banka == 3):
                    if(urok != 0):
                        print("nemáš stále splacenou půjčku")
                    if(urok == 0):
                        print("5% úrok")
                        kolikpuj = int(input("kolik chces půjčit max 2000 money"))
                        if(kolikpuj > 2000):
                            print("takováta částka nemůže být půjčena")
                        if(kolikpuj < 0):
                            print("máš IQ rašící trávy")
                        if(0 <= kolikpuj <= 2000):
                            money = money + kolikpuj
                            print("máš",money,"peněz")
                            urok = kolikpuj * 1.05
                            print("musíš zplatit", urok, "do 20 kol")
                            caspuj = 20
                            zplaceno = 0
                if(banka == 1):
                    kolik = int(input("kolik chces vybrat"))
                    if(kolik > bank):
                        print("tolik peněz v bance nemáš vybrat nemůžeš")
                        int(input("napis jakékoliv číslo pro pokračování"))
                    if(kolik <= bank):
                        print("vybral jsi" , kolik, "peněz")
                        bank = bank - kolik
                        money = money + kolik
                        int(input("napis jakékoliv číslo pro pokračování"))
                if(banka == 2):
                    kolko = int(input("kolik chces vlozit"))
                    if(money < kolko):
                        print("mas malo peněz na vklad")
                    if(money >= kolko):
                        print("přesunul jsi do banky", kolko, "peněz")
                        money = money - kolko
                        bank = bank + kolko
                print("mas" , bank, "peněz v bance")
                print("mas" , money, "peněz")
                int(input("napis jakékoliv číslo pro pokračování"))
            perce = 0
            mezicas = round(time.monotonic(),1)
            print("hrál si zatím", round(mezicas - Cas_Start,1), "sekund")
            print("1 pro pokračování")
            print("0 pro vstup do shopu či banky, změnu hesla či odhlášení")
            print("mas", money, "peněz a v bance máš" , bank)
            gem = randint(1,10)
            if(gem == 10):
                gems = gems + 3
                print("získal si za toto kolo 1 gem")
            dia = randint(1,20)
            if(dia == 20):
                diamond = diamond + 1
                print("získal si za toto kolo 1 diamant")
            if(zplaceno == 0):
                caspuj = caspuj - 1
                print("půjčku musíš zplatit do", caspuj, "kol")
            if(zplaceno == 1):
                print("všechny půjčky zplaceny")
            if(caspuj == 0):
                urok = urok + urok
                print("musis zplatit ", urok, "money")
            if(caspuj == -20):
                urok = urok + urok
                print("nestihl si to do 40 kol")
            if(nav1 > 39):
                ach1 = ach1 + 1
            if(nav1 > 120):
                ach2 = ach2 + 1
            if(nav0 > 39):
                ach3 = ach3 + 1
            if(nav0 > 120):
                ach4 = ach4 + 1
            if(nav2 > 39):
                ach5 = ach5 + 1
            if(nav2 > 120):
                ach6 = ach6 + 1
            if(nav3 > 39):
                ach7 = ach7 + 1
            if(nav3 > 120):
                ach8 = ach8 + 1
            if(nav4 > 39):
                ach9 = ach9 + 1
            if(nav4 > 120):
                ach10 = ach10 + 1
            if(nav5 > 39):
                ach11 = ach11 + 1
            if(nav5 > 120):
                ach12 = ach12 + 1
            if(nav6 > 39):
                ach13 = ach13 + 1
            if(nav6 > 120):
                ach14 = ach14 + 1
            if(nav7 > 39):
                ach15 = ach15 + 1
            if(nav7 > 120):
                ach16 = ach16 + 1
            if(nav8 > 39):
                ach17 = ach17 + 1
            if(nav8 > 120):
                ach18 = ach18 + 1
            if(nav9 > 39):
                ach19 = ach19 + 1
            if(nav9 > 120):
                ach20= ach20 + 1
            if(nav10 > 39):
                ach21 = ach21 + 1
            if(nav10 > 120):
                ach22 = ach22 + 1
            if(nav11 > 39):
                ach23 = ach23 + 1
            if(nav11 > 120):
                ach24 = ach24 + 1
            if(nav12 > 39):
                ach25 = ach25 + 1
            if(nav12 > 120):
                ach26 = ach26 + 1
            if(nav13 > 39):
                ach27 = ach27 + 1
            if(nav13 > 120):
                ach28 = ach28 + 1
            if(nav15 > 39):
                ach66 = ach66 + 1
            if(nav15 > 120):
                ach67 = ach67 + 1
            if(money > 99):
                ach29 = ach29 + 1
            if(money > 999):
                ach30 = ach30 + 1
            if(money > 9999):
                ach31 = ach31 + 1
            if(money > 99999):
                ach32 = ach32 + 1
            if(money < 0):
                ach33 = ach33 + 1
            if(bank > 99):
                ach34 = ach34 + 1
            if(bank > 999):
                ach35 = ach35 + 1
            if(bank > 9999):
                ach36 = ach36 + 1
            if(bank > 99999):
                ach37 = ach37 + 1
            if(win > 9):
                ach38 = ach38 + 1
            if(win > 49):
                ach39 = ach39 + 1
            if(win > 99):
                ach40 = ach40 + 1
            if(spewin > 9):
                ach41 = ach41 + 1
            if(spewin > 49):
                ach42 = ach42 + 1
            if(spewin > 99):
                ach43 = ach43 + 1
            if(rekord > 4):
                ach44 = ach44 + 1
            if(rekord > 9):
                ach45 = ach45 + 1
            if(rekord > 19):
                ach46 = ach46 + 1
            if(rekord > 99):
                ach47 = ach47 + 1
            if(reccord > 1000):
                ach48 = ach48 + 1
            if(reccord > 10000):
                ach49 = ach49 + 1
            if(reccord > 25000):
                ach50 = ach50 + 1
            if(reccord > 500000):
                ach51 = ach51 + 1
            if(vzlepseni > 0):
                ach52 = ach52 + 1
            if(vzlepseni > 2):
                ach53 = ach53 + 1
            if(vzlepseni > 5):
                ach54 = ach54 + 1
            if(vzlepseni > 10):
                ach55 = ach55 + 1
            if(xp > 0):
                ach56 = ach56 + 1
            if(xp > 5):
                ach57 = ach57 + 1
            if(xp > 20):
                ach58 = ach58 + 1
            if(xp > 100):
                ach59 = ach59 + 1
            if(pole > 0):
                ach60 = ach60 + 1
            if(pole > 9):
                ach61 = ach61 + 1
            if(pole > 29):
                ach62 = ach62 + 1
            if(pole > 99):
                ach63 = ach63 + 1
            if(cenob > 0.15):
                ach64 = ach64 + 1
            if(cenob > 0.3):
                ach65 = ach65 + 1
            if(gems > 0):
                ach75 = ach75 + 1
            if(gems > 9):
                ach76 = ach76 + 1
            if(gems > 25):
                ach77 = ach77 + 1
            if(gems > 100):
                ach78 = ach78 + 1
            if(gems > 250):
                ach79 = ach79 + 1
            if(diamond > 0):
                ach80 = ach80 + 1
            if(diamond > 9):
                ach81 = ach81 + 1
            if(diamond > 25):
                ach82 = ach82 + 1
            if(diamond > 99):
                ach83 = ach83 + 1
            if(diamond > 250):
                ach84 = ach84 + 1
                
            print("aktuálně máš", obili, "obilí")
            print("aktuální cena obilí je", round(cenob,3))
            obili = obili + celkem * zajednoho
            cenob = cenob + randint(-5,10)/1000
            bank = bank * 1.001
            tele = int(input())
           
            
            q = a
