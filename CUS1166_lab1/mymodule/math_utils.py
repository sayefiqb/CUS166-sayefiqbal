def average_grade(roster):
    total = 0
    for student in roster:
        total = total + student.get_grade()
    average = total /len(roster)
    return average

def main():
    pass

if __name__ == "__main__":
    main()
