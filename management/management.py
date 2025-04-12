import os
import mysql.connector

class EmployeeManagementSystem:
    def __init__(self):
        # Initialize the connection and cursor
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="employee"
        )
        self.cursor = self.con.cursor()

    def add(self):
        os.system("cls")
        print("Enter employee details")
        ID = input("Enter ID of employee: ")
        NAME = input("Enter name of employee: ")
        EMAIL_ID = input("Enter email of employee: ")
        phn_num = input("Enter phn_num of employee: ")
        ADDRESS = input("Enter address of employee: ")
        POST = input("Enter position of employee: ")
        SALARY = input("Enter salary of employee: ")

        data = (ID, NAME, EMAIL_ID, phn_num, ADDRESS, POST, SALARY)

        sql = 'INSERT INTO employee (id, name, age) VALUES (%s, %s, %s)'
        try:
            self.cursor.execute(sql, data)
            self.con.commit()
            print("Successfully added!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        input("Press any key to continue...")
        self.menu()

    def update(self):
        os.system("cls")
        id = input("Enter the ID for which you want to update: ")
        col = input("Enter which column you want to update (name, age): ")
        val = input("Enter the new value: ")

        sql = f"UPDATE employee SET {col} = %s WHERE ID = %s"
        try:
            self.cursor.execute(sql, (val, id))
            self.con.commit()
            print("Successfully updated!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        input("Press any key to continue...")
        self.menu()

    def delete(self):
        os.system("cls")
        id = input("Enter the ID to delete: ")

        sql = 'DELETE FROM employee WHERE id = %s'
        try:
            self.cursor.execute(sql, (id,))
            self.con.commit()
            print("Successfully deleted!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        input("Press any key to continue...")
        self.menu()

    def display(self):
        os.system("cls")

        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
        else:
            print("No records found.")

        input("Press any key to continue...")
        self.menu()

    def promote(self):
        os.system("cls")
        id = input("Enter the ID of the employee to promote: ")
        amount = int(input("Enter the amount to increase the age: "))

        try:
            sql = "SELECT age FROM employee WHERE id = %s"
            self.cursor.execute(sql, (id,))
            r = self.cursor.fetchone()

            if r:
                new_salary = r[0] + amount
                update_sql = 'UPDATE employee SET SALARY = %s WHERE id = %s'
                self.cursor.execute(update_sql, (new_salary, id))
                self.con.commit()
                print(f"Age successfully updated to {new_salary}!")
            else:
                print(f"No employee found with ID {id}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        input("Press any key to continue...")
        self.menu()

    def menu(self):
        os.system("cls")
        print("<----------------------------EMPLOYEE MANAGEMENT SYSTEM---------------------------->")
        print("1. Add details")
        print("2. Update details")
        print("3. Delete details")
        print("4. Display all employees")
        print("5. Promote (Increase age)")
        print("6. Exit")

        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.add()
            elif ch == 2:
                self.update()
            elif ch == 3:
                self.delete()
            elif ch == 4:
                self.display()
            elif ch == 5:
                self.promote()
            elif ch == 6:
                self.exit()
            else:
                print("Invalid choice!")
                self.menu()
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            input("Press any key to continue...")
            self.menu()

    def exit(self):
        print("Exiting the system.")
        self.cursor.close()
        self.con.close()
        exit()

# Create an instance of the system and start the program
ems = EmployeeManagementSystem()
ems.menu()