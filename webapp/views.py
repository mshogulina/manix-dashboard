from django.shortcuts import render
from django.http import HttpResponse


class User:
  pass


class MobilePhone:
  def __init__(self, model, screen_diagonal, battery_capacity):
    self.model = model
    self.screen_diagonal = screen_diagonal
    self.battery_capacity = battery_capacity


class Task:
  # __init__ это специальная функция (конструктор), которая каждый раз вызывается
  # при создании объекта этого типа
  def __init__(self, begin_date1: str, end_date1: str, user1: str, description1: str):
    # self.begin_date - мы говорим, что у объекта типа Task
    # будет свойство begin_date
    self.begin_date = begin_date1
    self.end_date = end_date1
    self.user = user1
    self.description = description1

  def to_string(self):
    return "123"


def to_string(t: Task):
  return f"{t.begin_date} - {t.end_date}: {t.description}"


def sum(n1, n2):
  return (n1 + n2) * 3


def index(request):
  # y(x1, x2) = 2 * x1 - 6 + x2
  # sum(n1, n2) = 2 * n1 - 6 + n2
  # sum(n1, n2) = (n1 + n2) * 3

  # n3 = sum(1, 2)
  # print(n3)

  # n3 = sum(2, 3)
  # print(n3)

  # переменная task1 хранит целое число 123
  task1 = 123

  # переменная task1 хранит строку "123 qwe"
  task1 = "123 qwe"
  # task1.count

  # переменная task1 хранит вещественное число 123.45
  task1 = 123.45



  # переменная task1 хранит объект класса Task
  # переменная task1 хранит экземпляр класса Task

  # 1) создаем объект (экземпляр) класса (типа) Task
  # 2) инициализируем его значениями: "08:00", "08:10", "Маша", "Заправить постель"
  task1 = Task("08:00", "08:10", "Маша", "Заправить постель")
  print(task1.description2)

  # task1 = Task()
  # task1.begin_date = "08:00"
  # task1.end_date = "08:10"
  # task1.user = "Маша"
  # task1.description = "Заправить постель"




  # вывод значения в консоль
  print("task1.begin_date=" + task1.begin_date)
  print("task1.end_date=" + task1.end_date)

  task2 = Task("08:10", "09:00", "Маша", "Завтрак")
  task3 = Task("09:00", "11:00", "Маша", "Чтение книг")

  return HttpResponse("Hello, it's my <b>dashboard</b> web application." +
                      "<table>" +
                      "<tr><td>" + to_string(task1) + "</td></tr>" +
                      "<tr><td>" + to_string(task2) + "</td></tr>" +
                      "<tr><td>" + to_string(task3) + "</td></tr>" +
                      "</table>")
