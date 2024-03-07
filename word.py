import sys
import requests

def fetch_definitions(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return "Error Connecting: Please check your internet connection."
    except requests.exceptions.Timeout as errt:
        return "Timeout Error: The request timed out."
    except requests.exceptions.RequestException as err:
        return f"Unexpected Error: {err}"

def format_meanings(data):
    if isinstance(data, str):
        # Directly return the error message
        return data

    try:
        output = []
        for entry in data:
            meanings = entry.get('meanings', [])
            for meaning in meanings:
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                output.append(f"Part of Speech: {part_of_speech}")
                for definition in meaning.get('definitions', []):
                    def_text = definition.get('definition', '')
                    example = definition.get('example', '')
                    synonyms = ", ".join(definition.get('synonyms', []))
                    antonyms = ", ".join(definition.get('antonyms', []))

                    output.append(f"  Definition: {def_text}")
                    if example:
                        output.append(f"  Example:    {example}")
                    if synonyms:
                        output.append(f"  Synonyms:   {synonyms}")
                    if antonyms:
                        output.append(f"  Antonyms:   {antonyms}")
                output.append("")  # Add a newline for readability
        return "\n".join(output)
    except Exception as e:
        return f"Error processing the data: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: word <word_to_lookup>")
        sys.exit(1)

    word = sys.argv[1]
    data = fetch_definitions(word)
    output = format_meanings(data)
    print(output)

if __name__ == "__main__":
    main()
