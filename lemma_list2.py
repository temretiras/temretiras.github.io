import pandas as pd
import numpy as np
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

print(lemma_list_10)

def get_alphabet():
    """
    Returns the Turkish alphabet sorted in a specific order.

    Returns:
    list: List containing Turkish vowels and consonants.
    """
    vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    consonants = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
    return sorted(vowels + consonants)

alphabet = get_alphabet()

def create_matrix(lemma_list, alphabet):
    """
    Creates a DataFrame matrix with lemmas as rows and alphabet letters as columns.

    Parameters:
    lemma_list (DataFrame): DataFrame containing lemmas.
    alphabet (list): List of alphabet letters.

    Returns:
    DataFrame: DataFrame matrix with NaN values initialized.
    """
    matrix = pd.DataFrame(data=np.empty((len(lemma_list), 29)), columns=alphabet, index=lemma_list.iloc[:, 0])
    matrix[:] = np.nan
    return matrix

# Creating matrices for lemmas of different lengths
matrix_of_2 = create_matrix(lemma_list_2, alphabet)
matrix_of_3 = create_matrix(lemma_list_3, alphabet)
matrix_of_4 = create_matrix(lemma_list_4, alphabet)
matrix_of_5 = create_matrix(lemma_list_5, alphabet)
matrix_of_6 = create_matrix(lemma_list_6, alphabet)
matrix_of_7 = create_matrix(lemma_list_7, alphabet)
matrix_of_8 = create_matrix(lemma_list_8, alphabet)
matrix_of_9 = create_matrix(lemma_list_9, alphabet)
matrix_of_10 = create_matrix(lemma_list_10, alphabet)

print(matrix_of_2)
print(matrix_of_3)
print(matrix_of_4)
print(matrix_of_5)
print(matrix_of_6)
print(matrix_of_7)
print(matrix_of_8)
print(matrix_of_9)
print(matrix_of_10)

def fill_matrix(matrix):
    """
    Fills the matrix with the index positions of each character in the lemmas.

    Parameters:
    matrix (DataFrame): DataFrame matrix to be filled.

    Returns:
    DataFrame: Filled DataFrame matrix.
    """
    words = matrix.index
    for word in words:
        for i in range(0, len(word)):
            char = word[i]
            if matrix.loc[word, char] == np.nan:
                print('a')
                matrix.loc[word, char] = i
            elif matrix.loc[word, char] != np.nan:
                print('b')
                char2 = char + '2'
                matrix.loc[word, char2] = i
            else:
                print('c')
                char3 = char + '3'
                matrix.loc[word, char3] = i         
    return matrix

# Filling the matrices with index positions of characters in lemmas
#matrix_of_2 = fill_matrix(matrix_of_2)
#matrix_of_3 = fill_matrix(matrix_of_3)
#matrix_of_4 = fill_matrix(matrix_of_4)
#matrix_of_5 = fill_matrix(matrix_of_5)
#matrix_of_6 = fill_matrix(matrix_of_6)
#matrix_of_7 = fill_matrix(matrix_of_7)
#matrix_of_8 = fill_matrix(matrix_of_8)
#matrix_of_9 = fill_matrix(matrix_of_9)
matrix_of_10 = fill_matrix(matrix_of_10)

# Printing the filled matrices
#print(matrix_of_2)
#print(matrix_of_3)
#print(matrix_of_4)
#print(matrix_of_5)
#print(matrix_of_6)
#print(matrix_of_7)
#print(matrix_of_8)
#print(matrix_of_9)
print(matrix_of_10)