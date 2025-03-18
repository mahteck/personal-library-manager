import streamlit as st
import json

# File to store library data
LIBRARY_FILE = "library.txt"

def load_library():
    """Load the library from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a book to the library."""
    with st.form("add_book_form"):
        title = st.text_input("Enter the book title:")
        author = st.text_input("Enter the author:")
        year = st.number_input("Enter the publication year:", min_value=1000, max_value=9999, step=1)
        genre = st.text_input("Enter the genre:")
        read_status = st.checkbox("Have you read this book?")
        submit = st.form_submit_button("Add Book")
    
    if submit and title and author:
        book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
        library.append(book)
        save_library(library)
        st.success("Book added successfully!")

def remove_book(library):
    """Remove a book by title."""
    titles = [book["title"] for book in library]
    if titles:
        title_to_remove = st.selectbox("Select a book to remove:", titles)
        if st.button("Remove Book"):
            library[:] = [book for book in library if book["title"] != title_to_remove]
            save_library(library)
            st.success("Book removed successfully!")
    else:
        st.warning("No books available to remove.")

def search_books(library):
    """Search for a book by title or author."""
    search_query = st.text_input("Enter title or author to search:")
    if st.button("Search"):
        matches = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if matches:
            for book in matches:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.warning("Your library is empty.")

def display_statistics(library):
    """Display total books and read percentage."""
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Percentage read:** {percentage_read:.2f}%")

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="Personal Library Manager", layout="wide")
    library = load_library()
    
    with st.sidebar:
        # st.title("Library Manager")
        st.sidebar.title("📚 Library Manager")
        menu_choice = st.radio("Select an option:", ["Add Book", "Remove Book", "Search Book", "Display Books", "Statistics", "Save Library"])
    
    st.header("Personal Library Manager")
    
    if menu_choice == "Add Book":
        add_book(library)
    elif menu_choice == "Remove Book":
        remove_book(library)
    elif menu_choice == "Search Book":
        search_books(library)
    elif menu_choice == "Display Books":
        display_books(library)
    elif menu_choice == "Statistics":
        display_statistics(library)
    elif menu_choice == "Save Library":
        save_library(library)
        st.success("Library saved successfully!")

    st.markdown("---")
    st.write("Developed by Shoaib")
        
if __name__ == "__main__":
    main()
