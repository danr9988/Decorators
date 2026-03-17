from logger import logger

def calculate_salary():
    print("Расчёт зарплаты выполнен")

@logger('app.log')
def calculate_salary():
    print('Salary is calculated')
    return 'Salary is calculated'