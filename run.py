from family_search_scrapper import FamilySearchScrapper
from read_input import ReadInput
import multiprocessing
class Run(ReadInput):
    def __init__(self, filename, start, end):
        self.fscrapper = FamilySearchScrapper(match = 'exact')
        super(Run, self).__init__(filename, start, end)
        self.execute()

    def execute(self):
        for row in self.reader:
            self.fscrapper.firstname = row[0]
            self.fscrapper.surname = row[1]

            self.fscrapper.search()
            try:
                print(self.fscrapper.get_data())
                self.fscrapper.clear_data()
            except:
                pass
                
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=Run, args=('input/Name_csv.csv', 0, 10)) 
    p2 = multiprocessing.Process(target=Run, args=('input/Name_csv.csv', 10, 20))
    p3 = multiprocessing.Process(target=Run, args=('input/Name_csv.csv', 20, 30 ))
    

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Done")
    