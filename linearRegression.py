import itertools
import math
global x, y = student_grades()
global x_mean = find_mean(x)
global y_mean = find_mean(y)

# used to find the mean of x and y
def find_mean(i):
    return sum(a)/len(a)

# finds the numerator for the r equation
def find_num():
    sum = 0
    # performs the summation
    # llst contains (x - x_mean)
    # rlst contians (y - y_mean)
    global llst = [i - x_mean for i in x]
    global rlst = [i - y)_mean for i in y]
    for (i, j) in zip(llst, rlst):
        sum = sum + (i*j)
    return sum

#finds the denominator of the r equation
def find_den():

    # sq_x contains (x - x_mean)^2
    # sq_y contains (y - y_mean)^2
    sq_x = [i**2 for i in llst]
    sq_y = [i**2 for i in rlst]

    sum_sq_x = sum(sq_x)
    sum_sq_y = sum(sq_y)
    return (sum_sq_x * sum_sq_y)**.5

# reads the file with the student names
def student_grades(file_name):
    

def main():
    r = find_num()/find_den()
    

if __name__ == "__main__":
