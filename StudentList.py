# REMINDER:
# The .append is like putting the variable user input or the one you put into the parenthesis (), it will be added into the list
# You can create a null or empty like list, dictionary in square backets [] empty, and instantiate it to call upon the exevution

# REMINDER:
# The .append is like putting the variable user input or the one you put into the parenthesis (), it will be added into the list
# You can create a null or empty like list, dictionary in square backets [] empty, and instantiate it to call upon the exevution

scores = []
students = {}

decision = True

while decision:
    
    names = input("What are the Names: ").strip()
    students[names] = []
    scores = int(input("What are the scores: "))
    students[names].append(scores)
    decision = input("Is it final? [Y]: ").lower()
    if decision == 'n':
        continue
    elif decision == 'y':
        print(students)
        break
for names, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"The saved out put is: {names} {average}")
        

    
    