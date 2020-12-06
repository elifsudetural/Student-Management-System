name ="Elif Sude"
surname="Tural"

counter = 0

def check():
    global counter
    inputname = input("Enter name:  ")
    inputsurname = input("Enter surname:  ")
    if (name != inputname or surname != inputsurname):
        counter += 1
        print("Name or surname incorrrect.")
    else:
        print("Welcome")
        counter = 99 #loopun durması için
        
    if (counter == 3):
        print("try again")

while (counter < 3):
    check()

counter1 = 0
courses = ["Math", "Physics", "Computer Science", "Chemistry", "Economics"]

print("Please choose one of the courses below. (min:3, max:5)")
for course in courses:
    print(course)

selectedcourses = []

while (len(selectedcourses) < 3):
    selected = input("Enter course: ")
    if selected in courses and selected not in selectedcourses:
        selectedcourses.append(selected)
        print("Course successfully added.")
    elif selected == "":
        print("You should enter more than 3 courses to pass the class. ")
        answer = input("If you are sure, leave blank again. If you want to continue to take course, type something.")
        if answer == "":
            print("You failed class.")
        elif answer in courses and answer not in selectedcourses:
            selectedcourses.append(selected)
            print("Course successfully added.")
        
    else:
        print("Please enter a valid course.")

print("From now on, courses are optional. Leave blank if you do not want to get them.")

counter2 = len(selectedcourses)

while (len(selectedcourses) < 5):
    extracourse = input("Enter course: ")
    if extracourse in courses and  extracourse not in selectedcourses: 
        selectedcourses.append(extracourse)
        print("Course successfully added.")
    elif extracourse == "":
        print("Okay.")

    else:
        print("Please enter a valid course.")
print("Courses added.")


while(True): 
    examcourse = input("Choose one of the courses you have to take exam. ")   
    if examcourse in selectedcourses:
            print("Course successfully selected.")
            break
    else:
        print("Please enter a valid course.")


grades = {
  "midterm": 60,
  "final": 50,
  "project": 70,
}
print(grades)

averagegrade =  ((60* grades["midterm"]/100) + (50*grades["final"]/100) + (70*grades["project"]/100))/3

if averagegrade>90:
    print("Your score is AA")
elif 70<averagegrade<90 :
    print("Your score is BB")
elif 50<averagegrade<70 :
    print("Your score is CC")
elif 30<averagegrade<50 :
    print("Your score is DD")
elif 0<averagegrade<30:
    print("Your score is FF. You failed the class.")