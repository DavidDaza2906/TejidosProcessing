import math
i=0
s=100*math.sqrt(3)
#vertices de los triángulos
T=[[200,s,300,0,400,s],
   
   [200,s,0,1*s,100,2*s],
   [200,s,300,2*s,100,2*s],
   [200,s,300,2*s,400,1*s],
   [500,2*s,300,2*s,400,1*s],
   [500,2*s,600,s,400,1*s],
   
   [200,3*s,0,3*s,100,2*s],
   [200,3*s,300,2*s,100,2*s],
   [200,3*s,300,2*s,400,3*s],
   [500,2*s,300,2*s,400,3*s],
   [500,2*s,600,3*s,400,3*s],
     
   [200,3*s,300,4*s,400,3*s]

]
def setup():
    background(0)
    size(600,693)
def draw():
    Segmentos()
   
def Segmentos():
        global i #contador globa;
        global T
        k=25
        s=100*math.sqrt(3)
        if i  <= k :
            delay(50)
            for j in T:  
                p=[j[0]]+[j[1]]
                q=[j[2]]+[j[3]]
                r=[j[4]]+[j[5]]
                x=p+q+r
                #Partes blancas del triángulo
                stroke(250)
                line(x[0]+(x[2]-x[0])*i/k,x[1]+(x[3]-x[1])*i/k,x[4]+(x[0]-x[4])*i/k,x[5]+(x[1]-x[5])*i/k)
                #cambiar el orden de los vértices
                x=r+p+q
                stroke(250)
                line(x[0]+(x[2]-x[0])*i/k,x[1]+(x[3]-x[1])*i/k,x[4]+(x[0]-x[4])*i/k,x[5]+(x[1]-x[5])*i/k)
                #cambiar el orden de los vértices
                x=q+r+p
                #Parte amarilla del triángulo
                stroke(250,200,0)
                line(x[0]+(x[2]-x[0])*i/k,x[1]+(x[3]-x[1])*i/k,x[4]+(x[0]-x[4])*i/k,x[5]+(x[1]-x[5])*i/k)
             
            i +=1
        else:
             noLoop()
