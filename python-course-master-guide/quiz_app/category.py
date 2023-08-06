import requests
import random
import os

from question import Question


class Category:
    def __init__(self, name, questions_string):
        print("Initialising Category object '" + name + "'")
        self.name = name
        self.questions = set()

        print("Processing questions...")
        questions = questions_string.split("\n#Q ")
        questions.pop(0)  # Remove the erranous empty string
        for i in range(len(questions)):
            question = questions[i]
            self.questions.add(Question(question))

        print("Processed", len(self.questions), "questions.")
        print("Finished initialising category.")

    @staticmethod
    def download(name):
        print("Downloading category '" + name + "'.")
        url = "https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/" + name
        cache_folder = "cache/"
        if not os.path.exists(cache_folder):
            print("Cache does not exist. Creating.")
            os.mkdir(cache_folder)
        filename = cache_folder + name + ".dat"
        print("URL: " + url)
        response = requests.get(url)
        if not response.status_code == 200:
            print("Download error code:", response.status_code)
            return
        else:
            file = open(filename, "w", encoding="utf-8")
            file.write(response.text)
            file.close()
        print("Finished download category '" + name + "'.")
        return response.text

    @staticmethod
    def read_from_file(name):
        print("Reading category '" + name + "' from file.")
        filename = "cache/" + name + ".dat"
        file = open(filename, "r", encoding="utf-8")
        contents = file.read()
        file.close()
        print("Finished reading category '" + name + "' from file.")
        return contents

    @classmethod
    def new(cls, name):
        if os.path.exists("cache/" + name + ".dat"):
            questions_string = cls.read_from_file(name)
        else:
            questions_string = cls.download(name)

        if questions_string:
            return cls(name, questions_string)
        else:
            raise IOError

    def __iter__(self):
        self.number_of_q_asked = 0
        self.asked = set()
        return self

    def __next__(self):
        self.number_of_q_asked += 1
        if self.number_of_q_asked > len(self.questions):
            raise StopIteration

        not_asked = self.questions - self.asked
        question = random.choice(list(not_asked))
        self.asked.add(question)
        return question

    def __repr__(self):
        return "Category " + repr(self.name) + " with " + str(len(self.questions)) + " questions."
