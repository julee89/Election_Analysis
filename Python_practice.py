counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
#if counties[3] != 'Jefferson':
    #print(counties[2])
    #this will create an index error because it is out of range


#Membership Operators
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties") 
#Logical Operators
#"AND"
if "Arapahoe" in counties and "El Paso" in counties:
    print ("Arapahoe and El Paso are in the list of counties.")
else:
    print("Araphoe or El Paso is not in the list of counties.")
#"OR"
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of countie")

#For Loops
#iterating through a list
for county in counties:
    print(county)
#Python has a built-in function, range(), that simplifies the process of writing a for loop. The range() function creates an iterable object or a list. 
#Indexing can also be used to iterate through a list. If the list contains strings, we'll need to get the length of the list as an integer for the 
#range() function. For example, to iterate through the counties list using the range() function, the code should be rewritten as follows:
for i in range(len(counties)):
    print(counties[i])
#Let's break down what's happening in this code.
#The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. The letter i is often used for simplicity, but any variable can be used.
#Inside the range() function, we get the length of the list of counties, which is the integer 3.
#Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
#This process is continued until all three items, or counties, in the list are printed to the screen.
#the same logic can be applied to tuples and dictionaries
#creating counties dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
#executing over keys
for county in counties_dict.keys():
    print(county)
#over values
for county in counties_dict.values():
    print(county)
#values
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
#get the key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)
#using the key paired loop and making a statement
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")

#creating list of dictionaries for voting data
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
        print(county_dict)

for i in range (len(voting_data)):
    print(voting_data[i]['county'])
for i in range (len(voting_data)):
    print(voting_data[i]['registered_voters'])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    for key,value in county_dict.items():
        print(value)
for county_dict in voting_data:
    print(county_dict['registered_voters'])
for county_dict in voting_data:
    print(county_dict['county'])

#How to print different strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
#printing using f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes*100}% of the total votes")
#f-string with dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")


#multi-lne F-strings
#The general format for a number to format it in an f-string is as follows: f'{value:{width}.{precision}}'
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the elction was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes"
)
print(message_to_candidate)


for county, voters in counties_dict.items():
    output_message = (
        f"{county} county has {voters:,} registered voters"
)
print(output_message)
