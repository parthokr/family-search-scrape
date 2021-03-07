import tkinter as tk
from tkinter import filedialog

from family_search_scrapper import FamilySearchScrapper
from read_input import ReadInput
import multiprocessing
from multiprocessing import Pool
# from write_excel import WriteExcel
import pandas as pd
class Run(ReadInput):
    def __init__(self, worker_id, filename, start, end):
        self.worker_id = worker_id
        self.fscrapper = FamilySearchScrapper(match='approximate', filename=f'out/{start}-{end}.xlsx')
        super(Run, self).__init__(filename, start, end)
        self.execute()

    def execute(self):
        for row in self.reader:
            self.fscrapper.firstname = row[0].replace(' ', '%20')
            self.fscrapper.surname = row[1].replace(' ', '%20')
            self.fscrapper.id = row[2]
            self.fscrapper.search()
            try:
                # print(self.fscrapper.get_data())
                self.fscrapper.clear_data()
            except:
                pass
            worker_update = open(f'log/worker-{self.worker_id}.txt', 'w')
            worker_update.write(f'Total {self.fscrapper.count} rows written')
            worker_update.close()
                
if __name__ == "__main__":
    try:
        workers = 5

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        print(file_path)

        # n = int(input("Workers: "))
        # limit = [[file_path, 0, 10], [file_path, 10, 20], [file_path, 20, 30]]
        per = 1016 // 5
        rem = 1016 % 5
        workers = 5
        limits = [
            (1, file_path, 0, per)
        ]
        for i in range(2, workers+1):
            limits.append((i, file_path, limits[-1][3], limits[-1][3]  + per))
        limits[-1] = (workers, file_path, limits[-1][2], limits[-1][3] + rem)

        # print(limits)
        # with Pool(n) as p:
        #     p.map(Run, )

        p1 = multiprocessing.Process(target=Run, args=limits[0]) 
        p2 = multiprocessing.Process(target=Run, args=limits[1])
        p3 = multiprocessing.Process(target=Run, args=limits[2])
        p4 = multiprocessing.Process(target=Run, args=limits[3])
        p5 = multiprocessing.Process(target=Run, args=limits[4])

        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()

        print("Done")
    except KeyboardInterrupt:
        print('Successfully exited')
        