import constants
import csv


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
        for i in range(self.daysPerWeek):
            for j in range(self.lessonsPerDay):
                file.write(weeklySchedule.getDailyClassSchedule(classId, i).scheduledLessons[j].lesson + " ")
            file.write('\r')


class CsvSerializer:
    def __init__(self, config_class):
        self.daysPerWeek = config_class.daysPerWeek
        self.lessonsPerDay = config_class.lessonsPerDay

    def csv_writer(self, data, path):
        with open(path, "w", newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerow(line)

    def serialize(self, weeklySchedule):
        classes = weeklySchedule.getClasses()
        for item in classes:
            self.serializeClazzSchedule_csv(weeklySchedule, item)

    def serializeClazzSchedule_csv(self, weeklySchedule, classId):
        data = [
            "Понедельник,Вторник,Среда,Четверг,Пятница,Суббота".split(",")
        ]
        for i in range(self.lessonsPerDay):
            line = ""
            for j in range(self.daysPerWeek):
                line += str(weeklySchedule.getDailyClassSchedule(classId, j).scheduledLessons[i].lesson)
                line += ","
            line = line[0:len(line) - 1]
            #print(line)

            data.append(line.split(","))
            #print(data)

        path = "outputs/class_" + str(classId) + ".csv"
        self.csv_writer(data, path)


class SerializerFactory:
    @staticmethod
    def CreateSerializer(config_class):
        return Serializer(config_class)

    @staticmethod
    def CreateCsvSerializer(config_class):
        return CsvSerializer(config_class)
