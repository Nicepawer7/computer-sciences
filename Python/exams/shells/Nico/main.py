    prices_file = 'prices.dat'
    cart_file = 'cart.dat'

    def get_prices(file): #takes input file and gives back a dict item:price
        with open(file) as price:
            items = price.read().split('\n')
            item = dict()
            for couple_item in items:
                couple_item = couple_item.split(':') #list of shell and price
                item[couple_item[0]] = float(couple_item[1]) #convert to dict
            return item

    def get_cart(file):
        with open(file) as cart:
            return cart.read().split('\n')


    def compute_price(prices,cart):
        total = 0.0
        for item in cart:
            try:
                total += prices[item]
            except KeyError:
                print(item, 'unavailable')
        return round(total,2)


    def main():
        prices = get_prices(prices_file)
        cart = get_cart(cart_file)
        print(prices)
        print(cart)
        print(compute_price(prices,cart),'€')  

    if __name__ == '__main__': main()