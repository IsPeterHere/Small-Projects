import matplotlib.pyplot as plt
import math

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

    time_samples = []

    above = False
    avg = -0.4

    for v in range(len(y)):
        if above:
            if y[v] < avg:
                above = False
        else:
            if y[v] > avg:
                above = True
                time_samples.append(t[v])

    T = 1.4

    w = (2*math.pi)/T

    g = 0.5*(w**2)

    return g


t,x,y = trk_file("data/SHM B Wide.csv")

print("value for g: ",calculate_g(t,y))

graph(t,x,"time(s)","Horizontal displacment(m)")
#graph(t,y,"time(s)","Vertical displacment(m)")
#graph(x,y,"Horizontal displacment(m)","Vertical displacment(m)")