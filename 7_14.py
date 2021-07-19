'''
Dates can be written differently depending where you are in the world 05.05.2021 (the fifth of may 2021) 03.05.2021 (the third of may 2021 -> Europe, the 5th of march 2021 -> US) 05.03.2021 (the fifth of march 2021 -> Europe, the 3th of may 2021 -> US)
Sample Inputs (strings '05.05.2021'):
05.05.2021 -> non-ambiguous
03.05.2021 -> ambiguous
05.03.2021 -> ambiguous

* Also reject invalid dates


Write a function that detects if a date, written in the format NN.NN.NNNN where n is a digit [0-9] is ambiguous
save all the dates of the year that are ambiguous and print to user
part 2) add user input and using a try catch block to catch errors 
Extra: write a function that converts the format NN.NN.NNNN to a date such as "the 5th of May, 2021" (HINT: Use string formatting, and lists of strings)
January - 31 days.
February - 28 days in a common year and 29 days in leap years.
March - 31 days.
April - 30 days.
May - 31 days.
June - 30 days.
July - 31 days.
August - 31 days.'''