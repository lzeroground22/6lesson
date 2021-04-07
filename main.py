from itertools import chain


def unlist(some):
    return list(chain.from_iterable(some.values()))


def equal(some):
    """
    Среднее значение
    """
    return sum(unlist(some)) / len(unlist(some))


def __lt__(self, other):
    """
    Сравнение средних значений
    """
    return equal(self.rating) < equal(other.rating)



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.hw_grades = {}

    def set_rating(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return "Ошибка"

    def __str__(self):
        print("Имя", self.name)
        print("Фамилия", self.surname)
        print('Средняя оценка за домашние задания: ', equal(self.hw_grades))
        print("Курсы в процессе изучения:", ", ".join(self.courses_in_progress))
        print("Завершенные курсы:", ", ".join(self.finished_courses))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """
    лекторы
    """

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def __str__(self):
        print("Имя", self.name)
        print("Фамилия", self.surname)
        print('Средняя оценка за лекции: ', equal(self.rating))


class Reviewer(Mentor):
    """
    эксперты, проверяющие домашние задания
    """

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.hw_grades:
                student.hw_grades[course] += [grade]
            else:
                student.hw_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print("Имя", self.name)
        print("Фамилия", self.surname)


# ___________________________________________
# Студент 1
pasha = Student("Pasha", "Pupkin", "male")
pasha.courses_in_progress = "git", "python"
pasha.finished_courses = "Java", "Mar"

# Студент 2
artem = Student("Artem", "Ivanov", "male")
artem.courses_in_progress = "git",
artem.finished_courses = "JS",

# Лектор 1
semenov = Lecturer("Sergei", "Semenov")
semenov.courses_attached = ["git"]

# Лектор 2
serov = Lecturer("Boris", "Serov")
serov.courses_attached = ["git", "python"]

# Проверяющий 1
vodkin = Reviewer("Petr", "Vodkin")
vodkin.courses_attached = "git"
vodkin.rate_hw(pasha, "git", 8)
vodkin.rate_hw(artem, "git", 4)

# Проверяющий 2
batina = Reviewer("Masha", "Batina")
batina.courses_attached = "python"
batina.rate_hw(artem, "git", 6)
batina.rate_hw(pasha, "python", 10)

pasha.set_rating(semenov, "git", 3)
pasha.set_rating(serov, "python", 2)

artem.set_rating(semenov, "git", 9)
artem.set_rating(serov, "git", 4)

# semenov.__str__()
# print()
# serov.__str__()
# print()
# vodkin.__str__()
# print()
# batina.__str__()
# print()
# pasha.__str__()
# print()
# artem.__str__()

# print(equal(serov.rating))
# print(semenov < serov)