command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("hey, car already started ")
        else:
            started = True
            print("car started....")
    elif command == "stop":
        if not started:
            print("Hey, car is stopped")
        else:
            started = False
            print("car stopped.")
    elif command ==  "help":
        print("""
start - to start car
stop - to stop car
quit - to quit game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand")
