# Eng-Mal Translator

The Eng-Mal Translator is a web application designed to translate text from English to Malayalam. The backend is powered by Flask, and the frontend is built using HTML, CSS, and Bootstrap. The translation is performed using a fine-tuned model pulled from Hugging Face.

## Overview

The Eng-Mal Translator leverages the power of state-of-the-art NLP models to provide accurate and efficient translations from English to Malayalam. This project utilizes a fine-tuned version of the `facebook/nllb-200-distilled-600M` model.

## Features

- Translate text from English to Malayalam
- User-friendly web interface
- Fast and accurate translations

## Installation

To get started with the Eng-Mal Translator, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/govardhan-06/Eng-Mal-Translator.git
   cd Eng-Mal-Translator
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**

   ```bash
   python application.py
   ```

5. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Enter the text you wish to translate in the input box.
2. Click the "Translate" button.
3. View the translated text in the output box.

## Model and Dataset

This project uses a fine-tuned version of the `facebook/nllb-200-distilled-600M` model. The model was fine-tuned on a custom dataset for better accuracy in translating English to Malayalam.

- **Fine-tuned model on Hugging Face:** [Link to Model](https://huggingface.co/Govardhan-06/nllb-200-distilled-600M)
- **Custom dataset used for fine-tuning:** [Link to Dataset](https://huggingface.co/datasets/Govardhan-06/flores_eng_mal)

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for providing the model and tools.
- Flask for the backend framework.
- Bootstrap for the frontend framework.
