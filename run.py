from family_search_scrapper import FamilySearchScrapper
from read_input import ReadInput
class Run(ReadInput):
    def __init__(self, filename):
        self.fscrapper = FamilySearchScrapper(match = 'exact')
        super(Run, self).__init__(filename)

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
    obj = Run('input/Name_csv.csv')
    obj.execute()
    