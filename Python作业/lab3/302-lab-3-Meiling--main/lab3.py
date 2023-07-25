#Name:Meiling Luo
#Student Number;041068814
import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
country_code = input("Please enter the  country code:")

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
count = 0
for i in l:
    if i in country_code:
        count += 1

#Format and print the result
print('there are '+str(count)+' similar country codes have appeared ')


#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
winter = True
while winter == True:
    try:
        population = int(input("please enter the population value:"))
        print("the population you input is:", population)
    except:
        print("Your input should be a valid integer")
    else:
        break

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = list()

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
for i in l1:
    if i > population:
        lstOfRecords.append(i)

#Print the list l1
print("The population list is: ", l1)


#Bonus: Print the name of the cities whose index is in l1
listOfCity = list(db.ws(ws='Sheet1').col(col=2))
print("Name of the cities:")
for index, i in enumerate(l1):
    print(listOfCity[index])