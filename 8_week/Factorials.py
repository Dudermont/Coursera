import math
print(
    *map(
        lambda x: math.factorial(x),
        list(
            range(
                int(input()) + 1
            )
        )
    )
)
