# Text Reader & Analyzer
# A beginner-friendly project for Learning file handling in python

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def count_text(content):
    '''Count lines, words, and characters'''
    lines=content.splitlines()
    words=content.split()
    chars=len(content)
    return len(lines), len(words), chars

def search_word(content, word):
    '''Search words in content and return lines containing it'''
    lines = content.splitlines()
    results = [line for line in lines if word.lower() in line.lower()]
    return results

def save_report(filename, lines, words, chars):
    '''Save report to file'''
    with open('report.txt', 'w', encoding='utf-8') as report:
        report.write("📊 Text Analysis Report\n")
        report.write("======================\n")
        report.write(f"File: {filename}\n")
        report.write(f"Lines: {lines}\n")
        report.write(f"Words: {words}\n")
        report.write(f"Characters: {chars}\n")
    print("✅ Report saved as report.txt")


def main():
    filename ='sample.txt'
    try:
        content = read_file(filename)
    except FileNotFoundError:
        print("❌ File not found. Make sure sample.txt is in the same folder.")
        return

    while True:
        print("\n📖 Text Reader & Analyzer")
        print("1️⃣ Show full text")
        print("2️⃣ Count lines, words, characters")
        print("3️⃣ Search for a word")
        print("4️⃣ Save a report")
        print("0️⃣ Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            print("\n--- File Content ---")
            print(content)

        elif choice == "2":
            lines, words, chars = count_text(content)
            print("\n📊 Text Summary:")
            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {chars}")

        elif choice == "3":
            word = input("Enter a word to search: ").strip()
            found = search_word(content, word)
            if found:
                print(f"\n🔍 Lines containing '{word}':")
                for line in found:
                    print(" -", line)
            else:
                print(f"❌ Word '{word}' not found.")

        elif choice == "4":
            lines, words, chars = count_text(content)
            save_report(filename, lines, words, chars)

        elif choice == "0":
            print("👋 Goodbye! Keep learning!")
            break

        else:
            print("⚠️ Invalid choice. Try again!")

if __name__ == "__main__":
    main()




