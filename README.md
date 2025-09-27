# NATO Phonetic Alphabet Converter

## Description

This Python project demonstrates how to convert words into their corresponding NATO phonetic alphabet code words. It uses a CSV file as a data source, leverages Pandas for data manipulation, and includes examples of working with dictionaries and data frames. The project is ideal for beginners who want to learn about Python data structures, file I/O, and basic user interaction.

## Features

- Reads the NATO phonetic alphabet from a CSV file
- Builds a dictionary to map letters to their code words
- Converts any user-input word to a list of phonetic code words
- Demonstrates data manipulation with both dictionaries and pandas DataFrames

## Files

- `main.py`: Contains examples of dictionary and DataFrame looping, as well as TODOs to implement the phonetic converter.
- `Nato.py`: Complete script for converting input words to NATO phonetic code words using the CSV data.
- `nato_phonetic_alphabet.csv`: Data source for the NATO phonetic alphabet.

## Getting Started

### Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)

### Usage

1. Clone or download the repository.
2. Make sure `nato_phonetic_alphabet.csv` is in the same directory as the Python scripts.
3. Run `Nato.py`:
   ```bash
   python Nato.py
   ```
4. Enter any word when prompted; the program will output the corresponding NATO phonetic code words.

### Example

```
enter word: Hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## License

This project is open source and available under the MIT License.
