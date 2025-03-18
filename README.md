# Personal Library Manager

## Overview
The **Personal Library Manager** is a Streamlit-based web application that allows users to manage their book collection. Users can add, remove, search, and view book details, along with statistics about their library. The application also supports file handling, allowing users to save and load their library from a file.

## Features
- **Add a Book**: Users can add books with details including title, author, publication year, genre, and read status.
- **Remove a Book**: Users can remove books by selecting from a list.
- **Search for a Book**: Search books by title or author.
- **Display All Books**: View all books in a formatted list.
- **Display Statistics**: View total books and percentage read.
- **Save Library**: Library data is saved to a `library.txt` file and loaded upon app start.

## Technologies Used
- Python
- Streamlit
- JSON (for file handling)

## Installation and Setup
### Prerequisites
Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/mahteck/personal-library-manager
   cd personal-library-manager
   ```
2. Install dependencies:
   ```sh
   pip install streamlit
   ```
3. Run the application:
   ```sh
   streamlit run library_manager.py
   ```

## File Handling
- **library.txt**: Stores book data in JSON format.
- The app loads the library data from this file when started and saves updates when exiting.

## Usage
1. Run the app and use the left sidebar to navigate.
2. Add, remove, search, or display books.
3. Save the library to persist data.

## Developer
**Developed by Shoaib**

## GitHub Repository
[GitHub Repository Link](https://github.com/mahteck/personal-library-manager)