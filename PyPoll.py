# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canddiate won
#5. The winner of the election based on the popular vote

#Path = C:\Users\Junlee\Desktop\DataClass\Election_Analysis\Resources\election_results.csv

#Import the datetime class from the datetime module.
import datetime as dt

#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

#Print the present time.
present_time = f'The time right now is {now}'
print(present_time)

#Add out dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')


#Create a filename variable to a direct or indirect path ot the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Format for opening a file is file_variable = open (filename, mode)
#file_variable = name of the variable that will reference the file
#file_name = name of the file
#mode = what to do with file [ r - read, w - write, x - open for exclusive creation, a - append to existing file, + - open for reading/writing]

#Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    #txt_file.write("Hello World")

    #write three counties to the file.
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print each row in the CSV file.
    for row in file_reader:
        print(row)


    #Read and Print the header row.
    headers = next(file_reader)
    print(headers)



#Close the file.
#election_data.close()
