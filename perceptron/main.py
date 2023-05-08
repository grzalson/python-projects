from tkinter import filedialog


def create_set_table(file: str, f_first_decisive: str):
    temp_set_table = []
    with open(file, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            f_vector = line.split(',')
            for value in f_vector:
                if f_vector.index(value) != (len(f_vector) - 1):
                    value = float(value)
                else:
                    if value == f_first_decisive:
                        f_vector[-1] = 1
                    else:
                        f_vector[-1] = 0
            temp_set_table.append(f_vector)
        f.close()
    return temp_set_table


def read_first_decisive(path: str):
    with open(path, 'r') as f:
        return f.readline().split(',')[-1].strip()


def count_distance(vector1: list, vector2: list):
    distance = 0
    index = 0
    while index < len(vector1) - 1:
        distance += (float(vector1[index]) - float(vector2[index])) ** 2
        index += 1
    return distance


print("Load a file with training data: ")
train_set_file = filedialog.askopenfilename()
first_decisive = read_first_decisive(train_set_file)
train_set_table = create_set_table(train_set_file, first_decisive)
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
    test_set_file = filedialog.askopenfilename()
    print("Loaded file: " + test_set_file)
    test_set_table = create_set_table(test_set_file, first_decisive)
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
                else:
                    if z == first_decisive:
                        vector[-1] = 1
                    else:
                        vector[-1] = 0
            if vector_matching == 1:
                test_set_table.append(vector)
                print(f'Added vector: {vector}')
        else:
            print("Incorrect vector length")
        input_line = input("Add vector or type 'end' to finish): ")

deviation = 0.1
