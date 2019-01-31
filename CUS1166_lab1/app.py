from mymodule.models import Student
from mymodule.math_utils import average_grade

def main():
    student1 = Student("Sayef Iqbal", 89)
    student2 = Student("Christian George", 90)
    student3 = Student("John Doe", 61)
    student4 = Student("Phillip Ross", 78)
    student5 = Student("Louise Chan", 48)
    student6 = Student("Michael Meyer", 73)
    student7 = Student("Ronald Goldsmith", 93)
    student8 = Student("Mitchel Johnson", 83)
    student9 = Student("Kim Dustin", 90)
    student10 = Student("Rebecca Waterhouse", 44)

    roster = [student1,student2,student3,student4,student5,student6,
    student7,student8,student9,student10]

    average = average_grade(roster)
    print(f"The average score for the roster is: {average}")

if __name__ == "__main__":
    main()
