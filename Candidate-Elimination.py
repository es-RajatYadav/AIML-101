import csv
with open('trainingexamples.csv') as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
    specific = data[1][:-1]
    general = [["?" for i in range(len(specific))] for j in range(len(specific))]

    for i in data:
        if i [-1] == 'Yes':
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    specific[j] = "?"
                    general[j][j] = "?"
        elif i[-1] == 'No':
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = "?"
        k = 0
        print("Step {} of Candidate Elimination".format(k))
        print(specific)
        print(general)
        k += 1
    gh = []
    for i in general:
        for j in i:
            if j != "?":
                gh.append(i)
                break

    print("\nFinal Specific Hypothesis : ", specific)
    print("\nFinal General Hypothesis : ", gh)