def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You hcae %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man thats enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly"
cheese_and_crackers(20,30)

print "Or we can use varibales from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do Math inside too"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and MAth"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 2000)
