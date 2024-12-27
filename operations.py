class CustomerOperations:
    def buy_book(self, book_name, original_price, bargain_price):
        if bargain_price >= original_price:
            return f"Book '{book_name}' purchased successfully for {bargain_price}!"
        return "Bargain rejected! Enter a higher amount."

    def sell_book(self, book_name, price, books):
        books[book_name] = price
        return f"Book '{book_name}' added to sell list for {price}!"

    def search_book(self, book_name, books):
        return book_name in books
