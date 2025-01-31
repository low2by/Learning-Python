def revList(lst):
    # Here is the base case
    if lst == []:
        return []

    # The rest of this function is the recursive case.
    # This works because we called it on something smaller.
    # The lst[] is a slice of all but the first item in lst.
    restrev = revList(lst[1:])
    first = lst[:1]

    # Now put the pieces together.
    result = restrev + first

    return result


def revString(s):
    if s == "":
        return ""

    restrev = revString(s[1:])
    first = s[:1]

    # Now put the pieces together.
    result = restrev + first

    return result


def main():
    print(revList([1,2,3,4]))
    print(revString("Hello World"))

if __name__ == "__main__":
    main()