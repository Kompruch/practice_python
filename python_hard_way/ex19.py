def chesse_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print("You have {} box of crackers!".format(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
chesse_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = int(input('amount_of_cheese'))
amount_of_crackers = int(input('amount_of_crackers'))

chesse_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
chesse_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
chesse_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)