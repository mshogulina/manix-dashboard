from django.shortcuts import render
from django.http import HttpResponse


class User:
  pass


class Task:
  def __init__(self, begin_date, end_date, user, description):
    self.begin_date = begin_date
    self.end_date = end_date
    self.user = user
    self.description = description


def to_string(t: Task):
  return f"{t.begin_date} - {t.end_date}: {t.description}"


def sum(n1, n2):
  n3 = n1 + n2
  return n3


def index(request):
  # n1 = 12
  # n1 = 45

  # number = sum(12, 23)
  # number = sum(23, 45)

  task1 = Task("08:00", "08:10", "Маша", "Заправить постель")
  task2 = Task("08:10", "09:00", "Маша", "Завтрак")
  task3 = Task("09:00", "11:00", "Маша", "Чтение книг")

  return HttpResponse("Hello, it's my <b>dashboard</b> web application." + 
                      "<table>" + 
                      "<tr><td>" + to_string(task1) + "</td></tr>" +
                      "<tr><td>" + to_string(task2) + "</td></tr>" +
                      "<tr><td>" + to_string(task3) + "</td></tr>" + 
                      "</table>")
