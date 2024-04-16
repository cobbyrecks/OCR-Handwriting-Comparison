# OCR Handwriting Comparison

This project allows users to compare handwritten text recognition performance between different OCR (Optical Character Recognition) algorithms. It supports Pytesseract and EasyOCR algorithms and provides options to compare either letters or words from two uploaded images.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Configuration](#configuration)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

The project aims to help users understand and compare the effectiveness of different OCR algorithms when it comes to recognizing handwritten text. By providing a user-friendly interface, users can easily upload images and compare the output of Pytesseract and EasyOCR algorithms side by side.

## Features

- Supports Pytesseract and EasyOCR algorithms for text recognition.
- Allows users to compare either letters or words from two uploaded images.
- Provides a simple and intuitive interface for users to upload images and view comparison results.

## Configuration

Install and configure Tesseract OCR based on your operating system.

For windows, installl the Tesseract executable file from [here](https://github.com/UB-Mannheim/tesseract/wiki)

## Installation

To run this project locally, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/cobbyrecks/ocr-handwriting-comparison.git
cd OCR-Handwriting-Comparison
````

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run streamlit_app.py
```

## Usage

1. Select the OCR Algorithm (Pytesseract or EasyOCR).
2. Choose the comparison mode (letters or words).
3. Upload two images containing handwritten text.
4. Click the button to create a juxtaposed collage for comparison.

Note: The two uploaded images should be of high quality and resolution to enable the OCR algorithm to detect the letters and words effectively.

## License
This project is licensed under the MIT License. See the LICENSE file for details.