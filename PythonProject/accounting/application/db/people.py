from logger import logger

def get_employees():
    print("Список сотрудников получен")

@logger('app.log')
def get_employees():
    print('Employees are received')
    return 'Employees are received'