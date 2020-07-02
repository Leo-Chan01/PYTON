#maximum number of scores to be inputed
max = 1000
#empty high scores list
high_scores = []
#welcome message
print("welcome, press Y or any key to start, 0 when done! and N to end the application" )
while (input(">>")).title() !='N':
    print("input the scores below:")
    #ask for user to input score
    while len(high_scores) < max:
        curr_score = int(input())
        #check if the inputed score is the highest by sorting them from lowest to highest for each input
        if curr_score > 0:
            high_scores.append(curr_score)
            sorted(high_scores)
        else:
            break
    #display the highest score and the recently inputed score
    highest = sorted(high_scores)
    print("the highest score is... {}\n".format(highest[-1]))
    if curr_score != 0:
        print("the current score inputed is... {}".format(curr_score))
    else:
        print("the current score inputed is... {}".format(high_scores[-1]))
    print("try again?")
print("goodbye!!!")