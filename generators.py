import random

import constants
import model


class WeeklyScheduleGenerator:
    def __init__(self, lessons):
        self.ensureEnoughLessons()
        self.lessons = lessons
        self.classesQty = constants.classesQty
        self.lessonsPerDay = constants.lessonsPerDay
        self.daysPerWeek = constants.daysPerWeek

    def ensureEnoughLessons(self):
        count = 0
        for item in range(len(self.lessons)):
            count += self.lessons[item]
        if count < self.lessonsPerDay * self.daysPerWeek:
            print('Not enough Lessons!')

    def generate(self):
        dailyClassSchedules = []
        for i in range(len(self.classesQty)):
            lessons_pool = self.generateLessonsPool()
            for j in range(self.daysPerWeek):
                scheduleLesson = self.generateScheduleLessons(lessons_pool)
                dailyClassSchedules.append(model.ObjectsFactory.CreateDailyClassSchedule(scheduleLesson, i, j))
        return model.ObjectsFactory.CreateWeeklySchedule(dailyClassSchedules)

    def generateScheduleLessons(self, lessons):
        scheduleLessons = []
        for i in range(self.lessonsPerDay):
            n = random.randint(0, len(lessons) - 1)
            scheduleLessons[i] = model.ObjectsFactory.CreateScheduledLesson(lessons[n], i)
            lessons.pop(n)
        return lessons, scheduleLessons

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
