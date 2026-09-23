print("STUDENT ACTIVITY SCORE SYSTEM") 

Students = int(input("\nHow many students? "))

def Students_info ():
    S_1 = str(input("Enter your name:"))
    A = float(input("Activity 1:"))
    B = float(input("Activity 2:"))
    C = float(input("Activity 3:"))

    return S_1, (A + B + C)/3

for i in range (Students):
    print("\nSTUDENT:", i + 1)
    S_1, Average = Students_info()

    if Average >= 90:
        Status = "Excellent"
    elif Average >= 80:
        Status = "Very Good"
    elif Average >= 75:
        Status = "Passed"
    else:
        Status = "Failed"



    print("STUDENT REPORT")
    print("\nNAME: ", S_1)
    print("Average: ",round(Average, 2))
    print("Status: ", Status)

    
