import time

class Timer():
    def __init__(self, duration):
        self.duration = duration
        self.sleep()

    def sleep(self):
        start_time = time.time()
        print(f"Sleeping for {self.duration} seconds...")
        time.sleep(self.duration/2)
        print("Halfway there!")

        elapsed_time = time.time() - start_time
        remaining_time = self.duration - elapsed_time
        if remaining_time > 0:
            remaining_time = round(remaining_time, 2)
        elif remaining_time < 0:
            remaining_time = 1
        else:
            remaining_time = 0
        print(f"Sleeping for {remaining_time} more seconds...")
        time.sleep(remaining_time)
        print("Done sleeping!")

