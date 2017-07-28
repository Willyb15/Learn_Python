def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "multiplying %d * %d" % (a,b)
    return a * b
def divide(x,y):
    print "dividing %d and %d" % (x,y)
    return x / y

print "Lets do some math with the funcitons!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, wieght: %d, iq: %d" % (age, height, weight, iq)

# A puzzle for extra credit

print "Here is a puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand!?"
