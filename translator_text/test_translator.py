from translator import TranslatorService

key = '51ef61e196ab420db9cf50004bcdde04'

t = TranslatorService(key)

result = t.translate('hello world', 'pt')
print(result)

result = t.detect("Let's try this")
print(result)

langs1 = t.getLanguagesForSpeak()
print(langs1)

langs2 = t.getLanguagesForTranslate()
print(langs2)

result = t.getLanguageNames(langs2,'en')
print(result)

l = []
l.append("Here's a sentence")
l.append("This thing really does work")

result = t.translateArray(l,'pt')
print(result)

l = []
l.append("Here's a sentence in english")
l.append("Aqui está uma frase em português")

result = t.detectArray(l)
print(result)

t.speak('This is the final test', 'en-us')
input('Wait until the sound plays and then press any key')

