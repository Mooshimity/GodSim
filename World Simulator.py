#Game of Life
#In game statistics based on real life
#V0.1
#Main Author Luke Dunn
#Others Involved
#youtube.com/user/Mooshimity (myemailistemporary@gmail.com) added x-23 lines of code
#youtube.com/user/Willbl3pic101 (william@williambl.com) added 23 lines of code
#someone else (xxx@email.com) added x lines of code
import time
import turtle
#import antigravity
from datetime import datetime
from random import randint

tag = 0
runs = 0
events = ''
now = datetime.now()
gametime = "%s/%s/%s" % (now.day, now.month, now.year) #setting time to IRL time
print("[Luke Dunn's Game of Life]")
time.sleep(0.1)
print
print("It is ",gametime)
#Temperature
print("[Select an average temperature of the region. (Celcius)]")
tmp = int(input())
tmps = tmp-21
ox = 20.946
co = 0.04
ni = 0.934
ar = 78.079
ot = 0.001
cos = co+0.96
tmpd = 1
tmpb = 1
gasbox = 1
gasdox = 1
print()
#Population
print("[Select an estimated population of the region. (1-1000)]")
ppl = int(input())
ppla = ppl
ppld = 0
pplb = 0
ppli = 0
print()
#Development
print("[Select a stage of development for the region. (1-5)]")
dlp = int(input())
print()
#Events
print("[Select the chance of a mass extinction event]")
meo = int(input('1 in '))
print()
#
#
#
print
active = 1
tcycle = 0
while active == 1:
    cycle = 1
    while cycle < runs+1:
        print(cycle)
        if events != '':
            print('MEE -',events,'dead')
            events = ''
        tcycle = tcycle+1 #Making the mass extinction event more rare
        cycle = cycle+1
        #Day
        print(gametime)
        #Add code to change day...
        #Atmosphere
        ##Temperature
        tmp = (tmp*1.00000000000924426)*cos #Carbon Dioxide emission makes the temperature higher.
        tmps = tmp-21
        if tmps < 0:
            tmps = tmps*-1
        tmpd = 1-(tmps/1000)
        tmpb = 1-(tmps/100)
        ##Gases
        co = co+(co*(dlp/100))
        if ox < 0:
            ox = 0
        if co < 0:
            co = 0
        if ni < 0:
            ni = 0
        if ar < 0:
            ar = 0
        if ot < 0:
            ot = 0
        if ox+co+ni+ar+ot > 100:  #Making sure that percentages are under 100 (gastemp is a temporary variable for gasses)
            gastemp = (ox+co+ni+ar+ot)-100
            gastemp = gastemp/5
            ox = ox-gastemp
            co = co-gastemp
            ni = ni-gastemp
            ar = ar-gastemp
            ot = ot-gastemp

        if ox < 5:
            gasbox = 0.5
            gasdox = 1.5
            if ox < 1:
                gasbox = 0
                ppla = 0
                ppld = ppl+pplb-ppla
        cos = co+0.96
        #Old births/deaths related to temperature code
        #tmpd = tmp*1.000476190476
        #tmpb = tmp*1.048
        #if tmpd < 0:
        #    tmpd = 2-tmp
        #if tmpb < 0:
        #    tmpb = 2-tmp
        #
        #
        #
        #
        #Population
        me = randint(1,meo)
        if ppl < 2.5:
            ppla = 0
            ppld = ppl
        if ppl > 1:
            ppld = ppld+(((ppla*0.00009)*tmpd)*gasdox)
            pplb = pplb+(((ppla*0.00019)*tmpb)*gasbox)
            ppla = ppl+int(round(pplb))-int(round(ppld))
        if ppla < 0:
            ppla = 0
        if pplb < 0:
            pplb = 0
        if ppla == 0:
            ppld = ppl+pplb
        if tcycle == randint(100,1000):
            #Mass Extinction
            if me == 1:
                events = (int(ppld))
                ppla = randint(0,ppla)
                ppld = ppl+pplb-ppla
                tcycle = 0
        time.sleep(1/runs)
    time.sleep(0.5)
    print()
    print("[Type /help <page number> for commands to display]")
    command = 1
    while command == 1:
        cmd,tag = input().split()
        ##Generic
        if cmd == '/help':
            try:
                tag = int(tag)
            except ValueError:
                print("Ah, the days of '/help potato'.")
        if cmd == '/help':
            print("##Generic")
            print("  /run <number of cycles>")
            print("  /help")
            print()
            print("##Stats")
            print("  /stats population")
            print("  /stats atmosphere")
            print("  /stats development")
            print()
            print("##Graph")
            print("  /graph population")
            print("  /graph atmosphere")
            print("  /graph development")
        if cmd == '/run':
            runs = int(tag)
            command = 0
        ##Stats
        if cmd == '/stats':
            if tag == 'population':
                print('Deaths:',int(round(ppld)))
                print('Alive: ',int(round(ppla)))
                print('Born:  ',int(round(pplb)))
                print()
            if tag == 'atmosphere':
                print('Temperature:',tmp,'*C')
                print()
                print('Carbon Dioxide %:',co)
                print('Radon %         :',ox)
                print('Nitrogen %      :',ni)
                print('Argon %         :',ar)
                print('Other %         :',ot)
                print()
        ##Graph
        if cmd == '/graph':
            if tag == 'population':
                turtle.speed(0)
                turtle.hideturtle()
                turtle.color('white')
                turtle.left(90)
                turtle.forward(ppl+pplb+ppld)
                turtle.left(90)
                turtle.right(180)
                turtle.color('black')
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(180)
                turtle.right(90)
                turtle.forward(10)
                turtle.left(90)
                turtle.color('red')
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppld))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppld))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.left(90)
                turtle.color('blue')
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(ppla))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(ppla))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.left(90)
                turtle.color('green')
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.forward(1)
                turtle.left(90)
                turtle.forward(int(pplb))
                turtle.right(90)
                turtle.forward(1)
                turtle.right(90)
                turtle.forward(int(pplb))
                turtle.left(90)
                turtle.color('black')
                turtle.forward(10)
                turtle.exitonclick()
