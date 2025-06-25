from pynput import keyboard
import time

name = input("what is the name of the person you want to tracK: ")
filename = name + ".txt"

# create empty file
with open(filename, 'w') as file:
    pass

print("created:", filename)

# tell the user to press space to start
print("Press left alt to start")

start = time.time()
count = 0

def on_release(key):
    global start 
    global count
    if key == keyboard.Key.alt_gr:
        print("ending " + str(count) + " Recordings.")
        listener.stop()
    elif key == keyboard.Key.space:
        count += 1
        end = time.time()
        duration = int(end - start)
        with open(filename, 'a') as file:
            file.write(str(duration) + "\n")
        start = end
        print("recorded", duration)
    elif key == keyboard.Key.alt_l:
        start = time.time()
        print("time started. press space to record")

listener = keyboard.Listener(on_release=on_release)
listener.start()
listener.join()