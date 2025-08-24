class Course:
    """
    Базовый класс, описывающий курс для студентов.
    """
    def __init__(self, name, students: list, max_students):
        """
        :param name: название курса
        :param max_students: максимальное количество студентов
        :param students: список студентов
        """
        self.name = name
        self.students = students
        self.max_students = max_students

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
    def __init__(self, name, courses, grades):
        """
        Инициализация объекта Student.

        :param name: Имя студента (строка).
        :param courses: Список названий курсов (список строк).
        :param grades: Словарь, где ключи - названия курсов, значения - оценки (словарь).
        """
        self.name = name
        self.courses = courses
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
        return f"Имя: {self.name}, Курсы: {', '.join(self.courses)}, Оценки: {self.grades}"

class University:
    """
    Класс, управляющий студентами и курсами.
    """
    def __init__(self):
        """
        Инициализация объекта University
        """
        self.new_course = []
        self.list_of_students = []

    def add_student(self, student):

        if not isinstance(student, Student):
            raise TypeError("Объект должен быть экземпляром класса Student или его подклассов.")
        self.list_of_students.append(student)
        print(f"Студент {student.name} добавлен в систему университета.")

    def add_courses(self, course):
        if not isinstance(course, Course):
            raise TypeError("Объект должен быть экземпляром класса Course или его подклассов.")
        self.new_course.append(course)
        print(f"Курс {course.name} добавлен в систему университета.")

    def register_student_for_course(self, student_name, course_name):
        """
        Регистрирует студента на указанный курс.

        :param student_name: Имя студента (строка).
        :param course_name: Название курса (строка).
        """
        # Проверяем, существует ли студент
        if student_name not in self.list_of_students:
            self.list_of_students[student_name] = []  # Создаем пустой список курсов для нового студента

        # Проверяем, существует ли курс
        if course_name not in self.new_course:
            self.new_course[course_name] = []  # Создаем пустой список студентов для нового курса

        # Добавляем студента на курс, если он еще не зарегистрирован на него
        if student_name not in self.new_course[course_name]:
            self.new_course[course_name].append(student_name)
            self.list_of_students[student_name].append(course_name)
            print(f"Студент '{student_name}' успешно зарегистрирован на курс '{course_name}'")
        else:
            print(f"Студент '{student_name}' уже зарегистрирован на курс '{course_name}'")





if __name__ == "__main__":
    course1 = Course("Английский язык", ["Иван Иванов", "Петр Петров", "Сергей Сереев"], 15)
    print(course1)
    course2 = Course("Физика", ["Иван Иванов", "Петр Петров", "Сергей Сереев"], 4)
    course2.add_on_course("Василий Васильев")
    print(course2)
    course1.del_student("Иван Иванов")
    print(course1)

    student1 = Student("Иван Иванов", ["Математика", "Физика"], {})
    student1.add_grade("Математика", 5)
    student1.add_grade("Физика", 4)
    student1.add_course("Химия")
    student1.add_grade("Химия", 3)

    print(student1)
    print(f"Средний балл: {student1.get_average_grade()}")

    university1 = University()
    university1.add_courses(course1)
    university1.add_student(student1)







