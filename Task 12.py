
# Task 12

# Create class Product
######################
class Product: ####### Task 12.1 #######
    def __init__( self,product_id,price,prime_eligible,number_in_stock,date_added): 
        self.product_id = product_id                    ######## Task 12.2 ########
        self.price = price
        self.prime_eligible = prime_eligible
        self.number_in_stock = number_in_stock
        self.date_added = date_added
        
# Setter functions for each data field
    def set_product_id(self, value):
        self.product_id = value

    def set_price(self, value):
        self.price = value

    def set_prime_eligible(self, value):
        self.prime_eligible = value

    def set_number_in_stock(self, value):
        self.number_in_stock = value

    def set_date_added(self, value):
        self.date_added = value

# Getter functions for each data field
    def get_product_id(self):
        return self.product_id

    def get_price(self):
        return self.price
    
    def get_prime_eligible(self):
        return self.prime_eligible

    def get_number_in_stock(self):
        return self.number_in_stock

    def get_date_added(self):
        return self.date_added

# Print function for Product class
    def printProduct(self):
        print('Product ID: ', self.product_id)
        print('Price: £', self.price)
        print('Prime Eligible: ', self.prime_eligible)
        print('Number in Stock: ', self.number_in_stock)
        print('Date Added: ', self.date_added)

# Create class Book, which inherits from the Product
####################################################    
class Book(Product): ####### Task 12.3 ######        
    def __init__(self, product_id,price,prime_eligible,number_in_stock,  
                 date_added, title,author,num_pages,publisher,publication_date):
        super().__init__(product_id,price,prime_eligible,number_in_stock,date_added)
        self.title = title                              ######## Task 12.4 #########
        self.author = author
        self.num_pages = num_pages
        self.publisher = publisher
        self.publication_date = publication_date

# Setter functions for each data field
    def set_title(self, value):
        self.title = value

    def set_author(self, value):
        self.author = value

    def set_num_pages(self, value):
        self.num_pages = value

    def set_publisher(self, value):
        self.publisher = value

    def set_publication_date(self, value):
        self.publication_date = value

# Getter functions for each data field
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_num_pages(self):
        return self.num_pages

    def get_publisher(self):
        return self.publisher

    def get_publication_date(self, value):
        return self.publication_date

# Print function
    def printBook(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Pages: ', self.num_pages)
        print('Publisher: ', self.publisher)
        print('Publication Date: ', self.publication_date)

        self.printProduct()

######## Task 12.5 ########
book1 = Book(
    "B0031R5K6S",      # ID
    6.99,              # Price
    False,             # Prime
    21,                # Stock
    "5 May 2021",      # Date added
    "Brave New World", # Title
    "Aldous Huxley",   # Author
    288,               # Pages
    "Vintage Classics",# Publisher
    "6 Dec. 2007"      # Publication Date
    )
book1.printBook()

print(' ')

book2 = Book(
    "0008322066",      # ID
    2.25,              # Price
    True,              # Prime
    16,                # Stock
    "8 Jun. 2021",     # Date added
    "1984"           , # Title
    "George Orwell",   # Author
    384,               # Pages
    "William Collins", # Publisher
    "7 Jan. 2021"      # Publication Date
    )
book2.printBook()

print(' ')

book3 = Book(
    "0241956285",      # ID
    6.99,              # Price
    True,              # Prime
    14,                # Stock
    "20 Oct. 2019",    # Date added
    "The Big Sleep",   # Title
    "Raymond Chandler",# Author
    256,               # Pages
    "Penguin",         # Publisher
    "15 Jun. 2011"     # Publication Date
    )
book3.printBook()

print(' ')

# some setters and getters test with random info.

book1.set_price(5.22)
print('New price for book1: £', book1.get_price())

print(' ')

book2.set_title('Big Sleep')
print('New title for book2: ', book2.get_title())

print(' ')

book3.set_num_pages(300)
print('New number of pages for book3: ', book3.get_num_pages())
