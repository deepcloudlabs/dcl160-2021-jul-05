def fun():
    try:
        0/0
        return 108
    except:
        print("Something is wrong!")
        return 42
    finally:
        return 549


print(fun())
