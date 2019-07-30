import time
import timeit


@timeit.timeit
def foo() -> None:
    time.sleep(5)
    pass


@timeit.timeit
def boo() -> None:
    time.sleep(3)
    foo()
    foo()
    pass


@timeit.timeit
def zoo() -> None:
    boo()
    boo()
    pass


if __name__ == "__main__":
    # foo()
    time.sleep(10)
    zoo()
    pass
