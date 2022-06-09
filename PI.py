import turtle as tu

lines = 1_000_000

with open("PIMillion.txt", "r") as f:
    pi = f.read()

tu.mode("logo")
tu.tracer(False)
tu.screensize(5000,5000,'black')
tu.colormode(255)

for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255-int((color/2)),255-color,color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation) 
    tu.forward(2)
    if n % 10_000 == 0:
        tu.update()

tu.getcanvas().postscript(file='PI_picture')
tu.done()

print(len(pi))
print(pi[0:10])
#print(pi[999_991:1_000_001]) 
print(pi[-10:])