def safe_divide(numerator, denominator):
    try:
        division = numerator/denominator
        return division
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e :
        print(e)

    