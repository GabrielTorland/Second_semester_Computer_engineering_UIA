from Function import menu, student, your_info, add_students, edit_student, delete_student

def main():
    while True:
        menu()
        c = str(input("Option [1-6]: "))

        if c == "1":
            student()
        elif c == "2":
            your_info()
        elif c == "3":
            add_students()
        elif c == "4":
            edit_student()
        elif c == "5":
            delete_student()
        else:
            break


if __name__ == '__main__':
    main()
