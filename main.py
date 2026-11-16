
from SOUND import listen
from SOUND import speak
from SOUND.wakeWordEngine import start_wakeword_detection
from BRAIN.choise.choose import choise


motherVariable = True

try:
    speak.initialize_audio()

    while motherVariable:

        heard = start_wakeword_detection()

        if not heard:
            continue

        while motherVariable:

            query = listen.listen()

            if not query:
                continue

            # Completely terminate Helen
            if "helen exit" in query.lower():
                speak.speak("Shutting down. Goodbye.")
                motherVariable = False
                break

            # Put Helen to sleep
            if "go to sleep" in query.lower():
                speak.speak("Going to sleep. Call me when you need me.")
                break

            answer = choise(query)

            if not answer:
                continue

            speak.speak(str(answer))

finally:
    speak.shutdown()






# ------------------------------------------------reel main----------------------------------------------------
# import time

# from SOUND import listen
# from SOUND import speak
# from SOUND.wakeWordEngine import start_wakeword_detection
# from BRAIN.choise.choose import choise


# motherVariable = True

# try:

#     speak.initialize_audio()

#     while motherVariable:

#         print("\nHelen is waiting for her wake word...")

#         heard = start_wakeword_detection()

#         if not heard:
#             continue

#         print("Helen activated!")

#         # Start from the first dialogue every time
#         dialogue_index = 0

#         while motherVariable:

#             if dialogue_index >= 12:
#                 print("Helen's dialogue is complete.")
#                 break

#             # Wait until you finish speaking
#             listen.listen()

#             # Get Helen's next scripted response
#             answer = choise(dialogue_index)

#             if answer is None:
#                 break

#             print("\nHelen:", answer)

#             # Speak immediately after silence is detected
#             speak.speak(answer)

#             dialogue_index += 1

#         print("\nReturning to standby...")

# finally:

#     speak.shutdown()
# ------------------------------------------------reel main----------------------------------------------------
