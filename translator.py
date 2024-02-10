def translator_with_google ():

    from googletrans import Translator

    # Create a translator object
    translator = Translator()

    # English text to be translated
    # input_text = "Hello, how are you?"
    input_text = "Comment Ca Va ?"

    # Detect the language of the text
    detected_lang = translator.detect(input_text).lang

    print(f"detected_lang is {detected_lang}")

    # Translate the text to Arabic
    if detected_lang != 'ar':
        arabic_translation = translator.translate(input_text, src=detected_lang, dest='ar').text
        print("Input text:", input_text)
        print("Arabic:", arabic_translation)
    else:
        print("The text is already in Arabic.")

def translator_with_nltk ():
    import nltk
    from nltk.tokenize import word_tokenize
    from googletrans import Translator

    nltk.download('punkt')

    # Sample English text
    # english_text = "Hello, how are you?"
    english_text = "Comment Ca Va ?"

    # Tokenize the text
    tokens = word_tokenize(english_text)

    print(f"Tokens are {tokens}")

    # Combine the tokens into a single string
    english_text_combined = ' '.join(tokens)

    # Initialize Translator
    translator = Translator()

    # Translate the text to Arabic
    translation = translator.translate(english_text_combined, dest='ar')

    print("English:", english_text)
    print("Arabic:", translation.text)


translator_with_google()
translator_with_nltk()