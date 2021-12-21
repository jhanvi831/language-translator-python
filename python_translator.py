from googletrans import Translator
translator = Translator()
out = translator.translate("नमस्ते", dest="en")
print(out.text)