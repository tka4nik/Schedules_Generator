class WeeklyScheduleFitnessCalculator:
    def calculate(self, weeklySchedule):
        return self.lessonsMatch(weeklySchedule)

    def lessonsMatch(self, weeklySchedule):
        fitness = 0
        for i in range(len(weeklySchedule.dailyClassSchedules)):
            for j in range(len(weeklySchedule.dailyClassSchedules)):
                if (self.dailyClassScheduleMatch(weeklySchedule.dailyClassSchedules[i], weeklySchedule.dailyClassSchedules[j])):
                    fitness += 10
        return fitness

    def dailyClassScheduleMatch(self, dailyClassScheduleA, dailyClassScheduleB):
        if (dailyClassScheduleA.classId == dailyClassScheduleB.classId) or (dailyClassScheduleA.weekDayNumber != dailyClassScheduleB.weekDayNumber):
            return False
        else:
            for i in range(len(dailyClassScheduleA.scheduledLessons)):
                for j in range(len(dailyClassScheduleB.scheduledLessons)):
                    scheduleA = dailyClassScheduleA.scheduledLessons[i]
                    scheduleB = dailyClassScheduleB.scheduledLessons[j]
                    if scheduleA.IfEqual(scheduleB):
                        return True
        return False

class FitnessFactory:
    def CreateFitnessCalculator(self):
        return WeeklyScheduleFitnessCalculator()