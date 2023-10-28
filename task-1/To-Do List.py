
import os

#             ----------------------------------------------- File Class -----------------------------------------------

class Add_file_saver:

    def check_unique_username(self,username,pswd):
        with open ("info.txt") as file:
            file = eval(file.read())
            list = []
            for item in file:
                for i in item:
                    list.append(i)
            if username not in list:
                dict = {username:pswd}
                file.append(dict)
                with open("info.txt","w") as f:
                    f.write(f'{file}')
                    os.system("cls")
                    input("\n\n\nYour New Account Was Created !! \n\nPress Enter to  Continue ")
                    return
            else:
                os.system("cls")
                print("Enter Unique Username")
                input("Press Enter To Continue")
                return

    def Add_User_Task(self, first_name,task):
        with open(f"{first_name}.txt") as add:
            file = eval(add.read())
            list = file[1]
            list.append(task)
            file[1] = list
        with open(f"{first_name}.txt", "w") as add:
            add.write(f'{file}')
        return


    def update_user_list(self,first_name):
        with open(f"{first_name}.txt") as add:
            file = eval(add.read())
            file = file[1]
            if len(file) == 0:
                os.system("cls")
                input("First Add Task In  To-Do list\n\nPress Enter To Continue  ")
            else:
                return len(file)


#             ----------------------------------------------- User Class -----------------------------------------------

class User:
    def __init__(self):
        self.filename = Add_file_saver()
    def SignUp(self):
        while True:
            os.system("cls")
            print(f'\n\n\n {"-"*40} SIGN UP {"-"*40} \n\n\n')
            self.First_Name = input("Enter First Name: ")
            self.Last_Name = input("Enter Last Name: ")
            self.Username = input("Enter Username: ")
            self.Pswd = input("Enter Strong Passsword: ")
            self.unique = self.filename.check_unique_username(self.Username,self.Pswd)
            with open(f"{self.Username}.txt","w") as f:
                d = {}
                d[self.Username] = self.Pswd
                f.write(f'[{d},[]]')
            break
    def LogIn(self):
        os.system("cls")
        print(f"\n\n\n{'-'*40} LogIn {'-'*40} \n\n\n")
        self.first_name = input("Enter Username: ")
        while True:
            try:
                with open(f'{self.first_name}.txt') as file:
                    file = eval(file.read())
                    self.pswd = input("\nEnter pswd: ")
                    dict = file[0][self.first_name]
                    if dict == self.pswd:
                        while True:
                            os.system("cls")
                            print(f"\n\n\n\n{'-' * 50} WELCOME TO THE TO-DO LIST {'-' * 50}")
                            user = input("\n\n1. Add Task\n2. Remove Task\n3. Clear List\n4. Show Task\n\n\n[q]: Quit\n\n")
                            if user == "1":
                                self.Add_task()
                            elif user == "2":
                                self.Remove_task()
                            elif user == "3":
                                self.Clear_list()
                            elif user == '4':
                                self.Show_task()
                            elif user == "q":
                                return
                            else:
                                os.system('cls')
                                input("Invalid input\n\nPress Enter To Continue  ")
                    else:
                        print("Invalid Password\n\n")
                        input("Press Enter To Continue  ")
                        os.system("cls")
                        break
            except:
                print('Account Was Not Exist\n\n')
                input("Press Enter To Continue  ")
                os.system("clear")
                break


    def Add_task(self):
        os.system("cls")
        print("\n\n\nCongratulation !! Your  To-Do list is create\n")
        while True:
            user = input("Enter Y for Continue and B for back   ").upper()
            if user == "Y":
                os.system("cls")
                user = input("\n\n\n\nEnter Task : ")
                self.filename.Add_User_Task(self.first_name,user)
                print("Your task was SucessFully Added")
            elif user == "B":
                return
            else:
                os.system("cls")
                input("\n\nInvalid Input\n\nPress Enter To Continue  ")


    def Remove_task(self):
        count = self.filename.update_user_list(self.first_name)
        if count == None:
            return
        else :
            while True:
                os.system("cls")
                for i in range(1):
                    user = input("\n\n\n\nEnter Task: ")
                    with open(f'{self.first_name}.txt') as file:
                        file = eval(file.read())
                        list = file[1]
                        if user in list:
                            list.remove(user)
                            file[1] = list
                            with open(f'{self.first_name}.txt', 'w') as f:
                                f.write(str(file))
                                print(file)
                            print("\n\nTask Remove\n")
                        else:
                            print("Invalid Task Input")
                os.system("cls")
                print("\n[c].Continue\n[q].Quit\n")
                user = input()
                if user == "q":
                    return
                elif "c":
                    continue
                else:
                    print("Invalid Input")

    def Clear_list(self):
        os.system('cls')
        with open(f"{self.first_name}.txt") as f:
            f = eval(f.read())
            f[1] = []
        with open(f'{self.first_name}.txt', 'w') as file:
            file.write(str(f))
        input("\n\nYour To-Do List was clear\nPress Enter To Continue  ")
        os.system('cls')
        return

    def Show_task(self):
        os.system('cls')
        with open(f"{self.first_name}.txt") as f:
            f = eval(f.read())
            file=f[1]
            if len(file) != 0:
                print(f'\n\n{"-" * 40} Task {"-" * 40} \n ')
                for i in range(len(file)):
                    print(f'{i+1}.{file[i]}')
                while True:
                    user = input('\n\n[q]: Quit\n')
                    if user == 'q':
                        os.system("clear")
                        return
                    else:
                        print("Invalid Input")
                        os.system("clear")
            else:
                input("Your To-Do List is empty\n\nPress Enter To Continue  ")
                os.system("clear")
                return


 #               ----------------------------------------------- Test Run -----------------------------------------------


Task = User()
while True:
    os.system("cls")
    User = input(f"\n\n\n\n{'-'*50} WELCOME TO THE TO-DO LIST {'-'*50} \n\n\n\n""1. Login\n""2. Sign up\n""3. Exit\n\n")
    if User == "1":
        Task.LogIn()
    elif User == "2":
        Task.SignUp()
    elif User == "3":
        break
    else:
        input("Invalid Input ! Please choose the right one\n\nPress Enter to Continue")
        os.system("cls")