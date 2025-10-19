import json
import logging
import os.path

utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../logs/utils_logs.log", encoding="utf-8")
file_handler.encoding = "utf-8"

file_formatter = logging.Formatter(" %(asctime)s %(name)s %(levelname)s: %(message)s ")
file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)


def jsn_date(path_):

    """Функция проверки данных"""

    date_path = path_
    data = []
    try:
        utils_logger.info("Прoизведена проверка данных,отроботала функция jsn_date")
        if not os.path.isfile(date_path):
            utils_logger.info(f" файл не найден{date_path},{str(e)} ")
            return data
        else:
            with open(date_path, "r", encoding="utf-8") as file:
                data_ = json.load(file)

            if isinstance(data_, list):
                print(" данные являются списком")
                if all(isinstance(item, dict) for item in data_):
                    print(" файл является списком словарей ")
                else:
                    utils_logger.info(" даные не соответствуют ожидаемым ")
                    return data
            if len(data_) == 0:
                print(data)
                return data

            utils_logger.info('Прoизведена проверка данных,отроботала функция jsn_date')
            return data_
    except Exception as e:
        utils_logger.error(f"ошибка {str(e)}")
        print(f"ошибка {e})")


if __name__ == "__main__":  # pragma: no cover

    jsn_date(r"C:/Users/serzh/PycharmProjects/pythonProject10/date/operations.json")
