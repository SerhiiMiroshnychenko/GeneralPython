# pip install -U deep-translator

from deep_translator import GoogleTranslator


# Use any translator you like, in this example GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")
print(translated)
# output -> Weiter so, du bist großartig
