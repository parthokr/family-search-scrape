import csv
class ReadInput:
    def __init__(self, filename, start, end):
        filename = open(filename, 'r')
        print("Reading CSV...")
        self.reader = list(csv.reader(filename))[start:end]
        # for row in self.reader:
        #     print(row)

    # def get_data(self):
    #     return self.reader

if __name__ == '__main__':
    obj = ReadInput('input/Name_csv.csv', 0, 10)