
# import time

# from SOUND import listen
# from SOUND import speak
# from SOUND.wakeWordEngine import start_wakeword_detection
# from BRAIN.choise.choose import choise


# motherVariable = True

# try:

#     # Initialize audio output before Helen starts listening
#     speak.initialize_audio()

#     while motherVariable:

#         print("\nHelen is waiting for her wake word...")

#         heard = start_wakeword_detection()

#         if not heard:
#             continue

#         print("Helen activated!")

#         while motherVariable:

#             # 1. Listen and transcribe
#             start = time.perf_counter()

#             query = listen.listen()

#             print(
#                 "Listening + transcription:",
#                 round(time.perf_counter() - start, 2),
#                 "seconds"
#             )

#             if not query:
#                 print("Helen: I didn't catch that. Try again.")
#                 continue

#             print("Recognised text:", repr(query))

#             # 2. Check sleep command
#             if "go to sleep" in query.lower():
#                 speak.speak(
#                     "Going to sleep. Call me when you need me."
#                 )
#                 break

#             # 3. Select response
#             start = time.perf_counter()

#             answer = choise(query)

#             print(
#                 "Response selection:",
#                 round(time.perf_counter() - start, 2),
#                 "seconds"
#             )

#             if not answer:
#                 print("Helen: I couldn't generate a response.")
#                 continue

#             print("Helen's answer:", repr(answer))

#             # 4. Speak response
#             start = time.perf_counter()

#             speak.speak(str(answer))

#             print(
#                 "Speech playback:",
#                 round(time.perf_counter() - start, 2),
#                 "seconds"
#             )

# finally:

#     # Close audio resources safely
#     speak.shutdown()





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
from BRAIN.internet import Internet
Internet.search("who is mark zuck")