import wikipedia

text = input("text: ")

wikipedia.set_lang('uz')

response = wikipedia.page(text)

print(response)