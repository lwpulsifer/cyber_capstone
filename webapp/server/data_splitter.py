import csv
import os
import string
from tqdm import tqdm

class DataSplitter():

    def __init__(self, path):
        self.path = os.path.join(os.getcwd(), path)   

    def get_header(self):
        with open(self.path, 'r', encoding="ISO-8859-1") as voter_data:
            reader = csv.reader(voter_data, delimiter='\t')
            header = reader.__next__() 
        return header


    def split_data(self, split_method='alpha', index=0):

        if split_method == 'alpha':
            writers = {}
            for char in string.ascii_lowercase:
                write_path = os.path.join("data", char + "-voter-data.tsv")
                writefile = open(write_path, 'w')
                writefile.truncate(0)
                writers[char] = csv.writer(writefile, delimiter='\t')
        
            with open(self.path, 'r', encoding="ISO-8859-1") as voter_data:
                reader = csv.reader(voter_data, delimiter='\t')
                header = reader.__next__() 
                for row in tqdm(reader):
                    first_char = str(row[index]).strip().lower()[0]
                    try:
                        writers[first_char].writerow(row)
                    except KeyError:
                        print(f"  Key error for key: {first_char} with last_name {row[index]}")
                


        

    
if __name__ == '__main__':
    PATH = os.path.join("data", "ncvoter_Statewide.tsv")
    vdata = DataSplitter(PATH)
    with open(os.path.join("data", "header.tsv"), 'w+') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(vdata.get_header())
     