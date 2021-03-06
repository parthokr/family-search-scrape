import csv
class ReadInput:
    def __init__(self, filename):
        filename = open(filename, 'r')
        self.reader = list(csv.reader(filename))[1:10]
        for row in self.reader:
            print(row)

    # def get_data(self):
    #     return self.reader

if __name__ == '__main__':
    obj = ReadInput('input/Name_csv.csv')