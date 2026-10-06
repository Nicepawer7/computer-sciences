PRICES_FILE = 'prices.dat'
CART_FILE = 'cart.dat'

def get_prices(file): #takes input file and gives back a dict item:price
    with open(file) as price:
        items = price.read().split('\n')
        item = dict()
        for couple_item in items:
            couple_item = couple_item.split(':') #list of shell and price
            item[couple_item[0]] = float(couple_item[1]) #convert to dict
        return item

def get_cart(file): #takes input file and gives back a dict item:amount
    with open(file) as cart:
        cart_dict = dict()
        for item in cart.read().split('\n'):
            try:
                cart_dict[item.strip()] += 1
            except KeyError:
                if item.strip() != '':
                    cart_dict[item.strip()] = 1
        return cart_dict


def get_offers(file):#takes filename and gives a tuple containing a dict (item:number) and the free item
    with open(file) as offers_list:
        offers_lines = offers_list.read().split('\n') #list of line-offers
        offers_list = (dict(),'')
        for offer in offers_lines:
            offers_list.append(offer.split(':'))

            

def compute_price(prices,cart):
    total = 0.0
    for item in cart:
        try:
            total += prices[item]*cart[item]
        except KeyError:
            print(item, 'unavailable')
    return round(total,2)


def main():
    prices = get_prices(PRICES_FILE)
    cart = get_cart(CART_FILE)
    print(prices)
    print(cart)
    print(compute_price(prices,cart),'€')  

if __name__ == '__main__': main()