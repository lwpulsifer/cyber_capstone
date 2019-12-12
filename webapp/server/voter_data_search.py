import os
import csv

class VoterDataSearch():

    def __init__(self, prefix='data', postfix="-voter-data.tsv"):
        self.prefix = prefix
        self.postfix = postfix
    
    def getPath(self, last_name):
        '''
        Takes in last_name of the person to search
        and returns a file path of the form
        prefix/{first character of last_name}-voter-data.tsv
        '''
        return os.path.join(os.getcwd(), self.prefix, last_name.lower()[0] + self.postfix)

    def process_line(self, line):
        '''
        Processes a tsv line with the header from data/header.tsv
        '''
        header_path = os.path.join(self.prefix, "header.tsv")
        with open(header_path, 'r') as header_file:
            header = csv.reader(header_file, delimiter='\t').__next__()
        val_dict = {header[x]: line[x] for x in range(len(line))}
        return val_dict
    
    def checkLine(self, line, index, last_name, first_name, mi):
        if line[index].strip().lower() == last_name.lower() and \
            line[index + 1].strip().lower() == first_name.lower():
            if mi and line[index + 2].strip().lower().startswith(mi.lower()):
                return True
            if not mi:
                return True
        return False

    def search(self, first_name="", last_name="", mi="", index=9):
        path = self.getPath(last_name)
        # matches = []
        with open(path, 'r') as filepath:
            reader = csv.reader(filepath, delimiter='\t')
            for line in reader:
                if self.checkLine(line, index, last_name, first_name, mi):
                    return True, self.process_line(line)
        return False, {"Person not found": "ERROR"}

if __name__ == '__main__':
    search = VoterDataSearch()
    print(search.search(first_name="Liam", last_name="Pulsifer"))