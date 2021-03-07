import os
import sys
import glob
import tkinter as tk
from tkinter import filedialog

from service.family_search_scrapper import FamilySearchScrapper
from service.read_input import ReadInput

import multiprocessing
from multiprocessing import Pool

import pandas as pd


class Run(ReadInput):
    def __init__(self, worker_id, filename, start, end, count = 0):
        filename_with_path = f'out/{start+1}-{end}.xlsx'
        self.worker_id = worker_id
        if (count != 0):
            filename_with_path = f'out/{start+1 - count}-{end}.xlsx'
        self.fscrapper = FamilySearchScrapper(match='approximate', filename = filename_with_path, count = count)
        self.fscrapper.count = count
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
            worker_update.write(f'Total {self.fscrapper.count} rows written\nUnfinished')
            worker_update.close()

        read_file = open(f'log/worker-{self.worker_id}.txt', 'r')
        written = read_file.readlines()[0]
        read_file.close()

        mark_finished = open(f'log/worker-{self.worker_id}.txt', 'w')
        mark_finished.write(f'{written}Finished')
        mark_finished.close()
        
                

def change_offset_of_limit_if_unfinished(total_row, workers, limits):
    for i in range(1, workers + 1):
        worker_update = open(f'log/worker-{i}.txt', 'r')
        content = worker_update.readlines()
        last_line = content[-1]
        if (last_line == 'Unfinished'):
            ended_at = int(content[0].split(' ')[1])
            limits[i-1] = (limits[i-1][0], limits[i-1][1], limits[i-1][2] + ended_at, limits[i-1][3], ended_at)

    return limits

def clear_history():
    folders = glob.glob('out/')
    for fo in folders:
        file = glob.glob(f'{fo}/*')
        for f in file:
            os.remove(f)
    folders = glob.glob('log/')

    for fo in folders:
        file = glob.glob(f'{fo}/*')
        for f in file:
            os.remove(f)
    
    print('Cleared old files')

def merge_worksheets(excel_names):
        # read them in
        excels = [pd.ExcelFile(name) for name in excel_names]

        # turn them into dataframes
        frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

        # delete the first row for all frames except the first
        # i.e. remove the header row -- assumes it's the first
        frames[1:] = [df[1:] for df in frames[1:]]

        # concatenate them..
        combined = pd.concat(frames)

        # write it out
        combined.to_excel("out/merged.xlsx", header=False, index=False)

        print(f'merged.xlsx has been thrown at {os.getcwd()}\\out\\merged.xlsx')

if __name__ == "__main__":
    try:
        if '--clear' in sys.argv:
            clear_history()
            sys.exit(0)

        if '--merge' in sys.argv:
            partial_files = os.listdir('out/')
            partial_files = [f'out/{file}' for file in partial_files]
            merge_worksheets(partial_files)
            sys.exit(0)


        should_resume = '--resume' in sys.argv

        workers = 5
        total_row = None
        match = 'exact'

        for arg in sys.argv:
            if (arg.startswith('--row')):
                total_row = int(arg.split('=')[1])
            
            if (arg.startswith('--match')):
                match = arg.split('=')[1]
                if(match != 'exact' and match != 'approximate'):
                    raise ValueError('Match criteria must be either exact or approximate')

        if (total_row is None):
            raise Exception('You must provide row count')

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if (not file_path.endswith('.csv')):
            raise TypeError('File type must be CSV')
        print(f'Input provided from: {file_path}')

        # n = int(input("Workers: "))
        # limit = [[file_path, 0, 10], [file_path, 10, 20], [file_path, 20, 30]]
        per = total_row // workers
        rem = total_row % workers

        limits = [
            (1, file_path, 0, per, 0)
        ]
        for i in range(2, workers+1):
            limits.append((i, file_path, limits[-1][3], limits[-1][3]  + per, 0))
        limits[-1] = (workers, file_path, limits[-1][2], limits[-1][3] + rem, 0)
        
        if should_resume:
            try:
                limits = change_offset_of_limit_if_unfinished(total_row, workers, limits)
            except FileNotFoundError:
                print('Resume is not possible due to deletion of logs and partially downloaded files')
                sys.exit(0)
        else:
            clear_history()

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
        
        partial_files = os.listdir('out/')
        partial_files = [f'out/{file}' for file in partial_files]
        merge_worksheets(partial_files)
    except KeyboardInterrupt:
        print('Successfully exited')
        