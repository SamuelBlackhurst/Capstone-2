# imports
import datetime
import os

DATETIME_STRING_FORMAT = "%Y-%m-%d"

task_list = []


def display_statistics():
    # Call function to generate report
    # Retrive generated report
    # Print user overview to user
    generate_report()
    with open("task_overview.txt", 'r') as task_file:
        print("\n***Task Overview***\n")
        for line in task_file:
            print(line, end="")

        with open("user_overview.txt", 'r') as task_file:
            print("\n***User Overview***\n")
            for line in task_file:
                print(line, end="")


def generate_report():
    current_date = datetime.datetime.today()
    total_task = 0
    uncompleted_task = 0
    completed_task = 0
    overdue_task = 0
    user_task = 0
    user_overdue_and_uncompleted = 0
    user_completed = 0
    user_uncompleted_task = 0
    current_date = datetime.datetime.today()
    total_task = 0
    uncompleted_task = 0
    completed_task = 0
    overdue_task = 0
    user_task = 0
    user_overdue_and_uncompleted = 0
    user_completed = 0
    user_uncompleted_task = 0

    # Read the users.txt file and store the usernames and passwords in a dictionary
    # Iterate through the dictionary and get the information for each user
    with open("user.txt", "r") as f:
        users = {}
        for line in f:
            user_name, password = line.strip().split(";")
            users[user_name] = password
    with open("overview.txt", "w") as out_file:
        for user_name, password in users.items():
            user_task = 0
            user_overdue_and_uncompleted = 0
            user_completed = 0
            user_uncompleted_task = 0

    # read task.txt file and count total tasks
    # check each line for uncomplete, complete and overdue tasks
    input_file = open("tasks.txt", "r")
    for line in input_file:
        parts = line.strip().split(";")
        total_task += 1


        if "No" in parts[-1]:
            uncompleted_task += 1
        elif "Yes" in parts[-1]:
            completed_task += 1
        elif str(current_date.strftime("%Y %m %d")) in parts[5]:
            overdue_task += 1


        with open("task_overview.txt", "w") as out_file:
            print(f"There are a total of {total_task} tasks.", file=out_file)
            print(f"There are a total of {uncompleted_task} uncompleted tasks.", file=out_file)
            print(f"There are a total of {completed_task} completed tasks.", file=out_file)
            print(f"There are a total of {overdue_task} overdue tasks.", file=out_file)
            print(f"{(uncompleted_task / total_task * 100):.2f}% of tasks are uncompleted.", file=out_file)
            print(f"{(overdue_task / total_task * 100):.2f}% of tasks are overdue.", file=out_file)

        # write results of various task totals and percentages to task_overview.txt file
        # check if current user has any task
        # check to work out information about tasks
        if user_name in parts[1]:
            user_task += 1
            if "No" in parts[-1]:
                user_uncompleted_task += 1
            elif "Yes" in parts[-1]:
                user_completed += 1
            if str(current_date.strftime("%Y %m %d")) in parts[5] and "No" in line:
                user_overdue_and_uncompleted += 1


            with open("user_overview.txt", "w") as out_file:
                print(f"{user_name} has been assigned {user_task} tasks", file=out_file)
                print(f"{(user_task / total_task * 100):.2f}% of all tasks have been assigned {user_name}.",
                      file=out_file)
                print(
                    f"{(user_completed / user_task * 100):.2f}% of all tasks assigned {user_name} have been completed.",
                    file=out_file)
                print(
                    f"{(user_uncompleted_task / user_task * 100):.2f}% of all tasks assigned {user_name} still need "f"to be "f"completed.",
                    file=out_file)
                print(
                    f"{(user_overdue_and_uncompleted / user_task * 100):.2f}% of all tasks assigned {user_name} are "f"overdue and "f"need to be completed.",
                    file=out_file)


