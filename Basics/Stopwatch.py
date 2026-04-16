import time


def stopwatch():
    input("Please press ENTER to START :- ")
    start_time = time.time()
    input("Press ENTER to Stop :- ")
    end_time = time.time()

    duration = (end_time - start_time)

    print("The time you entered is :- ", duration)

stopwatch()
