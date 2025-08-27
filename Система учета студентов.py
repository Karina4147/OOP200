class Course:
    """
    Базовый класс, описывающий курс для студентов.
    """
    def __init__(self, name, max_students, students: list|None = None):
        """
        :param name: название курса
        :param max_students: максимальное количество студентов
        :param students: список студентов
        """
        self.name = name
        self.max_students = max_students
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_on_course(self, student):
        """
        Добавляет студента на курс (если не превышен лимит)
        :param student: студент
        """
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            raise ValueError(f"Курс {self.name} уже переполнен.")

    def del_student(self, student):
        """
        Удаляет студента с курса
        :param student: студент
        """
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"Студент не был найден в списке {self.students}.")

    def __str__(self):
        """
        Представляет объект Course в виде строки для вывода.
        """
        return f"На курс {self.name} записаны следующие студенты: {self.students}. Максимальное количество студентов {self.max_students}."

class Student:
    """
    Класс, описывающий студентов.
    """
    def __init__(self, name, courses=None, grades=None):
        """
        Инициализация объекта Student.

        :param name: Имя студента (строка).
        :param courses: Список названий курсов (список строк).
        :param grades: Словарь, где ключи - названия курсов, значения - оценки (словарь).
        """
        self.name = name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        if grades is None:
            self.grades = []
        else:
            self.grades = grades


    def add_course(self, course_name):
        """
        Добавляет новый курс в список курсов студента.
        :param course_name: название нового курса
        """
        if course_name not in self.courses:
           self.courses.append(course_name)

    def add_grade(self, course_name, grade):
        """
        Добавляет оценку по курсу.
        :param course_name: название курса
        :param grade: оценка
        """
        if course_name in self.courses:
            self.grades[course_name] = grade
        else:
            print(f"Студент не записан на курс {course_name}")

    def get_average_grade(self):
        """
        Вычисляет средний балл студента по всем курсам.
        """
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        """
        Представляет объект Student в виде строки для вывода.
        """
        return f"Студент: {self.name}, Курсы: {self.courses}, Оценки: {self.grades}, Средний балл: {self.get_average_grade():.2f}"

class University:
    """
    Класс, управляющий студентами и курсами.
    """
    def __init__(self):
        """
        Инициализация объекта University
        """
        self.courses = {}
        self.students = {}

    def add_student(self, student: Student):
        """
        Добавление студента в систему.
        :param student: студент, экземпляр класса Student.
        """
        if not isinstance(student, Student):
            raise TypeError("Объект должен быть экземпляром класса Student или его подклассов.")
        if student.name in self.students:
            raise ValueError("Данный студент уже есть в системе")
        self.students[student.name] = student
        print(f"Студент {student.name} добавлен в систему университета.")

    def add_course(self, course: Course):
        """
        Добавление курса в систему.
        :param course: курс, экземпляр класса Course
        """
        if not isinstance(course, Course):
            raise TypeError("Объект должен быть экземпляром класса Course или его подклассов.")
        if course.name in self.courses:
            raise ValueError("Данный курс уже есть в системе")
        self.courses[course.name] = course
        print(f"Курс {course.name} добавлен в систему университета.")

    def register_student_for_course(self, student_name, course_name):
        """
        Регистрирует студента на указанный курс.
        :param student_name: Имя студента (строка).
        :param course_name: Название курса (строка).
        """
        # Проверяем, существует ли студент
        if student_name not in self.students:
            raise ValueError('Данного студента нет в системе')

        # Проверяем, существует ли курс
        if course_name not in self.courses:
            raise ValueError('Данного курса нет в системе')

        student = self.students[student_name]
        course = self.courses[course_name]

        try:
            # Добавляем студента на курс
            course.add_on_course(student)
            # Добавляем курс студенту
            student.add_course(course.name)
            print(f"Студент '{student_name}' успешно записан на курс '{course_name}'.")
        except ValueError:
            print(f"Не удалось записать студента '{student_name}' на курс '{course_name}'. Курс переполнен.")
            return False
        return True

    def assign_grade(self, student_name, course_name, grade):
        """
        Выставляет оценку студенту за курс.
        :param student_name: имя студента
        :param course_name: название курса
        :param grade: оценка
        """
        if student_name in self.students and course_name in self.courses:
            self.students[student_name].add_grade(course_name, grade)
            print(f"Оценка {grade} выставлена студенту '{student_name}' за курс '{course_name}'.")
        else:
            print("Студент или курс не найдены.")

    def view_students_performance(self):
        """
            Просмотр общего списка студентов и их успеваемости.
        """
        print("\n=== УСПЕВАЕМОСТЬ СТУДЕНТОВ ===")
        for student_name, student in self.students.items():
            print(student)
        print("=" * 50)



if __name__ == "__main__":
    uni = University()

    # Добавляем курсы
    uni.add_course(Course("Английский язык", 2))
    uni.add_course(Course("Физика", 4))
    uni.add_course(Course("Программирование", 10))

    # Добавляем студентов
    uni.add_student(Student("Иван Иванов"))
    uni.add_student(Student("Петр Петров"))
    uni.add_student(Student("Сергей Сергеев"))

    # Записываем студентов на курсы
    uni.register_student_for_course("Иван Иванов", "Английский язык")
    uni.register_student_for_course("Иван Иванов", "Программирование")
    uni.register_student_for_course("Петр Петров", "Английский язык")
    uni.register_student_for_course("Петр Петров", "Физика")
    uni.register_student_for_course("Сергей Сергеев", "Программирование")

    # Пытаемся записать третьего студента на Английский язык (лимит 2)
    uni.register_student_for_course("Сергей Сергеев", "Английский язык")

    # Выставляем оценки
    uni.assign_grade("Иван Иванов", "Английский язык", 5)
    uni.assign_grade("Иван Иванов", "Программирование", 4)
    uni.assign_grade("Петр Петров", "Английский язык", 3)
    uni.assign_grade("Петр Петров", "Физика", 5)
    uni.assign_grade("Сергей Сергеев", "Программирование", 5)

    # Просматриваем успеваемость
    uni.view_students_performance()






