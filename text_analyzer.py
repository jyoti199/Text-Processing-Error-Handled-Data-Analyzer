import os
import string

# --------- Read Input ----------
def read_text():
    while True:
        try:
            print("\n1. Enter text manually")
            print("2. Read from file (same folder)")
            print("3. Enter full file path (dynamic input)")
            
            choice = int(input("Choose option: "))
            
            # -------- Manual Input --------
            if choice == 1:
                return input("Enter your text: ")
            
            # -------- File in Same Folder --------
            elif choice == 2:
                while True:
                    filename = input("Enter file name (or 'exit' to go back): ").strip()
                    
                    if filename.lower() == "exit":
                        break
                    
                    if os.path.isfile(filename):
                        try:
                            with open(filename, 'r', encoding='utf-8') as file:
                                print("File loaded successfully ✅")
                                return file.read()
                        except Exception as e:
                            print("Error:", e)
                    else:
                        print("❌ File not found! Try again.")
            
            # -------- Dynamic File Path --------
            elif choice == 3:
                while True:
                    filepath = input("Enter full file path (or 'exit' to go back): ").strip().strip('"')
                    
                    if filepath.lower() == "exit":
                        break
                    
                    print("Checking path:", filepath)  # Debug line
                    
                    if os.path.isfile(filepath):
                        try:
                            with open(filepath, 'r', encoding='utf-8') as file:
                                print("File loaded successfully ✅")
                                return file.read()
                        except PermissionError:
                            print("❌ Permission denied!")
                        except Exception as e:
                            print("❌ Error:", e)
                    else:
                        print("❌ Invalid path or file not found! Try again.")
            
            else:
                print("Invalid choice! Select 1, 2, or 3.")
        
        except ValueError:
            print("❌ Enter a valid number!")


# --------- Process Text ----------
def process_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    duplicates = [w for w in freq if freq[w] > 1]
    palindromes = [w for w in words if w == w[::-1]]
    sorted_words = sorted(words)
    
    return words, freq, duplicates, palindromes, sorted_words


# --------- Features ----------
def display(freq, duplicates, palindromes, sorted_words):
    print("\n--- Word Frequency ---")
    for k, v in freq.items():
        print(k, ":", v)
    
    print("\nDuplicates:", duplicates if duplicates else "None")
    print("Palindromes:", palindromes if palindromes else "None")
    print("Sorted Words:", sorted_words)


def top_words(freq):
    print("\nTop 5 Frequent Words:")
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in sorted_freq[:5]:
        print(word, ":", count)


def search_word(freq):
    word = input("Enter word to search: ").lower()
    print(f"{word} occurs {freq.get(word, 0)} times")


def save_report(freq, duplicates, palindromes, sorted_words):
    try:
        with open("report.txt", "w", encoding='utf-8') as file:
            file.write("Word Frequency:\n")
            for k, v in freq.items():
                file.write(f"{k}:{v}\n")
            
            file.write("\nDuplicates:\n" + str(duplicates))
            file.write("\nPalindromes:\n" + str(palindromes))
            file.write("\nSorted Words:\n" + str(sorted_words))
        
        print("Report saved as report.txt ✅")
    
    except Exception as e:
        print("❌ Error saving file:", e)


# --------- Main Menu ----------
def main():
    text = read_text()
    
    if not text:
        print("No text found!")
        return
    
    words, freq, duplicates, palindromes, sorted_words = process_text(text)
    
    while True:
        print("\n--- MENU ---")
        print("1. Show Analysis")
        print("2. Top Frequent Words")
        print("3. Search Word")
        print("4. Save Report")
        print("5. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                display(freq, duplicates, palindromes, sorted_words)
            
            elif choice == 2:
                top_words(freq)
            
            elif choice == 3:
                search_word(freq)
            
            elif choice == 4:
                save_report(freq, duplicates, palindromes, sorted_words)
            
            elif choice == 5:
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice!")
        
        except ValueError:
            print("❌ Enter a valid number!")


# --------- Run Program ----------
main()