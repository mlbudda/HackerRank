#%%
def getPrecentage(student_marks, query_name):
    return f'{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}'

# Run some tests...
print(getPrecentage({
    'Krishna': [67.0, 68.0, 69.0], 
    'Arjun': [70.0, 98.0, 63.0], 
    'Malika': [52.0, 56.0, 60.0]}, 'Krishna') == '68.00')