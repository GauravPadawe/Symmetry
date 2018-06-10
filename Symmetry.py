x = [[1,2,3],
    [2,3,1],
    [3,1,2]]
    
def check(x):                          # Defining procedure
    a = len(x)                         # Length of Rows
    b = len(x[0])                      # Length of Columns
    if a != b:                         # If Rows and Columns aren't equal print False
        print ("False")
    i = 0                              # Defining 2 variables with 0 as initial value
    while i <= (a - 1):                # Initialise While loop with condition i <= 
        j = 0
        while j <= (a - 1):            # for each entry in ith row/column
            if x[i][j] != x[j][i]:     # If x[i][j] is not equals to x[j][i] print false and add i and j by 1
                print ("False")       
            j = j + 1                  # Update value to check each and every value of rows and columns
        i = i + 1
    print ("True")                     # If condition passes then print out desired statement
    
print (check(x))

# CODED BY - GAURAV PADAWE
