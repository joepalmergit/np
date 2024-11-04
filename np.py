import sys
import time
import random


def read_file(filename):
    contents = []

    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            contents.append(line)

    return contents


names_file = sys.argv[1]

names = read_file(names_file)

try:
    selected_names = read_file("selected_names.txt")

except FileNotFoundError:
    file = open("selected_names.txt", "w")
    file.close()

    selected_names = read_file("selected_names.txt")

if selected_names:
    for selected_name in selected_names:
        if selected_name in names:
            names.remove(selected_name)

print(f"Students remaining: {len(names)}")
print("Selecting a student...")

time.sleep(5)

student = random.choice(names)

print(f"Selected {student}!")

with open("selected_names.txt", "a") as file:
    file.write(f"{student}\n")
