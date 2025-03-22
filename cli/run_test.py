import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.selects import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10
)
from tabulate import tabulate



if __name__ == "__main__":
    print("Топ 5 студентів з найвищим середнім балом:")
    data = select_1()
    print(tabulate(data, headers=["Студент", "Середній бал"], tablefmt="github"))

    print("\nСтудент з найвищим балом з предмета (ID=2):")
    result = select_2(2)
    if result:
        print(tabulate([result], headers=["Студент", "Середній бал"], tablefmt="github"))
    else:
        print("Немає даних")

    print("\nСередній бал у групах з предмета (ID=3):")
    data = select_3(3)
    print(tabulate(data, headers=["Група", "Середній бал"], tablefmt="github"))

    print("\nСередній бал на потоці:")
    avg = select_4()
    print(tabulate([[round(avg, 2)]], headers=["Середній бал"], tablefmt="github") if avg else "Немає оцінок")

    print("\nКурси, які читає викладач (ID=1):")
    subjects = select_5(1)
    if subjects:
        print(tabulate(subjects, headers=["Курс"], tablefmt="github"))
    else:
        print("Немає курсів")

    print("\nСтуденти у групі (ID=1):")
    data = select_6(1)
    print(tabulate(data, headers=["Студент"], tablefmt="github"))

    print("\nОцінки студентів у групі (ID=1) з предмета (ID=2):")
    data = select_7(1, 2)
    print(tabulate(data, headers=["Студент", "Оцінка"], tablefmt="github"))

    print("\nСередній бал, який ставить викладач (ID=1):")
    avg = select_8(1)
    print(tabulate([[round(avg, 2)]], headers=["Середній бал"], tablefmt="github") if avg else "Немає оцінок")

    print("\nКурси, які відвідує студент (ID=1):")
    data = select_9(1)
    print(tabulate(data, headers=["Курс"], tablefmt="github"))

    print("\nКурси, які читає викладач (ID=1) студенту (ID=1):")
    data = select_10(1, 1)
    print(tabulate(data, headers=["Курс"], tablefmt="github"))
