from kana_to_romaji import furigana_romaji_map
import pandas as pd


def furigana_to_romaji(furigana):
    romaji = ' '.join(furigana_romaji_map.get(char, char) for char in furigana)
    return romaji


df = pd.read_csv('japanese_words.csv')

df['Romaji'] = df['Furigana'].apply(furigana_to_romaji)

df.to_csv('japanese_words.csv', index=False)

print('Romaji column added and CSV file saved successfully.')
