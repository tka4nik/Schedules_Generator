"""
Файл по вычислению значения приспособления.
"""


class WeeklyScheduleFitnessCalculator:
    def calculate(self, weeklySchedule):
        return self.lessonsMatch(weeklySchedule)

    def lessonsMatch(self, weeklySchedule):  # Приватный метод
        # Ищет совпадения по уроку и времени его проведения в разных учебных классах
        fitness = 0
        for i in range(len(weeklySchedule.dailyClassSchedules)):
            for j in range(len(weeklySchedule.dailyClassSchedules)):
                if (self.dailyClassScheduleMatch(weeklySchedule.dailyClassSchedules[i],
                                                 weeklySchedule.dailyClassSchedules[j])):
                    fitness += 10
        return fitness

    def dailyClassScheduleMatch(self, dailyClassScheduleA, dailyClassScheduleB):  # Приватный метод
        # Ищет совпадения уроков
        if (dailyClassScheduleA.classId == dailyClassScheduleB.classId) or (
                dailyClassScheduleA.weekDayNumber != dailyClassScheduleB.weekDayNumber):
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
    @staticmethod
    def CreateFitnessCalculator():
        return WeeklyScheduleFitnessCalculator()
