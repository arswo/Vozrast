def checkAge():
    age = input("vvedi vozrast: ")
    if not age.isdigit():
        print("Введи нормально")
        return

    age = int(age)
    if age == 18:
        print('ti norm')

    elif age >= 19:
        print ('you big boy')

    elif age <= 17:
        print ('you small boy')

checkAge()
