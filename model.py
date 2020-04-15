"""
Файл, в котором хранятся все модели программы
"""


class WeeklySchedule:
    """
    Главный класс расписания
    """

    def __init__(self, dailyClassSchedules):
        self.dailyClassSchedules = dailyClassSchedules

    def getDailyClassSchedule(self, classId, weekDayNunmber):
        for i in range(len(self.dailyClassSchedules)):
            if classId == self.dailyClassSchedules[i].classId \
                    and weekDayNunmber == self.dailyClassSchedules[i].weekDayNumber:
                return self.dailyClassSchedules[i]

    def getClasses(self):
        r = set()
        for item in self.dailyClassSchedules:
            r.add(item.classId)
        return r


class DailyClassSchedule:
    """
    Класс одного дня
    """

    def __init__(self, scheduledLessons, classId, weekDayNumber):
        self.scheduledLessons = scheduledLessons
        self.classId = classId
        self.weekDayNumber = weekDayNumber

    def getLessonsCount(self):
        return len(self.scheduledLessons)


class ScheduledLesson:
    """
    Класс одного урока
    """

    def __init__(self, lesson, lessonNumber):
        self.lesson = lesson
        self.lessonNumber = lessonNumber

    def IfEqual(self, scheduledLesson):
        return self.lesson == scheduledLesson.lesson and self.lessonNumber == scheduledLesson.lessonNumber


class ObjectsFactory:
    def CreateScheduledLesson(self, lesson, lessonNumber):
        return ScheduledLesson(lesson, lessonNumber)

    def CreateDailyClassSchedule(self, scheduledLessons, classId, weekDayNumber):
        return DailyClassSchedule(scheduledLessons, classId, weekDayNumber)

    def CreateWeeklySchedule(self, dailyClassSchedules):
        return WeeklySchedule(dailyClassSchedules)
