class admin:
    def role(self):
        print("1.ADMIN:  ")
        print("2.STAFF: ")
        print("3.STUDENT:  ")
        print()
        print()
        self.role1 = int(input(' '))
        p.l()

    def l(self):
        if (self.role1 == 2 or self.role1 == 3):
            print()
            print()
            print("1 LOGIN:  ")
            print("2 SIGN UP:  ")
            print()
            print()
            self.l1 = int(input(" "))
            if (self.l1 == 1):
                p.login()
            else:
                p.application()
        else:
            p.login()

    def login(self):
        if (self.role1 == 1):
            x = open("python/project/admin.txt", "r")
            y = x.read()
            y = y.split(",")
            x.close()
            l = len(y)
            print()
            print()
            name = str(input("Enter your username:"))
            passw = str(input("Enter the password:"))
            for i in range(0, l, 2):
                if (y[i] == name):
                    flag = 1
                    temp = i
                    break
                if (i == (l - 2)):
                    print()
                    print()
                    print("Incorrect username!!")
                    p.login()
                    return 0
            if (y[temp + 1] == passw):
                print()
                print()
                print("Login successfull!!")
                p.admina()
                return 1
            else:
                print()
                print()
                print("Incorrect password!!")
                p.login()
                return 0
        if (self.role1 == 2):
            x = open("python/project/stafflogin.txt", "r")
            y = x.read()
            y = y.split(",")
            x.close()
            l = len(y)
            print()
            print()
            name = str(input("Enter your username:"))
            passw = str(input("Enter the password:"))
            for i in range(0, l, 2):
                if (y[i] == name):
                    flag = 1
                    temp = i
                    break
                if (i == (l - 2)):
                    print()
                    print()
                    print("Incorrect username!!")
                    p.login()
                    return 0
            if (y[temp + 1] == passw):
                print()
                print()
                print("Login successfull!!")
                p.staff()
                return 1
            else:
                print()
                print()
                print("Incorrect password!!")
                p.login()
                return 0
        if (self.role1 == 3):
            x = open("python/project/studentlogin.txt", "r")
            y = x.read()
            y = y.split(",")
            x.close()
            l = len(y)
            print()
            print()
            name = str(input("Enter your username:"))
            passw = str(input("Enter the password:"))
            for i in range(0, l, 2):
                if (y[i] == name):
                    flag = 1
                    temp = i
                    break
                if (i == (l - 2)):
                    print()
                    print()
                    print("Incorrect username!!")
                    p.login()
            if (y[temp + 1] == passw):
                print()
                print()
                print("Login successfull!!")
                p.student()
            else:
                print()
                print()
                print("Incorrect password!!")
                p.login()
                print()
                print()

    def application(self):
        if (self.role1 == 2):
            x = open("python/project/staffapp.txt", "a")
            print()
            print("NAME: ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("AGE: ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("ADDRESS: ")
            y = str(input(""))
            x.write(y + ",")
            print()
            print("EMAIL: ")
            y = str(input(""))
            x.write(y + ",")
            print()
            print()
            print("YOUR STAFF APPLICATION HAS BEEN SUBMITTED")
            x.close()
        if (self.role1 == 3):
            x = open("python/project/studentapp.txt", "a")
            print()
            print("NAME: ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("AGE: ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("ADDRESS: ")
            y = str(input(""))
            x.write(y + ",")
            print()
            print("EMAIL: ")
            y = str(input(""))
            x.write(y + ",")
            print()
            print()
            print("YOUR STUDENT APPLICATION HAS BEEN SUBMITTED")
            x.close()

    def student(self):
        print()
        print()
        print("1.REAQUEST FOR ALLOCATION:  ")
        print("2.RETURN BOOK:  ")
        print("3.SEARCH BOOK: ")
        print("4.EXIT:")
        print()
        print()
        a = int(input(" "))
        if (a == 1):
            x = open("python/project/bookreq.txt", "a")
            print()
            print()
            print("STUDENT NAME: ")
            y = input(" ")
            x.write(y + ",")
            print()
            print()
            print("BOOK NAME: ")
            y = input(" ")
            x.write(y + ",")
            print()
            print()
            print("BOOK SERIAL NO.: ")
            y = input(" ")
            x.write(y + ",")
            print()
            print()
            print("TIME PERIOD FOR ALLOCATION: ")
            y = input(" ")
            x.write(y + ",")
            print()
            print()
            print("BOOK ALLOCATION REQUEST HAS BEEN SUBMITTED")
            p.student()
        else:
            if (a == 2):
                x = open("python/project/bookret.txt", "a")
                print()
                print()
                print("STUDENT NAME: ")
                y = input(" ")
                x.write(y + ",")
                print()
                print()
                print("BOOK NAME: ")
                y = input(" ")
                x.write(y + ",")
                print()
                print()
                print("BOOK SERIAL NO.: ")
                y = input(" ")
                x.write(y + ",")
                print()
                print()
                print("BOOK RETURN REQUEST HAS BEEN SUBMITTED")
                p.student()
        if (a == 3):
            p.search()

    def staff(self):
        print()
        print()
        print("1.BOOK ALLOCATION: ")
        print("2.BOOK RETURN: ")
        print("3.STOCK UPDATE REQUEST: ")
        print("4.EXIT: ")
        print()
        print()
        a = int(input(" "))
        if (a == 1):
            x = open("python/project/bookreq.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            print()
            print()
            for i in range(0, l - 1, 4):
                print()
                print("NAME:" + y[i])
                print()
                print("BOOK NAME:" + y[i + 1])
                print()
                print("SERIAL NO." + y[i + 2])
                print()
                print("TIME:" + y[i + 3])
                print()
                print()
                print("1.APPROVE:")
                print("2.REJECT:")
                print()
                k = int(input(" "))
                x.close()
                if (k == 1):
                    continue
                elif (k == 2):
                    continue
            x = open("python/project/bookreq.txt", "w")
            x.write(" ")
            x.close()
            p.staff()
        if (a == 2):
            x = open("python/project/bookret.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            print()
            print()
            for i in range(0, l - 1, 4):
                print()
                print("NAME:" + y[i])
                print()
                print("BOOK NAME:" + y[i + 1])
                print()
                print("SERIAL NO." + y[i + 2])
                print()
                print()
                print("1.APPROVE:")
                print("2.REJECT:")
                print()
                k = int(input(" "))
                x.close()
                if (k == 1):
                    continue
                elif (k == 2):
                    continue
            x = open("python/project/bookret.txt", "w")
            x.write(" ")
            x.close()
            p.staff()
        if (a == 3):
            x = open("python/project/stockreq.txt", "a")
            print()
            print("NAME: ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("SERIAL NO. ")
            y = str(input(" "))
            x.write(y + ",")
            print()
            print("AMOUNT: ")
            y = str(input(""))
            x.write(y + ",")
            print()
            print("YEAR: ")
            y = input("")
            x.write(y + ",")
            print()
            print()
            print("YOUR STOCK APPLICATION HAS BEEN SUBMITTED")
            x.close()
            p.staff()

    def admina(self):
        print()
        print("1.LIST OF STAFF: ")
        print("2.LIST OF STUDENTS: ")
        print("3.LIST OF BOOKS: ")
        print("4.STUDENT APPLICATION: ")
        print("5.STAFF APPLICATION: ")
        print("6.STOCK UPDATE REQUEST: ")
        print("7.EXIT: ")
        print()
        print()
        a = int(input(" "))
        if (a == 1):
            x = open("python/project/staff.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            print()
            print()
            for i in range(0, l - 1, 4):
                print("NAME:" + y[i] + "    " + "AGE:" + y[i + 1] + "    " +
                      "ADDRESS:" + y[i + 2] + "   " + "EMAIL:" + y[i + 3])
                print()
                print()
            x.close()
            p.admina()
        elif (a == 2):
            x = open("python/project/student.txt", "r")
            y = x.read()
            y = y.split(",")
            print()
            print()
            l = len(y)
            for i in range(0, l - 1, 4):
                print("NAME:" + y[i] + "    " + "AGE:" + y[i + 1] + "    " +
                      "ADDRESS:" + y[i + 2] + "   " + "EMAIL:" + y[i + 3] + "   ")
                print()
                print()
            x.close()
            p.admina()
        elif (a == 3):
            x = open("python/project/book.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            print()
            print()
            for i in range(0, l - 1, 4):
                print("NAME:" +
                      y[i] +
                      "    " +
                      "SERIAL NO:" +
                      y[i +
                        1] +
                      "    " +
                      "AMOUNT:" +
                      y[i +
                        2] +
                      "   " +
                      "YEAR:" +
                      y[i +
                        3] +
                      "  ")
                print()
                print()
            x.close()
            p.admina()
        elif (a == 4):
            x = open("python/project/studentapp.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            for i in range(0, l - 1, 4):
                print()
                print("NAME:" + y[i])
                print()
                print("AGE:" + y[i + 1])
                print()
                print("ADDRESS:" + y[i + 2])
                print()
                print("EMAIL:" + y[i + 3])
                print()
                print()
                print("1.APPROVE:")
                print("2.REJECT:")
                print()
                k = int(input(" "))
                x.close()
                if (k == 1):
                    z = open("python/project/student.txt", "a")
                    z.write(y[i] + "," + y[i + 1] + "," +
                            y[i + 2] + "," + y[i + 3] + ",")
                    z.close()
                    x.close()
                    z = open("python/project/studentlogin.txt", "a")
                    z.write(y[i] + "," + y[i + 1] + ",")
                    z.close()
                elif (k == 2):
                    continue
            x = open("python/project/studentapp.txt", "w")
            x.write(" ")
            x.close()
            p.admina()
        elif (a == 5):
            x = open("python/project/staffapp.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            for i in range(0, l - 1, 4):
                print()
                print("NAME:" + y[i])
                print()
                print("AGE:" + y[i + 1])
                print()
                print("ADDRESS:" + y[i + 2])
                print()
                print("EMAIL:" + y[i + 3])
                print()
                print()
                print("1.APPROVE:")
                print("2.REJECT:")
                print()
                k = int(input(" "))
                x.close()
                if (k == 1):
                    z = open("python/project/staff.txt", "a")
                    z.write(y[i] + "," + y[i + 1] + "," +
                            y[i + 2] + "," + y[i + 3] + ",")
                    z.close()
                    x.close()
                    z = open("python/project/stafflogin.txt", "a")
                    z.write(y[i] + "," + y[i + 1] + ",")
                    z.close()
                elif (k == 2):
                    continue
            x = open("python/project/staffapp.txt", "w")
            x.write(" ")
            x.close()
            p.admina()
        elif (a == 6):
            x = open("python/project/stockreq.txt", "r")
            y = x.read()
            y = y.split(",")
            l = len(y)
            for i in range(0, l - 1, 4):
                print()
                print("NAME:" + y[i])
                print()
                print("SERIAL NO." + y[i + 1])
                print()
                print("AMOUNT:" + y[i + 2])
                print()
                print("YEAR:" + y[i + 3])
                print()
                print()
                print("1.APPROVE:")
                print("2.REJECT:")
                print()
                k = int(input(" "))
                x.close()
                if (k == 1):
                    z = open("python/project/book.txt", "a")
                    z.write(y[i] + "," + y[i + 1] + "," +
                            y[i + 2] + "," + y[i + 3] + ",")
                    z.close()
                elif (k == 2):
                    continue
            x = open("python/project/stockreq.txt", "w")
            x.write(" ")
            x.close()
            p.admina()

    def search(self):
        x = open("python/project/book.txt", "r")
        y = x.read()
        y = y.split(",")
        l = len(y)
        print()
        print()
        print("1.SEARCH BY NAME: ")
        print("2.SEARCH BY SERIAL NO. ")
        print("3.SEARCH BY YEAR:")
        a = int(input(" "))
        if (a == 1):
            k = str(input("BOOK NAME:"))
            for i in range(0, l - 1, 4):
                if (k == y[i]):
                    print()
                    print("NAME:" +
                          y[i] +
                          "      " +
                          "SERAIAL NO." +
                          y[i +
                            1] +
                          "       " +
                          "AMOUNT:" +
                          y[i +
                            2] +
                          "     " +
                          "YEAR:" +
                          y[i +
                            3])
                    p.student()
        if (a == 2):
            k = int(input("SERIAL NO."))
            for i in range(1, l - 1, 4):
                if (k == y[i]):
                    print()
                    print("NAME:" +
                          y[i -
                            1] +
                          "      " +
                          "SERAIAL NO." +
                          y[i] +
                          "       " +
                          "AMOUNT:" +
                          y[i +
                            1] +
                          "     " +
                          "YEAR:" +
                          y[i +
                            2])
                    p.student()
        if (a == 3):
            k = int(input("BOOK YEAR:"))
            for i in range(3, l - 1, 4):
                if (k == y[i]):
                    print()
                    print("NAME:" +
                          y[i -
                            3] +
                          "      " +
                          "SERAIAL NO." +
                          y[i -
                            2] +
                          "       " +
                          "AMOUNT:" +
                          y[i -
                            1] +
                          "     " +
                          "YEAR:" +
                          y[i])
                    p.student()
        else:
            print()
            print()
            print("BOOK NOT FOUND!!")
            p.student()


p = admin()
p.role()
