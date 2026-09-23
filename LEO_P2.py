print("STUDENT ACTIVITY SCORE SYSTEM") 

Students = int(input("\nHow many students? "))

def Students_info ():
    L = str(input("Enter your name: "))
    E = float(input("Activity 1: "))
    O = float(input("Activity 2: "))
    R = float(input("Activity 3: "))

    return L, (E + O + R)/3

for i in range (Students):
    print("\nSTUDENT:", i + 1)
    L, Average = Students_info()

    if Average >= 90:
        Status = "Excellent"
    elif Average >= 80:
        Status = "Very Good"
    elif Average >= 75:
        Status = "Passed"
    else:
        Status = "Failed"



    print("\nSTUDENT REPORT")
    print("NAME: ", L)
    print("Average: ",round(Average, 2))
    print("Status: ", Status)

    
