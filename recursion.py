

def countdown(i):
    print(i)
    if i == 0:
        # Base case
        return
    else:
        # Recursive case
        countdown(i - 1)


if __name__ == "__main__":
    i = 20
    countdown(i)
