def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e :
        print(e)

    