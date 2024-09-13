import time


def calculate_wpm(text_entered, start_time, end_time):
    words = len(text_entered.split())
    elapsed_time = end_time - start_time
    wpm = (words / elapsed_time) * 60
    return round(wpm, 2)


def calculate_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    matches = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    accuracy = (matches / max(len(original_words), 1)) * 100
    return round(accuracy, 2)
