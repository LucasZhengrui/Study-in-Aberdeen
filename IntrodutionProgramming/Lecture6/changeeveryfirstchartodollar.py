str = "In this folder you will find the course guide, with essential information such as the intended learning outcomes, content, assessment information, staff contact details, indicative timetable."

str_ = str[0]

for i in range(1, len(str)):
    if str[i - 1] == " ":
        str_ += "$"
    else:
        str_ += str[i]

print(str_)
