##############################################################################################################
# Name: Tarek Hisham Ahmed Fouad
#
# This program reads 2 txt files (one is the population file and the other is the area file)
# then asks the user to enter the name of the destination file. Then the density of the ghost
# town is calculated and placed in the new txt file with the name the user input.
#
##############################################################################################################

#Setting CONSTANT vars
POPULATION_FILE = "GhostTownPop.txt"
AREA_FILE = "GhostTownArea.txt"
REPORT_FILE = "GhostTownPopDensity.txt"

def main():

    #User Input that grabs the files
    print ("Density calculator\n\nGive this program the names of the files that contain the population and area\nand a name for a destination file where the density is going to be calculated.\n(!!WHEN TYPING THE FILE NAMES DO NOT FORGET TO INCLUDE .txt extension AFTER THE NAME!!)\n")
    print ("The file names have already been included in the code! Just write the name of the destination .txt file!\n")
    reportFile1 = input("What file namewould you like to save to?") 
    
    #Opening the files the user called
    popFile =  open(POPULATION_FILE, "r")
    areaFile = open(AREA_FILE, "r")
    reportFile = open(reportFile1, "w")

    popData = extractDataRecord(popFile) #Starting thw while statment
    #Just a header for the .txt output file
    Greeting = "   Town Name\t\t     Density\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    reportFile.write(Greeting)
    while len(popData) == 2: #when the popFile list has 2 items its true
        areaData = extractDataRecord(areaFile) #extraxt the area file lines into lists
        #extract the data from both lists
        Town = popData[0] 
        Population = popData[1]
        Area = areaData[1]
        #creats density and makes the calc
        density=0.0
        if Area>0: #check if area is 0
            Density=Population/Area
        reportFile.write(f"%-25s%10.2f\n"%(Town, Density))
        #Reads the next population record if false loop ends
        popData=extractDataRecord(popFile)
    popFile.close()
    areaFile.close()
    reportFile.close()
    print(f"All Done! The file name is saves as {reportFile1} have a great day!")

def extractDataRecord(inFile): #This Runs both Files and grabs the lines to make them a list
    line = inFile.readline()
    if line == "": #if line is empty send back an empty list
        return[]
    else:           #else right Split the line at the first space and turn the part on the left to an int
        parts=line.rsplit(" ",1)
        parts[1]=int(parts[1])
        return parts

if __name__ == '__main__':
    main()
