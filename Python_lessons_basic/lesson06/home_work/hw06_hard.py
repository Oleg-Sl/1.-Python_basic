# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Employee:
    def __init__(self, row):
        data = row.split()
        self.name = data[0]
        self.lastname = data[1]
        self.morm_salary = float(data[2])
        self.profession = data[3]
        self.norm_hours = float(data[4])
        self.salary = None

    def calculation_of_salary(self, hours_worked):
        self.salary = self.morm_salary * hours_worked / self.norm_hours


def main():
    employees = []

    with open('data/workers', 'r', encoding='utf-8') as f:
        f.readline()
        for row in f:
            employees.append(Employee(row))

    with open('data/hours_of', 'r', encoding='utf-8') as f:
        f.readline()
        for row in f:
            name, lastname, hours = row.split()
            for employee in employees:
                if employee.name == name and employee.lastname == lastname:
                    employee.calculation_of_salary(float(hours))

    header = ['Фамилия', 'Имя', 'Зарплата']
    width_lastname = len(max([emloyee.lastname for emloyee in employees], key=len)) + 1
    width_name = len(max([emloyee.name for emloyee in employees], key=len)) + 5

    print(f'{header[0]:{width_lastname}} {header[1]:{width_name}} {header[2]}')
    print(*[f'{emloyee.lastname:{width_lastname}} {emloyee.name:{width_name}} {emloyee.salary:.2f}' for emloyee in employees], sep="\n")


if __name__ == '__main__':
    main()


