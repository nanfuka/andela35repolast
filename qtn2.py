def qtn3(lines):
    lines.upper()
    return lines


def qtn4(numbers):
    goodnumber = []
    for number in numbers:
        if number % 5 == 0:
            goodnumber.append(number)
            return goodnumber
        return none