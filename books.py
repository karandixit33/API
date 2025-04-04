from flask import Flask , jsonify, request

app = Flask(__name__)



books = [
  
    {"id": 1 , "title":"kabir ke pohe", "Author": "KARAN JI" },
    {"id": 2 , "title":"poor boy poor day", "Author": "VIVEK JI" },
    {"id": 3 , "title":"gillu", "Author": "ROHAN JI" }
    
]

#get all books
@app.route('/books', methods=['GET'])
def get_books():
    return books

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book
        
    return {'error':'book not found'}

#create a book
    
@app.route('/books', methods=['POST'])
def create_book():
    new_book={'id':len(books)+1,'title':request.json['title'], 'author': request.json['author']}
    books.append(new_book)
    return new_book

#update a book

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title'] 
            book['author']=request.json['author'] 
            return book
        return{'error': 'book not found'} 
    
    
    
if __name__=='__main__':
    app.run(debug=True)
