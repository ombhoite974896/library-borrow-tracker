from collections import Counter
from statistics import mode, StatisticsError

# Sample data:

# Dictionary: member_id -> number of books borrowed
members_borrow_counts = {
    'member1': 3,
    'member2': 0,
    'member3': 5,
    'member4': 2,
    'member5': 0,
    'member6': 4,
    'member7': 3
}

# Dictionary: book_title -> total number of times borrowed
books_borrow_counts = {
    'Book A': 10,
    'Book B': 4,
    'Book C': 15,
    'Book D': 7,
    'Book E': 15,
    'Book F': 0
}

# 1. Compute the average number of books borrowed by all library members
def average_books_borrowed(members_borrow_counts):
    total_books = sum(members_borrow_counts.values())
    total_members = len(members_borrow_counts)
    average = total_books / total_members if total_members > 0 else 0
    return average

# 2. Find the book with the highest and lowest number of borrowings
def highest_and_lowest_borrowed_books(books_borrow_counts):
    if not books_borrow_counts:
        return None, None
    
    max_borrow = max(books_borrow_counts.values())
    min_borrow = min(books_borrow_counts.values())
    
    highest_books = [book for book, count in books_borrow_counts.items() if count == max_borrow]
    lowest_books = [book for book, count in books_borrow_counts.items() if count == min_borrow]
    
    return highest_books, lowest_books

# 3. Count the number of members who have not borrowed any books (borrow count = 0)
def count_non_borrowing_members(members_borrow_counts):
    count = sum(1 for count in members_borrow_counts.values() if count == 0)
    return count

# 4. Display the most frequently borrowed book (mode of borrow counts)
def most_frequently_borrowed_book(books_borrow_counts):
    # We find the book(s) with the highest frequency of borrow counts
    try:
        borrow_counts = list(books_borrow_counts.values())
        mode_borrow = mode(borrow_counts)
        most_frequent_books = [book for book, count in books_borrow_counts.items() if count == mode_borrow]
        return most_frequent_books, mode_borrow
    except StatisticsError:
        # If no unique mode (all different), return empty list or appropriate message
        return [], None

# --- Running the functions ---
avg_borrowed = average_books_borrowed(members_borrow_counts)
highest_books, lowest_books = highest_and_lowest_borrowed_books(books_borrow_counts)
non_borrowing_members = count_non_borrowing_members(members_borrow_counts)
most_frequent_books, freq_count = most_frequently_borrowed_book(books_borrow_counts)

print(f"Average number of books borrowed by members: {avg_borrowed:.2f}")
print(f"Book(s) with the highest borrowings ({books_borrow_counts[highest_books[0]]} times): {highest_books}")
print(f"Book(s) with the lowest borrowings ({books_borrow_counts[lowest_books[0]]} times): {lowest_books}")
print(f"Number of members who have not borrowed any books: {non_borrowing_members}")
if most_frequent_books:
    print(f"Most frequently borrowed book(s) (borrowed {freq_count} times): {most_frequent_books}")
else:
    print("No unique most frequently borrowed book (mode not found).")