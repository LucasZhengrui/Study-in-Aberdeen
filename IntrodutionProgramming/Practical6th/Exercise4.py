def security(mes):
    if mes == "X":
        mes = "A"
        return mes
    elif mes == "Y":
        mes = "B"
        return mes
    elif mes == "Z":
        mes = "C"
        return mes
    else:
        mes = ord(mes) + 3
    return chr(mes)

while 1:
    mes = input("Please inpiut your message: ")
    if mes != " ":
        print(security(mes))
    else:
        break
