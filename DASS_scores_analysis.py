import matplotlib.pyplot as plt


def isolateA():
    # isolate answer columns
    columns = []
    for i in range(len(header)):
        if header[i][-1] == "A":
            columns.append(i)
    clean_file = open("clean_data.csv", "w")
    clean_file.write(f"{columns}\n")

    # write a clean data file with just the answers to each question
    for line in lines:
        row = line.split("\t")
        new_line = []
        for j in range(len(row)):
            if j in columns:
                new_line.append(row[j])
        new_line = (str(new_line))[1:-2].replace("'", "")
        clean_file.write(f"{new_line}\n")


def isolate_illness(items):
    # subtract 1 from each item in the question list
    new_items = []
    for i in range(len(items)):
        num = int(items[i]) - 1
        new_items = new_items + [num]

    # generate name for file
    if items[0] == 1:
        name = "Stress"
    elif items[0] == 2:
        name = "Anxiety"
    elif items[0] == 3:
        name = "Depression"
    else:
        name = "error"
    i_file = open(f"{name}.csv", "w")

    # isolate answers to the illness-specific illness and clean up the file
    for line in clean_lines:
        row = line.split(",")
        new_line = []
        for j in range(len(row)):
            if j in new_items:
                new_line.append(row[j])
        new_line = (str(new_line)).replace("'", "")
        if name == "Depression":
            new_line = new_line[1:-3]
        else:
            new_line = new_line[1:-1]
        i_file.write(f"{new_line}\n")


def remove_healthy(illness, min, name):
    # calculate each persons score
    scores = []
    total = 0
    for line in illness:
        total = 0
        row = line.split(",")
        for i in range(len(row)):
            total = total + int(row[i])
        scores.append(total)

    # create a list of the row numbers of everyone who doesnt meet the minimum score
    healthy = []
    for i in range(len(scores)):
        if scores[i] <= min:
            healthy.append(i)

    # remove those individuals from the dataset
    count = 0
    final_file = open(f"{name}.csv", "w")
    for x in illness:
        if count in healthy:
            count = count + 1
        else:
            count = count + 1
            final_file.write(f"{x}")


def averages(items, file):
    # determine which illness to consider
    if items[0] == 1:
        name = "Stress"
    elif items[0] == 2:
        name = "Anxiety"
    elif items[0] == 3:
        name = "Depression"
    else:
        name = "error"
    print(f"Average Scores for {name}:")

    # print the average score of each question
    averages = []
    for i in range(len(items)):
        total = 0
        count = 0
        for line in file:
            row = line.split(",")
            total = total + int(row[i])
            count = count + 1
        print(f"{items[i]}: {round((total / count), 2)}")
        averages = averages + [total / count]

    # create graphs
    plt.bar(items, averages)
    plt.xlabel("Question Number")
    plt.ylabel("Average Answer")
    plt.title(f'Average Answers for Individuals with {name}')
    plt.savefig(name)
    plt.show()

    # clearing the plot
    plt.clf()


def close_files():
    file.close()
    clean_file.close()
    d_file.close()
    a_file.close()
    s_file.close()
    d_final_file.close()
    a_final_file.close()
    s_final_file.close()


if __name__ == '__main__':
    # open main file
    file = open("data.csv", "r")
    header = (file.readline()[:-1]).split("\t")
    lines = file.readlines()[0:]
    isolateA()

    # open clean file
    clean_file = open("clean_data.csv", "r")
    clean_lines = clean_file.readlines()[1:]

    # list of question numbers for each illness
    depression_items = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    anxiety_items = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    stress_items = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]

    isolate_illness(depression_items)
    d_file = open("Depression.csv", "r")
    d_lines = d_file.readlines()
    isolate_illness(anxiety_items)
    a_file = open("Anxiety.csv", "r")
    a_lines = a_file.readlines()
    isolate_illness(stress_items)
    s_file = open("Stress.csv", "r")
    s_lines = s_file.readlines()

    # calculate scores for each illness
    remove_healthy(d_lines, 9, "Depression-Final")
    d_final_file = open("Depression-Final.csv", "r")
    d_final_lines = d_final_file.readlines()
    remove_healthy(a_lines, 7, "Anxiety-Final")
    a_final_file = open("Anxiety-Final.csv", "r")
    a_final_lines = a_final_file.readlines()
    remove_healthy(s_lines, 14, "Stress-Final")
    s_final_file = open("Stress-Final.csv", "r")
    s_final_lines = s_final_file.readlines()

    # calculate the average score for each question
    averages(depression_items, d_final_lines)
    averages(anxiety_items, a_final_lines)
    averages(stress_items, s_final_lines)

    close_files()
