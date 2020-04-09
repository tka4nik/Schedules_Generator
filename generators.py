import random

import constants
import model


class WeeklyScheduleGenerator:
    def __init__(self, lessons):
        self.lessons = lessons
        self.classesQty = constants.classesQty
        self.lessonsPerDay = constants.lessonsPerDay
        self.daysPerWeek = constants.daysPerWeek
        self.ensureEnoughLessons()
        self.lessons_pool = []

    def ensureEnoughLessons(self):
        count = 0
        for item in self.lessons:
            count += self.lessons[item]
        if count < self.lessonsPerDay * self.daysPerWeek:
            print('Not enough Lessons!')

    def generate(self):
        dailyClassSchedules = []
        for i in range(self.classesQty):
            self.lessons_pool = self.generateLessonsPool()
            for j in range(self.daysPerWeek):
                scheduleLessons = self.generateScheduleLessons()
                dailyClassSchedules.append(model.ObjectsFactory.CreateDailyClassSchedule(self,scheduleLessons, i, j))
        return model.ObjectsFactory.CreateWeeklySchedule(self,dailyClassSchedules)

    def generateScheduleLessons(self):
        scheduleLessons = []
        for i in range(self.lessonsPerDay):
            n = round(random.random() * (len(self.lessons_pool) - 1))
            scheduleLessons.append(model.ObjectsFactory.CreateScheduledLesson(self, self.lessons_pool[n], i))
            self.lessons_pool.pop(n)
        return scheduleLessons

    def generateLessonsPool(self):
        newLessons = []
        for item in self.lessons:
            it = self.lessons[item]
            for i in range(it):
                newLessons.append(item)
        return newLessons


class GeneratorsFactory:
    def defaultGenerator(self):
        return WeeklyScheduleGenerator()
