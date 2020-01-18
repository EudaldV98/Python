import csv
import pdb


class CsvReader():
    def __init__(self, filename, sep = ',', header = False, skip_top = 0, skip_bottom = 0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass
    
    def getdata(self):
        file = open(self.filename, 'r')
        reader = csv.reader(file, delimiter = self.sep)
        if not self.header:
            next(reader)
        res = []
        for row in reader:
            res.append(row)
        return res
    
    def getheader(self):
        file = open(self.filename, 'r')
        reader = csv.reader(file)
        return next(reader)
