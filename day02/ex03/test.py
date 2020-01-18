from csvreader import CsvReader
import sys

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file == None:
            print('File is corrupted')
        data = file.getdata()
        header = file.getheader()
        prev_out = sys.stdout
        sys.stdout = open('res.txt', 'w')
        for i in data:
            print(i)
        sys.stdout = open('header.txt', 'w')
        print(header)
        sys.stdout = prev_out
    
