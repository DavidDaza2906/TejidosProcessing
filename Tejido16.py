x = 0
counter = 0
def setup():
    size(1000,1000)
    background(200,200,220)
def draw():
    lineas()
    
def lineas():
    global x
    global counter

    if x <= 250:
        delay(20)
        line(250,250,500+x,x)
        line(250,250,750-x,250+x)
        line(250,750,x,500-x)
        line(250,750,250+x,250+x)
        line(750,250,500+x,500+x)
        line(750,250,750+x,750-x)
        line(750,750,500-x,500+x)
        line(750,750,250+x,750+x)
        x += 7
        counter +=1
        if counter <=10:
            stroke(20,100,20)
        elif counter <=15:
            stroke(30,20,90)
        elif counter <=20:
            stroke(20,50,200)
        elif counter <=25:
            stroke(150,30,30)
        elif counter <= 30:
            stroke(30,20,90)
        elif counter <=35:
            stroke(228,232,59)
        else:
            counter = 0
    else:
        noLoop()
