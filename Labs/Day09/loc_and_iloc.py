import pandas as pd


stud_dictionary = {
    "RRR" : 100,
    "Mr. ABC" : 55,
    "Miss. M" : 75,
    "Mr. MNP" : 66
}

students=pd.Series(stud_dictionary)
print(students)
print(students.iloc[2])
print(students.loc['RRR'])

print(students[students > 80])