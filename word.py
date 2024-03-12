import sys
import requests

def lookup_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        definitions = response.json()
        for entry in definitions:
            word = entry['word']
            print(f"Word: {word}")
            for meaning in entry['meanings']:
                part_of_speech = meaning['partOfSpeech']
                print(f"\n{part_of_speech}:")
                for definition in meaning['definitions']:
                    definition_text = definition['definition']
                    print(f"- {definition_text}")
                    if 'example' in definition:
                        example = definition['example']
                        print(f"  Example: {example}")
    else:
        print("Word not found or error in API request.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lookup_word(sys.argv[1])
    else:
        print("Usage: word <word_to_lookup>")
