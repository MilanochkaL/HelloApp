
print("Hello Python from Visual Studio!")
s = "/\\"*30
print(s)
print("New project")
print(s)
while True:
    try:
        import datetime

        date1 = datetime.datetime.strptime(input("������� 1 ���� ������� dd.mm.yyyy: "), "%d.%m.%Y")
        date2 = datetime.datetime.strptime(input("������� 2 ���� ������� dd.mm.yyyy:"), "%d.%m.%Y")
        if (date1 < date2):
            print("yes")
        else:
            print("no")
        break
    except ValueError:
        print("������������ ����")
