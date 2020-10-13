from googletrans import Translator

translator = Translator()
res_text = []
with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    for cur_line in f_obj:
        try:
            replace_part = cur_line.split(" - ")[0]
            result = translator.translate(replace_part, src='en', dest='ru')
            res_text.append(cur_line.replace(replace_part, result.text))
        except Exception as e:
            print("I can't translate this because: ", str(e))

with open("text_4_tr.txt", "w", encoding="utf-8") as f_obj:
    f_obj.writelines(res_text)
