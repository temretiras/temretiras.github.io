import numpy as np
import pandas as pd
import re



# Reading the CSV file into a DataFrame
df = pd.read_csv('C:/Users/avcbs/OneDrive - boun.edu.tr/Masaüstü/Kelimelik/processed_lemmas.csv')
df.columns = ['lemmas']

# Removing non-string entries from the DataFrame
df = df[[False if type(i) != type('a') else True for i in df['lemmas']]]

# Removing entries that contain numbers
df = df[[False if re.match('^.*[0-9]+.*', i) else True for i in df['lemmas']]]

# Converting all entries to lowercase
df['lemmas'] = df['lemmas'].apply(lambda x: x.lower())

# Removing duplicate entries
df.drop_duplicates(inplace=True)

# Removing entries with non-Turkish characters and symbols
df = df[[True if re.match('^[a-zçğıöşü]+', i) else False for i in df['lemmas']]]
df = df[[False if re.match('^.*[qwx]', i) else True for i in df['lemmas']]]


# Removing entries with non-letter characters
df = df[[False if re.match('^.*[-̇]', i) else True for i in df['lemmas']]]
df = df[[False if re.match('^.*[\.³²âãōîéáôôïšʿćàèåúíøóûñčêäæđķ~äæđūßëłńýорэ′/дžėșð]', i) else True for i in df['lemmas']]]

def sort_lemma_list(processed_lemmas, length):
    """
    Sorts the lemmas based on their lengths.

    Parameters:
    processed_lemmas (DataFrame): DataFrame containing processed lemmas.
    length (int): Desired length of lemmas.

    Returns:
    DataFrame: DataFrame containing lemmas of the specified length.
    """
    return pd.DataFrame([i for i in processed_lemmas['lemmas'] if len(i) == length])

# Sorting lemmas by their lengths
lemma_list_2 = sort_lemma_list(df, 2)
lemma_list_3 = sort_lemma_list(df, 3)
lemma_list_4 = sort_lemma_list(df, 4)
lemma_list_5 = sort_lemma_list(df, 5)
lemma_list_6 = sort_lemma_list(df, 6)
lemma_list_7 = sort_lemma_list(df, 7)
lemma_list_8 = sort_lemma_list(df, 8)
lemma_list_9 = sort_lemma_list(df, 9)
lemma_list_10 = sort_lemma_list(df, 10)


def get_alphabet():
    vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    consonants = ['b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
    return np.array(consonants), np.array(vowels)


def random_letters(consonants, vowels):
    vowel_indexes = np.random.randint(0, 8, size=3)
    cons_indexes = np.random.randint(0, 21, size=4) 
    return np.concatenate([vowels[vowel_indexes], consonants[cons_indexes]])


class player:
    def __init__(self, consonants, vowels):
        self.points = 0
        self.inventory = random_letters(consonants, vowels)


    def ask_name(self):
        self.name = input('İsminizi söyleyin: ')
        return self.name
    

    def ask_word(self):
        print(f"{self.name} envanter: {self.inventory}")
        self.word = input(f'Bir kelime söyle {self.name}: ')
        return self.word
    

    def change_inventory(self, word, consonants, vowels):
        self.inventory = self.inventory.tolist()
        for char in word:
            if char in self.inventory:
                self.inventory.remove(char)
                if char in consonants:
                    index = np.random.randint(0, 21) 
                    self.inventory.append(consonants[index])
                else:
                    index = np.random.randint(0, 8)
                    self.inventory.append(vowels[index])
        self.inventory = np.array(self.inventory)
        return self.inventory


    def inv_checker(self):
        for char in self.word:
            if char not in self.inventory:
                print('Hata: Kelimenizde envanterde olmayan harf/harfler var')
                return self.ask_word()


    def get_lemma_list(self, lemma_list):
        length = str(len(self.word))
        dictionary = lemma_list[length]
        return dictionary


    def word_checker(self, lemma_list, word, consonants, vowels):
        if self.word not in lemma_list:
            pass_turn = input("Yanlış kelime, lütfen yeni bir kelime seçin ya da envanter değiştirmek için p'ye basın: ")
            if pass_turn == 'p':
                self.change_inventory(word, consonants, vowels)
            return self.ask_word()
        


                

def create_table():
    difficulty = input('Oyun zorluğu nasıl olsun? kolay/zor: ')
    if difficulty == 'kolay':
        table = pd.DataFrame([[''] * 6] * 6)
        return table
    elif difficulty == 'zor':
        table = pd.DataFrame([[''] * 10] * 10)
        return table
    else:
        print('Lütfen uygun bir zorluk seviyesi seçin :(')
        return create_table()



def place_word(word, table):
    print('Kelimeyi nereye koymak istersiniz?')
    row = int(input('Satır: '))
    column = int(input('Sütun: '))
    axis = input('Kelimeyi yatay mı yoksa düşey mi yerleştireceksiniz? x/y  ')
    counter = 0

    for char in word:
        if axis == 'y':
            table.iloc[row+counter, column] = char
            counter += 1
        if axis == 'x':
            table.iloc[row, column+counter] = char
            counter += 1 


def main():
    dictionary = {'2': lemma_list_2,
                  '3': lemma_list_3,
                  '4': lemma_list_4,
                  '5': lemma_list_5,
                  '6': lemma_list_6,
                  '7': lemma_list_7,
                  '8': lemma_list_8,
                  '9': lemma_list_9,
                  '10': lemma_list_10}
    

    print('=' * 100)
    print('!!!KELİMELİĞE HOŞGELDİNİZ!!!')
    print('=' * 100)

    consonants, vowels = get_alphabet()
    table = create_table()
    print(table)

    player1 = player(consonants, vowels)
    print('Oyuncu 1')
    player1.ask_name()

    player2 = player(consonants, vowels)
    print('Oyuncu 2')
    player2.ask_name()

    round_count = 1
    start = input('Başlamak için herhangi bir tuşa basın: ')
    while start != 'q':
        print(f'{round_count}. tur')


        player1.ask_word()
        player1.inv_checker()
        dictionary1 = player1.get_lemma_list(dictionary)
        player1.word_checker(dictionary1, player1.word, consonants, vowels)
        place_word(player1.word, table)  
        player1.change_inventory(player1.word, consonants, vowels)
        print(table)


        player2.ask_word()
        player2.inv_checker()
        dictionary2 = player2.get_lemma_list(dictionary)
        player2.word_checker(dictionary2, player2.word, consonants, vowels)
        place_word(player2.word, table)
        player2.change_inventory(player2.word, consonants, vowels)
        print(table)

        start = input("Çıkmak için q, sonraki tur için başka herhangi bir tuşa basın: ")

main()

# üst üste kelime yazılabiliyor
# herhangi bir kelimeye temas eden başka bir kelime yazılabiliyor, bu durumda anlamsız kelimeler olabiliyor
# anlamsız kelimeler yazılabiliyor (corpus gelince çözülecek)
# corpusta olmayan kelimeler için fst
# index hatası yapılabiliyor (tahtanın dışına taşmak)
# kelimelerin puanları yok (puanlar neye göre mesela ?) (daha yaygın harflere daha az puan vs.) --> bu nasıl olur?
# envanterde 3 sesli 4 sessiz harf var kelime bulunabilsin diye. Bu gerçekte nasıl? 
# bir şekilde ipucu veren bir şey olsa fena olmaz

