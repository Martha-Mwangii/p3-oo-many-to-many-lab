class Author:
    # Class variable to track all authors
    all_authors = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.name = name
        self._contracts = []  # Initialize the contracts list for the author
        Author.all_authors.append(self)
    
    def contracts(self):
        """Returns a list of contracts for this author."""
        return self._contracts
    
    def books(self):
        """Returns a list of books related to this author through contracts."""
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        """Creates and returns a new contract for the author and book."""
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        """Returns the total royalties the author earns from all contracts."""
        return sum(contract.royalties for contract in self._contracts)

class Book:
    # Class variable to track all books
    all_books = []
    
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        self.title = title
        self._contracts = []  # Initialize the contracts list for the book
        Book.all_books.append(self)
    
    def contracts(self):
        """Returns a list of contracts for this book."""
        return self._contracts
    
    def authors(self):
        """Returns a list of authors related to this book through contracts."""
        return [contract.author for contract in self._contracts]

class Contract:
    # Class variable to track all contracts
    all_contracts = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise TypeError("Date must be a string.")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        # Track the contract for the author and book
        Contract.all_contracts.append(self)
        author._contracts.append(self)
        book._contracts.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that have the same date, in the order they were created."""
        return [contract for contract in cls.all_contracts if contract.date == date]
    
    def __eq__(self, other):
        """Override equality check to compare the relevant attributes."""
        if isinstance(other, Contract):
            return (self.author == other.author and
                    self.book == other.book and
                    self.date == other.date and
                    self.royalties == other.royalties)
        return False



