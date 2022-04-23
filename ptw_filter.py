def main():
    for symbol_count in range(3,6):
        original_file = r".\original-list.txt"
        new_file = rf".\word-with-{symbol_count}-symbols.txt"
        new_list = []
        with open(original_file, mode="r", encoding="utf-8") as words:
            for word in words:
                uppercase = [letter for letter in word if letter.isupper()]
                if int(symbol_count) == len(uppercase):
                    if len(new_list) > 1:
                        if word.lower() != new_list[-1].lower():
                            new_list.append(word)
                    else:
                        new_list.append(word)

        with open(new_file, mode="w", encoding="utf-8") as file:
            file.writelines(new_list)


if __name__ == "__main__":
    main()
