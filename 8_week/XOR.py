print(
    *map(
        lambda x: abs(x[0] - x[1]),
        zip(
            map(
                int,
                input().split()
            ),
            map(
                int,
                input().split()
            )
        )
    )
)
