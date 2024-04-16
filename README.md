# OCR Handwriting Comparison

This project allows users to compare handwritten text recognition performance between different OCR (Optical Character Recognition) algorithms. It supports Pytesseract and EasyOCR algorithms and provides options to compare either letters or words from two uploaded images.

## Table of Contents

- [Description](#description)
- [Features](#features)
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

### 1. Download Tesseract for Windows

Download the Tesseract OCR executable file for Windows from [here](https://github.com/UB-Mannheim/tesseract/wiki)

### 2. Set Tesseract Path in System Environmental Variables:

After installing Tesseract on Windows, you need to add its installation directory to the system environmental variables. This ensures that Tesseract can be accessed from any location in the command prompt.

#### Steps:

1. **Find Tesseract Installation Directory**: Locate the directory where Tesseract is installed on your system. By default, it's usually installed in `C:\Program Files\Tesseract-OCR`.

2. **Open System Properties**: Right-click on the "This PC" icon on your desktop or in File Explorer, then select "Properties". Alternatively, you can press `Windows key + Pause/Break` to open System Properties.

3. **Access Environmental Variables**: Click on "Advanced system settings" on the left sidebar. In the System Properties window, click on the "Environmental Variables..." button.

4. **Edit System Variables**: In the Environmental Variables window, under the "System variables" section, find the variable named `Path` and select it. Then click the "Edit..." button.

5. **Add Tesseract Path**: In the Edit Environment Variable window, click the "New" button and paste the path to the Tesseract installation directory. For example, `C:\Program Files\Tesseract-OCR`. Click "OK" to save the changes.

### 3. Set Tesseract Path Manually in Python:

In addition to setting the Tesseract path in the system environmental variables, you may need to specify the path manually in your Python scripts, especially if you're using virtual environments.

#### Example Python Code:

```python
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

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