#Madlibs credit: http://www.teach-nology.com/worksheets/language_arts/madlibs/1/

#Print an introduction
print "Welcome to MadLibs. Enter a series of words and I'll give you a silly story!"

#Ask the user for all the variables
#Have to set: adjective1 through 5, animal1, animal2, food1, food2, verb, ptverb (a past tense verb)
adjective1 = raw_input("Enter an adjective: ")
adjective2 = raw_input("Enter an adjective: ")
adjective3 = raw_input("Enter an adjective: ")
adjective4 = raw_input("Enter an adjective: ")
adjective5 = raw_input("Enter an adjective: ")
animal1 = raw_input("Enter an animal: ")
animal2 = raw_input("Enter an animal: ")
food1 = raw_input("Enter a food item: ")
food2 = raw_input("Enter a food item: ")
verb = raw_input("Enter a verb: ")
ptverb = raw_input("Enter a past tense verb: ")

#print out the result
print "" #blank line
print "Today I went to the zoo. I saw a", adjective1, animal1, "jumping"
print "up and down in its tree. He",ptverb, "through the large"
print "tunnel that led to its", adjective2, "cage. I got a", food1
print "and passed it through the cage to a gigantic", adjective3, animal2
print "towering over my head. Feeding that animal made me hungry. "
print "I went to get a", adjective4,"scoop of", food2 +". Afterwards I had to"
print verb, "to catch our bus. It was a", adjective5, "day at the zoo!"
