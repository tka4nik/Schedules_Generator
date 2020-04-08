import constants


class Serializer:
    def serialize(self, weeklySchedule):
        classes = weeklySchedule.getClasses()
        for item in classes:
            self.serializeClazzSchedule(weeklySchedule, item, str(item)+".txt")

    def serializeClazzSchedule(self, weeklySchedule, classId, path):
        file = open(path, "w")
        for i in range(constants.daysPerWeek):
            for j in range(constants.lessonsPerDay):
                file.write(weeklySchedule.getDailyClassSchedule(classId, i).scheduledLessons[j].lesson)
            file.write('\n')

class SerializerFactory:
    def CreateSerializer(self):
        return Serializer