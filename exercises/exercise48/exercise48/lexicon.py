def scan(words_to_scan):
    words = words_to_scan.split()
    word_pairs = []

    dictionary = {
        "north": "direction",
        "south": "direction",
        "east": "direction",
        "west": "direction",
        "go": "verb",
        "stop": "verb",
        "kill": "verb",
        "eat": "verb",
        "the": "stop",
        "in": "stop",
        "of": "stop",
        "from": "stop",
        "at": "stop",
        "it": "stop",
        "door": "noun",
        "bear": "noun",
        "princess": "noun",
        "cabinet": "noun",
    }

    for word in words:
        if word.isdigit():
            word_pairs.append(("number", word))

        else:
            word_pairs.append((dictionary.get(word.lower(), "error"), word))

    return word_pairs
