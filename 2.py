# Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.

letter = str(input("podaj litere: "))
if 'a' <= letter <= 'z' :
    print("Litera jest mała")
elif 'A' <= letter <= 'Z' :
    print("Litera jest duża")
else :
    print("Ten symbol nie jest litera")