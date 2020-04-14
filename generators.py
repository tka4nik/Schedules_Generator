"""
Файл с генераторами. В этом файле хранится генератор расписания со всеми последующими
генераторами - Недели, дня, урока.
"""


import random
import constants
import model


class WeeklyScheduleGeneratorConfigurationClass:
    def __init__(self, lessons, classesQty=constants.classesQty,
                 lessonsPerDay=constants.lessonsPerDay, daysPerWeek=constants.daysPerWeek):
        self.lessons = lessons  # Список уроков и их количество
        self.classesQty = classesQty  # Количество классов
        self.lessonsPerDay = lessonsPerDay  # Количество уроков в день
        self.daysPerWeek = daysPerWeek  # Количество дней в неделе


class WeeklyScheduleGenerator:
    def __init__(self, config_class):
        self.lessons = config_class.lessons
        self.classesQty = config_class.classesQty
        self.lessonsPerDay = config_class.lessonsPerDay
        self.daysPerWeek = config_class.daysPerWeek
        self.ensureEnoughLessons()
        self.lessons_pool = []

    def ensureEnoughLessons(self):
        # Проверка на то, что уроков достаточно
        count = 0
        for item in self.lessons:
            count += self.lessons[item]
        if count < self.lessonsPerDay * self.daysPerWeek:
            print('Not enough Lessons!')

    def generate(self):
        # Генерация расписания
        dailyClassSchedules = []
        for i in range(self.classesQty):
            self.lessons_pool = self.generateLessonsPool()
            for j in range(self.daysPerWeek):
                scheduleLessons = self.generateScheduleLessons()
                dailyClassSchedules.append(model.ObjectsFactory.CreateDailyClassSchedule(self, scheduleLessons, i, j))
        return model.ObjectsFactory.CreateWeeklySchedule(self, dailyClassSchedules)

    def generateScheduleLessons(self):
        # Генерация массива уроков на день
        scheduleLessons = []
        for i in range(self.lessonsPerDay):
            n = round(random.random() * (len(self.lessons_pool) - 1))
            scheduleLessons.append(model.ObjectsFactory.CreateScheduledLesson(self, self.lessons_pool[n], i))
            self.lessons_pool.pop(n)
        return scheduleLessons

    def generateLessonsPool(self):
        # Генерация массива уроков
        newLessons = []
        for item in self.lessons:
            it = self.lessons[item]
            for i in range(it):
                newLessons.append(item)
        return newLessons


class GeneratorsFactory:
    @staticmethod
    def defaultGenerator(config_class):
        return WeeklyScheduleGenerator(config_class)
