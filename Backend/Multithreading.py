import threading
import time

def walk_dog():
    time.sleep(8)
    print("Take out talk")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("getting mail")

def main():

    chore1 = threading.Thread(target=walk_dog)
    chore1.start()

    chore2 = threading.Thread(target=take_out_trash)
    chore2.start()

    chore3 = threading.Thread(target=get_mail)
    chore3.start()

if __name__ == '__main__':
    main()