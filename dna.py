import sys
import csv

# check for correct user input
if len(sys.argv) != 3:
    print("Provide all files")
    exit(1)
    

def main():
    # open up file of dna suspects
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        strs = next(reader)
        del strs[0]
        reader1 = csv.reader(file)
        suspects = []
        for row in reader1:
            suspects.append(row)
    # open file of dna sequences   
    with open(sys.argv[2], "r") as file1:
        sequence = file1.read()
    # loop to check for dna matching
    for i in range(len(suspects)):
        check = True
        for j in range(len(strs)):
            if str(repetitions(strs[j], sequence)) != suspects[i][j+1]:
                check = False
                break
            
        if check == True:
            print(suspects[i][0])
            break  
    
    if check == False:
        print("No match")
    

def repetitions(index, sequence):
    number = []
    for k in range(len(sequence)):
        count = 0
        m = k
        j = k + len(index)
        for i in range(round(len(sequence)/len(index))):
            if sequence[m:j] == index:
                count += 1
                m += len(index)
                j += len(index)
            else:
                number.append(count)
                break
    maximum = max(number)
    return maximum


if __name__ == "__main__":
    main()

