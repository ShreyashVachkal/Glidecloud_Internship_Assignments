def chunk_text(text: str):
    sentences = text.split(". ")
    chunks = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunks.append(sentence)

    return chunks
