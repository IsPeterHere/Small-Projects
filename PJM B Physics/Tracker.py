import matplotlib.pyplot as plt
import numpy as np

def trk_file(file_name):
    with open(file_name) as f:
        data = f.read().splitlines()

    t = []
    x = []
    y = []
    for line in data[2:]:
        d = line.split(",")

        #s
        t.append(float(d[0]))

        #m
        x.append(float(d[1]))

        #m
        y.append(float(d[2]))

    return t,x,y


def graph(a,b,la,lb):
    plt.plot(a,b)
    plt.xlabel(la)
    plt.ylabel(lb)
    plt.show()


def calculate_g(t,y):
    dg = np.polyfit(t,y,2)
    ddg =  np.polyder(dg, m=2)
    return ddg


t,x,y = trk_file("data/PJMB2.csv")

print("value for g: ",calculate_g(t,y))

graph(t,x,"time(s)","Horizontal displacment(m)")
graph(t,y,"time(s)","Vertical displacment(m)")
graph(x,y,"Horizontal displacment(m)","Vertical displacment(m)")