def view_mine():
    # Retrive task data from tasks.txt
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    for t_str in task_data:
        curr_t = {}

        # Split data by ; and add each component
        task_components = t_str.split(";")
        curr_t['ID'] = task_components[0]
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[6] == "Yes" else False

        # append task list
        task_list.append(curr_t)
        # Display tasks to user
    for t in task_list:
        if t['username'] == user_name:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print("--------------------------")
            print(disp_str)
            print("--------------------------")

    # Let user select a task or return to menu
    task_selection = int(
        input(
            "Enter the number of the task you want to edit/mark as complete, or enter -1 to return to the main menu: "))
    while logged_in:
        if task_selection == -1:
            continue

        elif task_selection > len(task_list):
            print("Invalid task selection. Please try again.")
            continue

    # get data for selected task
    selected_task = task_list[task_selection]

    # ask user if they want to edit or mark task as complete

    task_action = input("Enter 'c' to mark the task as complete or 'e' to edit the task: ").lower()
    if task_action == 'c':

        # Mark task as completed
        task_data[
            task_selection] = f"{selected_task['ID']};{selected_task['username']};{selected_task['title']};" \
                              f"{selected_task['description']};{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};" \
                              f"{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};Yes"
        with open('tasks.txt', 'w') as task_file:
            for line in task_data:
                task_file.write(line + "\n")
            print("Task marked as complete")


    elif task_action == "e":
        selected_task = task_list[task_selection]

    # Check if task is complete and give appropriate response if complete
    if selected_task['completed']:
        print("Task is already complete and cannot be edited.")
        return

    # Ask user for input to edit user or due date
    # edit task user if u is answer given
    else:
        task_field = input("Enter 'u' to edit the user or 'd' to edit the due date: ").lower()
        if task_field == 'u':
            new_user = input("Enter the new user for the task: ")
            selected_task['username'] = new_user
            task_data[
                task_selection] = f"{selected_task['ID']};{selected_task['username']};" \
                                  f"{selected_task['title']};{selected_task['description']};" \
                                  f"{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};" \
                                  f"{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};No"
            with open('tasks.txt', 'w') as task_file:
                for line in task_data:
                    task_file.write(line + "\n")
            print("Task user updated.")


        # Edit task due date if d is given answer
        elif task_field == 'd':
            new_due_date = input("Enter the new due date for the task (yyyy-mm-dd): ")
            selected_task['due_date'] = datetime.datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
            task_data[
                task_selection] = f"{selected_task['ID']};{selected_task['username']};" \
                                  f"{selected_task['title']};{selected_task['description']};" \
                                  f"{selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)};" \
                                  f"{selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};No"
            with open('tasks.txt', 'w') as task_file:
                for line in task_data:
                    task_file.write(line + "\n")

            print("Task due date updated.")
        else:
            print("Invalid input. Task not edited.")


def view_all():
    # Read all data from tasks.txt file
    # Print to user in an easily readable manner

    with open("tasks.txt", "r") as task_file:
        for lines in task_file:
            temp = lines.strip().split(';')
            disp_str = f"ID: \n\t {temp[0]}\n"
            disp_str += f"Assigned to: \n\t {temp[1]}\n"
            disp_str += f"Task: \n\t {temp[2]}\n"
            disp_str += f"Date Assigned: \n\t {temp[4]}\n"
            disp_str += f"Due Date: \n\t {temp[5]}\n"
            disp_str += f"Task Description: \n\t {temp[3]}\n"
            disp_str += f"Task Complete: \n\t {temp[6]}\n"
            print("--------------------------")
            print(disp_str)
            print("--------------------------")


def reg_user():
    # Request user input new username
    # Request user input new password
    # Request user confirm new password
    new_username = input("Enter username:")
    new_password = input("Enter Password")
    confirm_password = input("Confirm Password: ")

    # check if username already exists
    # if username is new  and check if passwords match
    if confirm_password != new_password:
        print("The passwords do not match....please try again")
        return

    if new_username in usernames:
        print("This username already exists, Please try again! ")
        return
    # if passwords match and new username is given
    # add to user.txt
    elif confirm_password == new_password:
        file = open("user.txt", "a")

        file.write(f"\n{new_username};{new_password}")
        print("New user added!")
        file.close()


def add_task():
    # Create tasks.txt if it doesn't exist
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w") as default_file:
            pass
    with open("tasks.txt", "r") as file:
        last_id = len(file.readlines())

    new_id = int(last_id) + 1
    # Request user input defining new task
    ID = new_id
    assigned_user = input("Enter Assigned user:")
    title = input("Enter task title : ")
    desc = input("Enter Task description :")
    startdate = datetime.date.today()
    print(f"Starting date of the task : {startdate}")
    duedate = input("Enter the due date (YYYY-MM-DD) :")
    completed = "No"

    # return information in a readable way to user
    print(f"""
 
This is the task:
ID: {ID}
User : {assigned_user}
Title : {title}
Description : {desc}
Start date : {startdate}
Due Date : {duedate}
Completion Status : {completed}
""")

    # append data to tasks.txt
    file = open("tasks.txt", "a")

    file.write(f"\n{ID};{assigned_user};{title};{desc};{startdate};{duedate};{completed}")
    file.close()


usernames = []
passwords = []
# Read in user_data for each line in the file strip of spaces and split at the semi-colon
file = open("user.txt", "r")


for lines in file:
    temp = lines.strip().split(';')

    usernames.append(temp[0])
    passwords.append(temp[1])

file.close()

# If user not logged in check for the following when logging in
logged_in = False

while not logged_in:
    user_name = input("Username : ")
    pass_word = input("Password : ")

    if user_name not in usernames:
        print("Incorrect username... Please try again")

    elif pass_word not in passwords:
        print("Incorrect password... Please try again")

    else:
        print(f"welcome {user_name}, please make a selection from the menu below")
        logged_in = True

while logged_in:
    # show menu to logged-in user
    # check if user is admin and give extra options if user = admin
    menu = input(f'''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    {"""gr - Generate reports
    ds - Display statistics
    e - Exit""" if (user_name == "admin") else "e - Exit"}
    : ''').lower()

    if menu == "r":
        reg_user()
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()
    elif menu == "gr" and user_name == "admin":
        generate_report()
    elif menu == "ds" and user_name == "admin":
        display_statistics()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
