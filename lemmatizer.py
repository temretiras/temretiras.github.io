import zeyrek

analyzer = zeyrek.MorphAnalyzer()


def lemmatize_words(file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()

        for word in words:
            analysis = analyzer.lemmatize(word)
            lemmas = [item[1] for item in analysis if item]
            lemma = lemmas[1] if lemmas else 'Not Found'
            output_file.write(f"{lemma}\n")
            print(f"Lemmatized: {lemma}")


input_file_path = 'C:/Users/avcbs/OneDrive - boun.edu.tr/Masaüstü/Kelimelik/tur_wikipedia_2021_10K-words.txt'
output_file_path = "C:/Users/avcbs/OneDrive - boun.edu.tr/Masaüstü/Kelimelik/lemmas.txt"
lemmatize_words(input_file_path, output_file_path)


with open("C:/Users/avcbs/OneDrive - boun.edu.tr/Masaüstü/Kelimelik/lemmas.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()


processed_lines = []
for line in lines:
    clean_line = line.strip()[1:-1]
    words = [word.strip().strip("'\"") for word in clean_line.split(',')]

    processed_line = '\n'.join(words)
    processed_lines.append(processed_line)


with open("C:/Users/avcbs/OneDrive - boun.edu.tr/Masaüstü/Kelimelik/processed_lemmas.csv", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(processed_lines))


print("Processing complete. The words have been separated and saved to 'processed_lemmas.csv'.")