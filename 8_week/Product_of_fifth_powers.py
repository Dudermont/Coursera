import functools

print(
    functools.reduce(
                    lambda x, y: x * y,
                    list(
                        map(
                            lambda x: x ** 5,
                            map(
                                int,
                                input().split())
                            )
                    )
    )
)
