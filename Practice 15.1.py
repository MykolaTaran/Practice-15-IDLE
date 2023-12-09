import pandas as pd

class Employee:
    def __init__(self, last_name, salary, gender):
        self.last_name = last_name
        self.salary = salary
        self.gender = gender

def find_highest_salary(employees):
    # Placeholder logic for finding the employee with the highest salary
    highest_salary_employee = max(employees, key=lambda x: x.salary)
    return highest_salary_employee.last_name

def find_lowest_salary_names(employees):
    # Placeholder logic for finding the employees with the lowest salary for male and female
    lowest_salary_male_employee = min((emp for emp in employees if emp.gender == "Male"), key=lambda x: x.salary)
    lowest_salary_female_employee = min((emp for emp in employees if emp.gender == "Female"), key=lambda x: x.salary)

    return lowest_salary_male_employee.last_name, lowest_salary_female_employee.last_name

# Основна частина програми
if __name__ == "__main__":
    # Задання даних про співробітників
    employees_data = [
        {"last_name": "Ivanov", "salary": 49000, "gender": "Male"},
        {"last_name": "Petrov", "salary": 60000, "gender": "Male"},
        {"last_name": "Sidorovna", "salary": 45000, "gender": "Female"},
        {"last_name": "Sidorov", "salary": 47500, "gender": "Male"},
        {"last_name": "Prikhodko", "salary": 55500, "gender": "Male"},
        {"last_name": "Miroshnichenko", "salary": 60500, "gender": "Male"},
        {"last_name": "Skochenko", "salary": 30000, "gender": "Female"},
        {"last_name": "Ponomarenko", "salary": 52000, "gender": "Male"},
        {"last_name": "Taran", "salary": 51200, "gender": "Male"},
        {"last_name": "Rovna", "salary": 53000, "gender": "Female"}
    ]

    # Створення об'єктів співробітників
    employees = [Employee(data["last_name"], data["salary"], data["gender"]) for data in employees_data]

    # Перетворення в датафрейм
    df = pd.DataFrame(employees_data)

    # Знаходження результатів
    highest_salary_last_name = find_highest_salary(employees)
    lowest_salary_male, lowest_salary_female = find_lowest_salary_names(employees)

    # Виведення результатів
    print(f"Прізвище особи з найбільшою зарплатою: {highest_salary_last_name}")
    print(f"Прізвище чоловіка з найменшою зарплатою: {lowest_salary_male}")
    print(f"Прізвище жінки з найменшою зарплатою: {lowest_salary_female}")

    # Виведення датафрейму
    print("\nДані у вигляді датафрейму:")
    print(df)
