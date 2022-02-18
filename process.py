log_file = open("um-server-01.txt") #log_file is a variable that holds a text file that will be read into a python program.


def sales_reports(log_file):    #The function sales_reports is being defined it takes in a parameter called log_file.
    for line in log_file:       #for each line in the text file that is stored in log_file 
        line = line.rstrip()    #create a variable called line that strips any trailing characters at the end of the string 
        day = line[0:3]         #create a variable called day that looks at the third entry array line
        if day == "Mon":        #if day reads "Tue"
            print(line)         #print the corresponding line with "Tue" or "Mon" once I edit the code, in it out onto the screen


sales_reports(log_file)         #sales_force function is being called and the variable log_file is being passed in as a parameter to open the text file and execute the function


