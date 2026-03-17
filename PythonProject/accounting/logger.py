from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f'Дата и время вызова: {datetime.now()}\n'
                    f'Имя функции: {old_function.__name__}\n'
                    f'Аргументы: args={args}, kwargs={kwargs}\n'
                    f'Возвращаемое значение: {result}\n'
                    f'{"-" * 40}\n'
                )

            return result

        return new_function

    return __logger