# 🔓 PDF Password Remover - Online Tool

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An easy-to-use, free web tool to remove password protection and encryption from your PDF files directly in your browser. No software installation is required.

## ✨ Live Application

### **Access the tool here: [https://pdf-password-remover-dvae9gifwaonpbcqf2vyjd.streamlit.app/](https://pdf-password-remover-dvae9gifwaonpbcqf2vyjd.streamlit.app/)**

---

## 📄 About The Project

This project provides a simple and secure web application to unlock password-protected PDF files. If you have a PDF that requires a password to open, you can upload it here, provide the password, and download a new, unprotected version of the file.

The entire process is designed to be quick and intuitive. This tool is perfect for users who need to remove security from their PDFs for easier access, printing, or archiving.

This application was developed with the assistance of **Google's Gemini 1.5 Pro**, leveraging its capabilities for code generation, logic structuring, and content creation.

## ⭐ Key Features

*   **Remove PDF Passwords:** The core functionality to decrypt and remove user passwords from PDF files.
*   **Online & Free:** A completely free online PDF tool. No sign-up or payment is required.
*   **Secure & Private:** Files are processed in memory and are not stored on the server.
*   **User-Friendly Interface:** A clean, simple interface built with Streamlit for a smooth user experience.
*   **Multi-File Support:** Upload and process multiple PDF files in one session.
*   **Instant Downloads:** Download your unlocked PDF files directly from the browser.

## 🚀 How to Use the Online Tool

1.  **Navigate to the Web App:** Click on the live application link above.
2.  **Upload Your PDF(s):** Use the "Choose one or more PDF files" button to select the PDF file(s) you want to unlock.
3.  **Enter the Password:** If a file is encrypted, a password field will appear. Type the correct password for that file.
4.  **Download:** Once the correct password is provided, a "Download Unlocked PDF" button will appear. Click it to save your password-free file.

It's that simple!

## 🛠️ Technology Stack

This project is built entirely in Python and leverages the following powerful libraries:

*   **[Streamlit](https://streamlit.io/):** For creating and deploying the interactive web application.
*   **[pypdf](https://pypdf.readthedocs.io/):** For all backend PDF manipulation, including reading, decrypting, and writing PDF files.

## 🔍 Keywords for Search

This project is a solution for anyone searching for:
*   PDF password remover
*   Unlock PDF online
*   Free PDF unlocker
*   Remove PDF security
*   How to remove password from PDF
*   Decrypt PDF online free
*   Online PDF tool
*   Streamlit PDF application
*   Python PDF password remover
*   Get rid of PDF password

## 💻 Running a Local Instance (For Developers)

If you wish to run this application on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ImsMoon/Pdf-Password-Remover.git
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    Create a `requirements.txt` file with the following content:
    ```
    streamlit
    pypdf
    ```
    Then, run the installation command:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```
    The application will open in your default web browser.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
