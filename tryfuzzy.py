list1=["silk", "lightly soiled", "10 to 15kg"]
def result():
#Silk
    print("——")
    print("OUTPUT")
    print("——")
    #Rule 1:
    if((list1[0]=="silk")and(list1[1]=="lightly soiled")and(list1[2]=="below 10kg")):#1
        print("Wash Duration - 0.35 h")
        print("Temperature - 30c")
        print("RPM - 400")
        print("Dry Time - Quick")
        print("Quality - Good")
        input("Press Enter key to exit...")
    #Rule 2:
    elif((list1[0]=="silk")and(list1[1]=="lightly soiled")and(list1[2]=="10 to 15kg")):#2
        print("Wash Duration - 0.47 h")
        print("Temperature - 30c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Good")
        input("Press Enter key to exit...")
    #Rule 3:
    elif((list1[0]=="silk")and(list1[1]=="lightly soiled")and(list1[2]=="above 15kg")):#3
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Best")
    else:
        print("woopsie")
    input("Press Enter key to exit...")

result()