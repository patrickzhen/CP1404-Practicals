def main():
    score = float(input("Enter Score: "))
    print(status(score))

def status(score):
    if score < 0 or score > 100:
        return "Invalid Score"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Passable"

    elif score < 50:
        return "Bad"


main()