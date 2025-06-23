def count_words(text):
    """Counts the number of words in the given text."""
    if not text:
        return 0
    words = text.split()
    return len(words)