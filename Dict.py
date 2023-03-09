'''
Created on Feb 1, 2023

@author: CCaliboso24
'''
import csv   
def main():  

    try:                                                            #try: to open TN.txt file
        file1 = open("TN.txt", 'r')
    except:                                                         #except: print text that it failed and end code
        print('File cannot be opened:')
        exit()                          

    TN = dict()                                                     #variable, TN (Twelfth Night) - dictionairy
    for line in file1:                                              #For loop, convert every word to uppercase and split every word
        line = line.upper()
        words = line.split()
        for word in words:                                          #For loop, for each word, count its frequency and record it
            if word not in TN:
                TN[word] = 1
            else:
                TN[word] += 1

    try:                                                            #try: to open NE.txt file
        file2 = open("NE.txt", 'r')
    except:                                                         #except: print text that it failed and end code
        print('File cannot be opened:')
        exit()

    NE = dict()                                                     #variable, TN (No Exit) - dictionairy
    for line in file2:                                              #For loop, convert every word to uppercase and split every word
        line = line.upper()
        words = line.split()
        for word in words:                                          #For loop, for each word, count its frequency and record it
            if word not in NE:
                NE[word] = 1
            else:
                NE[word] += 1


    with open('NECSV.csv', 'w', newline='') as f:                   #program creates a csv file called "NECSV.csv" using the NE dictionary
        writer = csv.writer(f)
        for row in NE.items():                                      #For loop, converts dictionary element by element into rows for the csv file
            if row[1] >= 20:                                        #condtitional, if frequency of word is greater than or equal to 20, push to the csv file
                writer.writerow(row)  
            else:                                                   #conditional, else, skip the the word
                pass
    
    with open('TNCSV.csv', 'w', newline='') as f:                   #program creates a csv file called "TNCSV.csv" using the TN dictionary
        writer = csv.writer(f)
        for row in TN.items():                                      #For loop, converts dictionary element by element into rows for the csv file
            if row[0] == "I" or row[0] == "A":                      #conditional, if the word in the tuple is "I" or "A", skip it
                pass
            elif row[1] >= 20:                                      #condtitional, elif frequency of word is greater than or equal to 20, push to the csv file
                writer.writerow(row)  



if __name__ == "__main__":
    main() 