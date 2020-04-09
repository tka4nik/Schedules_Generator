from random import random

import model
import constants


class WeeklyScheduleCrossover:
    def getAllClasses(self, weeklySchedule1, weeklySchedule2):
        classes1 = weeklySchedule1.getClasses()
        classes2 = weeklySchedule2.getClasses()
        allClasses = set(classes1)
        allClasses.union(classes2)
        r = set()
        for item in allClasses:
            r.add(item)
        return r

    def crossover(self, weeklySchedule1, weeklySchedule2):
        newDailyClassSchedules = []
        uniqueClasses = self.getAllClasses(weeklySchedule1, weeklySchedule2)

        for classId in range(len(uniqueClasses)):
            for weekDayNumber in range(5):
                scheduledLessons1 = weeklySchedule1.getDailyClassSchedule(classId, weekDayNumber).scheduledLessons
                scheduledLessons2 = weeklySchedule2.getDailyClassSchedule(classId, weekDayNumber).scheduledLessons
                scheduleLessons = self.crossScheduledLesson(scheduledLessons1, scheduledLessons2)
                newDailyClassSchedules.append(
                    model.ObjectsFactory.CreateDailyClassSchedule(self, scheduleLessons, classId, weekDayNumber))
        return model.ObjectsFactory.CreateWeeklySchedule(self, newDailyClassSchedules)

    def crossScheduledLesson(self, scheduledLessons1, scheduledLessons2):
        cross = []
        for i in range(constants.lessonsPerDay):
            rand = round(random())
            if rand == 0:
                cross.append(scheduledLessons1[i])
            else:
                cross.append(scheduledLessons2[i])
        return cross


class CrossoverFactory:
    def CreateDefaultCrossover(self):
        return WeeklyScheduleCrossover()
