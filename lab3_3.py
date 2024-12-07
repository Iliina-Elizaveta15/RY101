def count_letters(text):
    letter_count_dict = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count_dict:
                letter_count_dict[char] += 1
            else:
                letter_count_dict[char] = 1

    return letter_count_dict


def calculate_frequency(count_dict):
    total = sum(count_dict.values())
    frequency_dict = {}

    for letter, count in count_dict.items():
        frequency_dict[letter] = round(count / total, 2)

    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


letter_count = count_letters(main_str)


frequency = calculate_frequency(letter_count)


for freq_letter, freq in sorted(frequency.items()):
    print(f"{freq_letter}: {freq:.2f}")