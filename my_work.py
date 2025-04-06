# Aubrey Schrameck
# CSCI 128 Section K


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

    # close finished files
    file.close()
    clean_file.close()


def isolate_depression():
    # 
    depression_items = [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]
    for i in range(len(depression_items)):
        num = int(depression_items[i]) - 1
        depression_items = depression_items[:i] + [num] + depression_items[i+1:]
    d_file = open("depression.csv", "w")
    for line in clean_lines:
        row = line.split(",")
        new_line = []
        for j in range(len(row)):
            if j in depression_items:
                new_line.append(row[j])
        new_line = (str(new_line))[1:-4].replace("'", "")
        d_file.write(f"{new_line}\n")


def isolate_anxiety():
    anxiety_items = [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]
    for i in range(len(anxiety_items)):
        num = int(anxiety_items[i]) - 1
        anxiety_items = anxiety_items[:i] + [num] + anxiety_items[i+1:]
    d_file = open("anxiety.csv", "w")
    for line in clean_lines:
        row = line.split(",")
        new_line = []
        for j in range(len(row)):
            if j in anxiety_items:
                new_line.append(row[j])
        new_line = (str(new_line))[1:-1].replace("'", "")
        d_file.write(f"{new_line}\n")


def isolate_stress():
    stress_items = [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]
    for i in range(len(stress_items)):
        num = int(stress_items[i]) - 1
        stress_items = stress_items[:i] + [num] + stress_items[i+1:]
    d_file = open("stress.csv", "w")
    for line in clean_lines:
        row = line.split(",")
        new_line = []
        for j in range(len(row)):
            if j in stress_items:
                new_line.append(row[j])
        new_line = (str(new_line))[1:-2].replace("'", "")
        d_file.write(f"{new_line}\n")


def close_files():
    file.close()
    clean_file.close()


if __name__ == '__main__':
    file = open(r"C:\Users\aubre\OneDrive\Desktop\128\final project\data.csv", "r")
    header = (file.readline()[:-1]).split("\t")
    lines = file.readlines()[0:]
    isolateA()
    clean_file = open(r"C:\Users\aubre\OneDrive\Desktop\128\final project\clean_data.csv", "r")
    clean_lines = clean_file.readlines()[1:]
    isolate_depression()
    isolate_anxiety()
    isolate_stress()

    close_files()
