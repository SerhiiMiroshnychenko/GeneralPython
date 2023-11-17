from deep_translator import GoogleTranslator

proxies_example = {
    "https": "34.195.196.27:8080",
    "http": "34.195.196.27:8080"
}
translated = GoogleTranslator(
    source='auto',
    target='de',
    proxies=proxies_example).translate("keep it up, you are awesome")

print(translated)
