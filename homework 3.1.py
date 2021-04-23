#Task3.1 
#VitalyPerepelko    

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)

print(num_translate('seven'))



#Task3.2
eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].capitalize()
    else:
        return eng_rus_dict[eng_word]


print(num_translate_adv('seven'))
print(num_translate_adv('Seven'))
