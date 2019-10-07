def solve(heads,legs):

    error_msg = "No solution"


    for chicken_count in range(heads+1):

        rabbit_count = heads - chicken_count
        if (2*chicken_count)+(4*rabbit_count) == legs:
            p = str(chicken_count) + " " + str(rabbit_count)

            return str(p)


    return error_msg

print(solve(35, 94))
