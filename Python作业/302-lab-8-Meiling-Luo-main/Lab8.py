
#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. Each grade is in between 0 and 100.
#Returns the number of Tests
def getNumberOfTests():
    while True:
        try:
            num = int(input("Please input the number of test"))
        except:
            print("Please input a number")
        else:
            break
    return num


#Prompts the user for the weight of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments

def getWeightOfAssignments():
    while True:
        try:
            wAssign = float(input("Please input the weight of assignment"))
            if wAssign < 0 or wAssign > 1:
                print("please enter a number between o-1")
                continue
        except ValueError:
            print("Invalid input")
        else:
            break

    return wAssign




#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    while True:
        try:
            wMidTerms = float(input('please input the weight of midterms between 0 and 1'))
            if wMidTerms < 0 or wMidTerms >1:
                print("please enter a number between o-1")
                continue
        except:
                print("Invalid input")
        else:
                break

    return wMidTerms


#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    while True:
        try:
            w_final = float(input('please input the weight of final between 0 and 1'))
            if wFinal < 0 or wFinal > 1:
                print("please enter a number between o-1")
                continue
        except ValueError:
            print("Invalid input")
        else:
            break
    return wFinal




#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to w_final, wMidtern and wFinal respectively
def checkWeights(wAssign,wMidTerms,wFinal):
    if wAssign + wMidTerms + wFinal == 1:
        return True
    else:
        return False

checkWeights(0.4, 0.35, 0.25)


#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wAssign,wMidTerms,wFinal):
    numericGrade = (AvgAssignments*wAssign)+(AvgTests*wMidTerms)+(final*wFinal)
    return numericGrade

#convert the numeric grade to a letter according to the conversion table in the course outline
def calculateLetterGrade(numericGrade):
    if numericGrade >= 90:
        gradeScale = "A+"
    elif 89 > numericGrade >= 85:
        gradeScale = "A"
    elif 84 > numericGrade >= 80:
        gradeScale = "A-"
    elif 79 > numericGrade >= 77:
        gradeScale = "B+"
    elif 76 > numericGrade >= 73:
        gradeScale = "B"
    elif 72 > numericGrade >= 70:
        gradeScale = "B-"
    elif 69 > numericGrade >= 67:
        gradeScale = "C+"
    elif 66 > numericGrade >= 63:
        gradeScale = "C"
    elif 62 > numericGrade >= 60:
        gradeScale = "C+"
    else:
        gradeScale = "C-"

    return gradeScale


#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
    while True:
        wAssign = getWeightOfAssignments()
        wMidTerms = getWeightOfMidTerms()
        wFinal = getWeightOfFinal()
        if checkWeights(wAssign, wMidTerms, wFinal):
            break
        else:
            print('The sum is not equal to one')




#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100
while True:
        try:
            avgAssignment = float(input("Please input your average grade of assignment"))
            if avgAssignment < 0 or avgAssignment > 100:
                print("Please enter a number between 0 and 100")
                continue
        except:
            print("Please enter a float number")
        else:
            break

#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.
numberOfTests = getNumberOfTests()
i = 0
Sum = 0
while i < numberOfTests:
        while True:
            try:
                testGrade = float(input("Please enter your grade of test" + str(i+1)))
                if testGrade < 0 or testGrade > 100:
                    print("The number should be between 0 and 100")
                    continue
                i += 1
            except:
                print("The number should be a float")
            else:
                Sum = Sum + testGrade
                break

avgGrade = Sum / numberOfTests

#Prompt and get the final grade
#Validate the input as a float between 0 and 100
while True:
    try:
        finalGrade = float(input("Please enter the grade of final"))
        if finalGrade < 0 or finalGrade > 100:
            print("The number should be between 0 and 100")
            continue
    except:
        print("The number should be a float")
    else:
        break
#Calculate and display the final numeric grade (call the appropriate function)
finalGrade = calculateNumericGrade(avgAssignment,avgGrade,finalGrade, wAssign, wMidTerms, wFinal)
print("Your final grade is:"+str(finalGrade))
#Calculate and display the final alphabetical grade (call the appropriate function)
finalAlphabeticalGrade = calculateLetterGrade(finalGrade)
print("Your final grade scale is:"+finalAlphabeticalGrade)


