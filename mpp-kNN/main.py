import math
import easygui
from statistics import mode


def create_set_table(file):
    temp_set_table = []
    with open(file, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            data = line.split(',')
            for d in data:
                if data.index(d) != (len(data) - 1):
                    d = float(d)
            temp_set_table.append(data)
    f.close()
    return temp_set_table


def count_distance(list1: list, list2: list):
    distance = 0
    for a in list1:
        if list1.index(a) != (len(list1) - 1):
            distance += math.pow(float(a) - float(list2[list1.index(a)]), 2)
    return distance


def find_most_frequent(fdistances_list: list):
    distances = []
    for set in fdistances_list:
        distances.append(set[1])
    distances.sort()

    min_distances = list(distances[0:k])
    closest = []
    for e in fdistances_list:
        if e[1] in min_distances:
            closest.append(e[0][-1])

    fmost_frequent = mode(closest)
    return fmost_frequent


print("Load a file with training data: ")
train_set_file = easygui.fileopenbox()
#train_set_file = "iris.data"
train_set_table = create_set_table(train_set_file)
print("Loaded file: " + train_set_file)
print("1 - Load a file with data to test\n2 - Enter data manually\nType number to select an option: ")
option = input()
while option not in ["1", "2"]:
    option = input("1 - Load a file with data to test\n"
                   "2 - Enter data manually\n"
                   "Incorrect input. Type one of the numbers above to select an option: ")
test_set_table = []
if option == "1":
    print("Load a file with data to test: ")
    test_set_file = easygui.fileopenbox()
    #test_set_file = "iris.test.data"
    print("Loaded file: " + test_set_file)
    test_set_table = create_set_table(test_set_file)
elif option == "2":
    trainset_columns = len(train_set_table[0])
    input_line = input("Add vector or type 'end' to finish: ")
    while input_line != "end":
        vector = input_line.split(",")
        if len(vector) == trainset_columns:
            vector_matching = 1
            for z in vector:
                if vector.index(z) != (len(vector) - 1):
                    try:
                        z = float(z)
                    except:
                        print(f"Incorrect vector format. Can't cast '{z}' to float")
                        vector_matching = 0
                        break
            if vector_matching == 1:
                test_set_table.append(vector)
                print(f'Added vector: {vector}')
        else:
            print("Incorrect vector length")
        input_line = input("Add vector or type 'end' to finish): ")

k = int(input("Enter the k parameter: "))

correct_guesses = 0
for z in test_set_table:

    distances_list = []
    for y in train_set_table:
        distances_list.append([y, count_distance(y, z)])

    most_frequent = find_most_frequent(distances_list)
    print(f'{z} classified as: {most_frequent}')

    if z[-1] == most_frequent:
        correct_guesses += 1
accuracy = correct_guesses / len(test_set_table) * 100
print(f'Algorithm was correct {correct_guesses} out of {len(test_set_table)} times.\nAccuracy: {accuracy}% ')
