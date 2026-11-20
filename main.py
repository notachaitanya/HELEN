
from SOUND import listen
from SOUND import speak
from SOUND.wakeWordEngine import start_wakeword_detection
from BRAIN import Choise


motherVariable = True

try:
    speak.initialize_audio()

    while motherVariable:

        print("\nWaiting for wake word...")
        heard = start_wakeword_detection()

        if not heard:
            continue

        print("WAKE WORD DETECTED!")
        
        while motherVariable:

            print("\nCALLING LISTEN...")

            query = listen.listen()

            print("LISTEN RETURNED:", repr(query))
            print("RETURN TYPE:", type(query))

            if not isinstance(query, str) or not query.strip():
                print("No valid speech detected. Listening again...")
                continue

            print("RECOGNIZED SPEECH:", query)

            # Completely terminate Helen
            if "helen exit" in query.lower():
                speak.speak("Shutting down. Goodbye.")
                motherVariable = False
                break

            # Put Helen to sleep
            if "go to sleep" in query.lower():
                speak.speak("Going to sleep. Call me when you need me.")
                break

            print("SENDING QUERY TO CHOICE...")

            answer = Choise.choise(query)

            print("CHOICE RETURNED:", repr(answer))

            if not answer:
                continue

            speak.speak(str(answer))

finally:
    speak.shutdown()
