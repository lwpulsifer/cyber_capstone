import csv
import os
import string
from tqdm import tqdm

class DataSplitter():

    def __init__(self, path):
        self.path = os.path.join(os.getcwd(), path)    

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
                for row in tqdm(reader):
                    first_char = str(row[index]).strip().lower()[0]
                    try:
                        writers[first_char].writerow(row)
                    except KeyError as e:
                        print(f"  Key error for key: {first_char} with last_name {row[index]}")
                


        

    
if __name__ == '__main__':
    PATH = os.path.join("data", "ncvoter_Statewide.tsv")
    vdata = DataSplitter(PATH)
    vdata.split_data(index=9)