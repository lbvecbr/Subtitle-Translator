from Functions.GoogleTranslate import google_translate
from Functions.WriteForAnyMemo import write

list_to_translate = ['hello', 'fuck off', 'get out']
list_to_translate, list_after_translate = google_translate(list_to_translate)
write(list_to_translate, list_after_translate)

