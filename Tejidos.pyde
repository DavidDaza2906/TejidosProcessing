
deg = 0
degb = 0
counter = 0
    
def setup():
    size(1000,1000)
    background(0)    
def draw():
    lineas()
    borde()
    
    
def lineas():
    global deg
    global counter
    if deg <= 360:
        strokeWeight(1)
        delay(20)
        deg +=2
        radio =450
        angulo = radians(deg)
        deg1 = radians(30)
        x = 500 + (cos(angulo)*radio)
        y = 500 + (sin(angulo) * radio)
        x1 = 500 - (sin(-angulo+deg1)*radio)
        y2 = 500 - (cos(-angulo+deg1) * radio)
        counter +=1
        #line(x,y,x1,y2)
        if counter <= 10:
            stroke(39,201,151)
            line(x,y,x1,y2)
        elif counter <= 20:
            stroke(127,39,201)
            line(x,y,x1,y2)
        elif counter <= 30:
            stroke(106,42,57)
            line(x,y,x1,y2)
        else:
            counter = 0
    
    else:
        noLoop()
def borde():
    global degb
    if deg <= 360:
        stroke(500,500,500)
        degb +=3
        radio =450
        angulo = radians(degb)
        deg1 = radians(2)
        z= 500 +(cos(angulo)*radio)
        p =500 + (sin(angulo) * radio)
        strokeWeight(2)
        z1 = 500 +(cos(angulo+deg1)*radio)
        p1 = 500 + (sin(angulo+deg1) * radio)
        line(z,p,z1,p1)
    else:
        noLoop()
