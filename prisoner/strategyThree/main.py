import random
# Testing the library
# print(random.randint(1,100))
box = list(range(1,101))
file = open('SimulationResult.txt','a') #####projects\prisoner\strategyOne\
simulation_result = [] # To store the simulation results
# Running the simulation for TEN THOUSAND TIMES times
for loop in range (0,10000):
    # create a dictionary where the keys will indicate the box number \
    # and the values will indicate the slip containing the prisoner's number
    box_with_slip = {}
    flag_for_prisoner = [] # This list stores true or false depending on success or failure of the prisoner
    random.shuffle(box)  # Shuffle the list of prisoner numbers
    for i in range(1, 101):
        box_with_slip[i] = box[i - 1]  # Assign shuffled prisoner numbers to boxes
    # Each prisoner making a choice
    prisoner_id = 1
    while(prisoner_id < 101):
        temp = prisoner_id
        for attempt_count in range(50):
            if prisoner_id == box_with_slip[temp]:
                flag_for_prisoner.append(True)
                break
            elif prisoner_id <= 50:
                temp += 1
            elif prisoner_id >=51:
                temp -=1
        prisoner_id += 1
    if len(flag_for_prisoner) == 100:
        file.write('Simulation Successful\n')
    else:
        file.write('Simulation Failed\n') # instead of printing the result, storing the result in a text file
file.close()
print('Simulation completed')