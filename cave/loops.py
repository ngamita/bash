#! usr/bin/python
"""
Given a color as input you'll have to output the personality of the person as follows.

		VIOLET	->	optimistic
		INDIGO	->  independent
		BLUE    ->  practical
		GREEN   ->  conservative
		YELLOW  ->  trustworthy 
		ORANGE  ->  reliable 
		RED     ->  loving 
"""

color = ""
while(color != "exit"):
    # print("please enter color:")
    
    #color = "RED"

    if(color == "violet"):
        print("optimistic")
    elif (color == "indigo"):
        print "independent"
    elif(color == "blue"):
        print("practical")
    elif(color == "green"):
        print("conservative")
    elif(color == "yellow"):
        print("trustworthy")
    elif(color == "orange"):
        print("reliable")
    elif(color == "red"):
        print("loving")
    else:
        print("Sorry, we didn't understand that color!")
    color = raw_input('Please enter color: ').lower()

"""
names = "ngamita"
len(names)
i = 0
while(i < len(names)):
    print names[i]
    i+=1"""
