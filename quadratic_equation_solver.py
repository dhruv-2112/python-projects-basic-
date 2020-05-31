while True:
    import cmath

    print ("This is a quadraric equation solver")
    print ("form: ax^2 + bx + c")

    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))

    #calculate discriminant
    dis = (b**2) - (4*a*c)

    # calculate solutions
    solution_1 = (-b + cmath.sqrt(dis))/(2*a)
    solution_2 = (-b - cmath.sqrt(dis))/(2*a)

    #print output
    print("solutions are x = {0} and x = {1}".format(solution_1,solution_2))
