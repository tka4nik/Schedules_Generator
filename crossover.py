"""
Файл, в котором происходит скрещивание
"""

from random import random

import model
import constants


class WeeklyScheduleCrossoverConfigurationClass:
    def __init__(self, lessonsPerDay=constants.lessonsPerDay, daysPerWeek=constants.daysPerWeek):
        self.lessonsPerDay = lessonsPerDay  # Количество уроков в день
        self.daysPerWeek = daysPerWeek   # Количество дней в учбеной неделе


class WeeklyScheduleCrossover:
    def __init__(self, config_class):
        self.lessonsPerDay = config_class.lessonsPerDay
        self.daysPerWeek = config_class.daysPerWeek

    def getAllClasses(self, weeklySchedule1, weeklySchedule2):
        # Получение всех классов из двух расписаний
        classes1 = weeklySchedule1.getClasses()
        classes2 = weeklySchedule2.getClasses()
        allClasses = set(classes1)
        allClasses.union(classes2)
        r = set()
        for item in allClasses:
            r.add(item)
        return r

    def crossover(self, weeklySchedule1, weeklySchedule2):
        # Скрещивание
        newDailyClassSchedules = []
        uniqueClasses = self.getAllClasses(weeklySchedule1, weeklySchedule2)

        for classId in range(len(uniqueClasses)):
            for weekDayNumber in range(self.daysPerWeek):
                scheduledLessons1 = weeklySchedule1.getDailyClassSchedule(classId, weekDayNumber).scheduledLessons
                scheduledLessons2 = weeklySchedule2.getDailyClassSchedule(classId, weekDayNumber).scheduledLessons
                scheduleLessons = self.crossScheduledLesson(scheduledLessons1, scheduledLessons2)
                newDailyClassSchedules.append(
                    model.ObjectsFactory.CreateDailyClassSchedule(self, scheduleLessons, classId, weekDayNumber))
        return model.ObjectsFactory.CreateWeeklySchedule(self, newDailyClassSchedules)

    def crossScheduledLesson(self, scheduledLessons1, scheduledLessons2):
        # Скрещивание двух уроков
        cross = []
        for i in range(self.lessonsPerDay):
            rand = round(random())
            if rand == 0:
                cross.append(scheduledLessons1[i])
            else:
                cross.append(scheduledLessons2[i])
        return cross


class CrossoverFactory:
    @staticmethod
    def CreateDefaultCrossover(config_class):
        return WeeklyScheduleCrossover(config_class)
