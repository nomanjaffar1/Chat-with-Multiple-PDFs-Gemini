# Chat-with-Multiple-PDFs-Gemini
## Overview

The **PDF Chat App with Gemini** is a Streamlit-based web application that allows users to interact with and query multiple PDF documents. By integrating Google Generative AI (Gemini) and FAISS (Facebook AI Similarity Search), this application provides advanced text analysis and question-answering capabilities. Users can upload PDF files, process their content, and ask questions related to the information within those documents.

## Features

- **PDF Upload:** Support for uploading multiple PDF files.
- **Text Extraction:** Extract text from the uploaded PDFs.
- **Text Chunking:** Split large texts into manageable chunks.
- **Vector Store:** Store and manage text embeddings using FAISS.
- **Question Answering:** Utilize Gemini AI to answer questions based on PDF content.
- **User Interface:** A simple and intuitive web interface built with Streamlit.

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **Virtual Environment (Recommended)**

### Setup Instructions

1. **Clone the Repository:**

   Open your terminal and clone the repository using the following command:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

   Navigate into the project directory:

   ```bash
   cd your-repo-name
   ```

2. **Create a Virtual Environment:**

   Create a virtual environment to manage your project dependencies:

   ```bash
   python -m venv env
   ```

   Activate the virtual environment:

   - On **Windows**:

     ```bash
     env\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies:**

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory of the project. Add your Google API key in the following format:

   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the Application:**

   Start the Streamlit application by running:

   ```bash
   streamlit run app.py
   ```

   Open your web browser and navigate to `http://localhost:8501` to access the application.

## Usage

1. **Upload PDF Files:**

   - On the sidebar, use the file uploader widget to select and upload your PDF files.
   - Click the "Submit & process" button to extract text from the uploaded PDFs and create text embeddings.

2. **Ask Questions:**

   - Enter your questions in the text input field on the main page.
   - Click the "Submit" button to receive answers based on the content of the PDFs.

## Code Structure

- **`app.py`**: The main application script where the Streamlit app logic is defined.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`.env`**: Contains environment variables, such as API keys.
- **`README.md`**: Documentation file for the project.

## Contributing

We welcome contributions to the project. To contribute:

1. **Fork the Repository:**

   Click the "Fork" button on the repository page to create a personal copy of the project.

2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Make Changes:**

   Implement your changes and commit them:

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to GitHub:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Create a Pull Request:**

   Go to the repository on GitHub and click "New Pull Request" to propose your changes.



---

Thank you for using the PDF Chat App with Gemini!

---

