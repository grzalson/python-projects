def create_set_table(file):
    temp_set_table = []
    with open(file, 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            f_vector = line.split(',')

            temp_set_table.append(f_vector)
        f.close()
    return temp_set_table


def smooth(counter):
    cases = []
    for e in train_table:
        if e[i] not in cases:
            cases.append(e[i])
    return 1 / (counter + len(cases))


train_set_file = "agaricus-lepiota.test.data"
train_table = create_set_table(train_set_file)

data_file = "agaricus-lepiota.data"
data_table = create_set_table(data_file)

p_total = 0
e_total = 0
for e in train_table:
    if e[0] == 'p':
        p_total += 1
    elif e[0] == 'e':
        e_total += 1

correct = 0
tp = 0
fp = 0
fn = 0
for y,vec in enumerate(data_table):
    p_prob = p_total / len(train_table)
    e_prob = e_total / len(train_table)

    for i, x in enumerate(vec):
        if i == 0:
            continue
        p_instances = 0
        e_instances = 0
        for _vec in train_table:
            if _vec[0] == 'p' and _vec[i] == x:
                p_instances += 1
            elif _vec[0] == 'e' and _vec[i] == x:
                e_instances += 1
        a = p_instances / p_total
        b = e_instances / e_total
        if p_instances == 0:
            a = smooth(p_total)
        if e_instances == 0:
            b = smooth(e_total)
        p_prob = p_prob * a
        e_prob = e_prob * b

    if p_prob > e_prob:
        if vec[0] == 'p':
            correct += 1
            tp += 1
        else:
            fp += 1
    elif p_prob < e_prob:
        if vec[0] == 'e':
            correct += 1
        else:
            fn += 1
precyzja = tp / (tp + fp)
pelnosc = tp / (tp + fn)
print(f"{correct} out of {len(data_table)} correct\naccuracy: {correct/len(data_table)*100}")
print(f"precyzja: {precyzja * 100}")
print(f"pełność: {pelnosc * 100}")
print(f"F-miara: {(2 * (precyzja * pelnosc) / (precyzja + pelnosc)) * 100}")




