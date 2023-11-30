import pyttsx3

if __name__ == '__main__':
    print("Welcome gunge!, jabaa?")
    while True:
        x = input("Say it again: ")
        
        if x=='q':
            break

    # Initialize the text-to-speech engine
        engine = pyttsx3.init()

    # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech

    # Say the input text
        engine.say(x)

    # Wait for the speech to finish
        engine.runAndWait()
