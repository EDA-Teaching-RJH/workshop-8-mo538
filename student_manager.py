def add_student(name, age, grade):
    with open("students. txt", "a") as file:
        file.write(f"{name}, {age}, {grade}\n")

def display_students():
    try:
        with open("students.txt", "r") as file:
             for line in file:
                 print(line.strip())
    
    
    except FileNotFoundError:
        print("No student data found.")
    
def find_student(name):
    try:
        with open("students.txt", "r") as file:
             for line in file:
                 student = line.strip(). split(",")
                 if student [0] == name:
                    return f"Name:{student[0]}, Age: {student[1]}, Grade: {student[2]}"
        return "student not found"
    except FileNotFoundError:
        return "no student data found"
    

    if __name__ == "__main__":
        add_student("Ayo", 21, "A")
        add_student("emmanuel", 20, "B")
        display_students()
    print(find_students ("Ayo"))
    print(find_student("Tessa"))
    