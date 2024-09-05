class Author:
    def __init__(self,name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    
    def __str__(self):
        if self.books:
            book_list = ','.join(self.books)
        else:
            book_list = 'No books'
        return f'Author: {self.name}. Books Published: {book_list}'


    
shakespeare = Author('William Shakespeare')
shakespeare.publish ('Hamlet')
shakespeare.publish ('Richard III') 

print(shakespeare)

