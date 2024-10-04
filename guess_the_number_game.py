import sys
import random

MAX_ATTEMPT = 10

sys.stdout.buffer.write(b"Enter the min number n: ")
sys.stdout.flush()
n = int(sys.stdin.buffer.readline())

sys.stdout.buffer.write(b"Enter the max number m: ")
sys.stdout.flush()
m = int(sys.stdin.buffer.readline())

random_number = random.randint(n, m)


sys.stdout.buffer.write(f"You can try {MAX_ATTEMPT} times.\n".encode("UTF-8"))
sys.stdout.flush()

for i in range(MAX_ATTEMPT):
    sys.stdout.buffer.write(f"This is {i+1} attempt\n".encode("UTF-8"))
    sys.stdout.flush()

    sys.stdout.buffer.write(b"Enter the number: ")
    sys.stdout.flush()
    guess_number = int(sys.stdin.buffer.readline())
    if guess_number == random_number:
        sys.stdout.buffer.write(b"You win!\n")
        sys.stdout.flush()
        break

    sys.stdout.buffer.write(b"You lose\n")
    sys.stdout.flush()
