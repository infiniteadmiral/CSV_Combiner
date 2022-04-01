import sys
import pandas as pd
import csv
import unittest




def filename_spliter(fileName):
    chunks=fileName.split("/")
    return chunks[-1]

def read_csv(fileName):
    with open (fileName) as csvfile:    
        reader=csv.reader(csvfile)

        _=next(reader)
        for row in reader:
            print(f"{row[0]},{row[1]},{filename_spliter(fileName)}")


def combiner(fileNames):
    print("email_hash, category, fileName")
    for i in range(1, len(fileNames)):
        read_csv(fileNames[i])
        

if __name__ =="__main__":  
    combiner(sys.argv)



