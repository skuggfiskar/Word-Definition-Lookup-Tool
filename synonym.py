import sys
import requests

def lookup_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        definitions = response.json()
        print(f"Word: {word}")

        # count synonyms as a one liner
        all_synonyms = [synonym for entry in definitions for meaning in entry['meanings'] for synonym in meaning.get('synonyms', [])]

        if len(all_synonyms) == 0:
            print("No synonyms found.")
            return

        for entry in definitions:
            for meaning in entry['meanings']:
                part_of_speech = meaning['partOfSpeech']
                synonyms_set = set()  # Use a set to avoid duplicate synonyms

                synonyms = meaning.get('synonyms', [])
                synonyms_set.update(synonyms)  # Add synonyms to the set

                # Only print the part_of_speech and synonyms if there are synonyms
                if synonyms_set:
                    print(f"\n{part_of_speech}:")
                    print(", ".join(synonyms_set))
    else:
        print("Word not found or error in API request.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lookup_word(sys.argv[1])
    else:
        print("Usage: synonym.py <word_to_lookup>")
