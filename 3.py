def process_text():
    text = "Представьте, что вы стоите на берегу озера, вдыхая прохладный воздух. Солнце только что поднялось над горизонтом, и вы видите, как оно отражается в воде. Вдалеке вы слышите пение птиц, и это успокаивает вас. Вы закрываете глаза и наслаждаетесь моментом."

    # Разбиваем текст на слова
    words = text.split()

    # Создаем словарь, где ключ - слово, значение - количество его вхождений в тексте
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    # Находим наиболее часто встречающееся слово
    most_common_word = max(word_counts, key=word_counts.get)
    print(f"Наиболее часто встречающееся слово: {most_common_word}")

    # Находим самое длинное слово
    longest_word = max(words, key=len)
    print(f"Самое длинное слово: {longest_word}")


if __name__ == '__main__':
    process_text()

