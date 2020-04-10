import constants


class SerializerConfigurationClass:
    def __init__(self, daysPerWeek=constants.daysPerWeek, lessonsPerDay=constants.lessonsPerDay):
        self.daysPerWeek = daysPerWeek  # Количество дней в неделе
        self.lessonsPerDay = lessonsPerDay  # Количество уроков в день


class Serializer:
    def __init__(self, config_class):
        self.daysPerWeek = config_class.daysPerWeek
        self.lessonsPerDay = config_class.lessonsPerDay

    def serialize(self, weeklySchedule):
        classes = weeklySchedule.getClasses()
        for item in classes:
            self.serializeClazzSchedule(weeklySchedule, item, str(item) + ".txt")

    def serializeClazzSchedule(self, weeklySchedule, classId, path):
        file = open(path, "w")
        for i in range(constants.daysPerWeek):
            for j in range(constants.lessonsPerDay):
                file.write(weeklySchedule.getDailyClassSchedule(classId, i).scheduledLessons[j].lesson + " ")
            file.write('\r')


class SerializerFactory:
    @staticmethod
    def CreateSerializer(config_class):
        return Serializer(config_class)
