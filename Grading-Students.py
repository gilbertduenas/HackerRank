def gradingStudents(grades):
    rounded = []

    for i in grades:
        r = i%10

        if i < 38:
            rounded.append(i)
        elif r > 2 and r < 5: 
            rounded.append(i-r+5)
        elif r > 7 and r < 10:
            rounded.append(i-r+10)
        else:
            rounded.append(i)

    return rounded
