from typing import List

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.books_borrowed = {}
        self.book_reservation = []
        self.book_history = {}
        
    def add_book(self, book_id: str, title: str) -> bool:
        if book_id in self.books:
            return False
        self.books[book_id] = title
        self.books_borrowed[book_id] = False
        self.book_history[book_id] = []
        return True
    
    def list_books(self) -> List[str]:
        available_books = []
        for i,v in zip(self.books_borrowed.items(), self.books.items()):
            if i[1] == False:
                available_books.append(v[1])
        print(available_books)
        return available_books

    def print_book_history(self) -> List[str]:
        for k, v in self.book_history.items():
            if k in self.books:
                print(f"Book: {self.books[k]}  History: {v}")
                
    
    def borrow_books(self, book_id: str) -> bool:
        if book_id not in self.books or self.books_borrowed.get(book_id)== True:
            return False
        self.books_borrowed[book_id] = True
        self.book_history[book_id].append("Borrowed")
        return True

    def return_book(self, book_id: str) -> bool:
        if book_id in self.books and self.books_borrowed.get(book_id) == True:
            self.books_borrowed[book_id] = False
            self.book_history[book_id].append("Returned")
            return True
        return False
    
    def reserve_book(self, book_id: str) -> bool:
        if book_id not in self.books or book_id in self.book_reservation or self.books_borrowed.get(book_id) == False:
                return False
        self.book_reservation.append(book_id)
        self.book_history[book_id].append("Reserved")
        return True
    
    
        



result = LibrarySystem()
result.add_book("1", "HarryPotter 1")
result.add_book("2", "HarryPotter 2")
result.add_book("3", "HarryPotter 3")
result.add_book("4", "HarryPotter 4")
result.borrow_books("1")
result.borrow_books("2")
result.return_book("2")
result.borrow_books("2")
result.reserve_book("2")
result.list_books()
result.print_book_history()