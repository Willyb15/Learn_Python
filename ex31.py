print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "Theres a bear. What do you do?"
    print "1. Take the Cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face boff"
    elif bear =="2":
        print "The bear eats your legs off"

    else:
        print "well %s is better" % bear

elif door == "2":
    print "suckit"
