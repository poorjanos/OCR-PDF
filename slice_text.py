import re
import os
from pathlib import Path

out_directory = Path(r"C:\Users\poorj\Projects\OCR-PDF\output")
sliced_directory = Path(r"C:\Users\poorj\Projects\OCR-PDF\output\sliced")
text_file = out_directory / Path("test.txt")


def count_sentences(text):
    sentence_endings = re.compile(r'[।|]')
    sentences = sentence_endings.split(text)
    return len([s for s in sentences if s.strip()])

def split_text_into_sentences(text):
    sentence_endings = re.compile(r'(?<=[।|]) +')
    sentences = sentence_endings.split(text)
    return [s.strip() for s in sentences if s.strip()]

def write_pieces(sentences, n, base_filename):
    sentences_per_file = len(sentences) // n
    extra_sentences = len(sentences) % n

    start = 0
    files = []
    for i in range(n):
        end = start + sentences_per_file + (1 if i < extra_sentences else 0)
        piece = " ".join(sentences[start:end])
        filename = f"{base_filename}_part_{i+1}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(piece)
        files.append(filename)
        start = end

    return files

def split_file(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = split_text_into_sentences(text)
    total_sentences = count_sentences(text)
    print(f"Total sentences: {total_sentences}")

    base_filename = os.path.splitext(filename)[0]
    return write_pieces(sentences, n, base_filename)

# Example usage
n = 3
split_file(text_file, n)