import pandas as pd
import os

class VoterDataProcessor():

    def __init__(self, datapath):
        self.path = os.path.join(os.getcwd(), datapath)
        print(self.path)



if __name__ == '__main__':
    PATH = os.path.join("data", "ncvoter_Statewide.tsv")
    vdata = VoterDataProcessor(PATH)