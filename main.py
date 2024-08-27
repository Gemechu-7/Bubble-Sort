basket =[
    {"fruit":"Bananas", "price":200},
    {"fruit":"Apples", "price":300},
    {"fruit":"Avocados", "price":250},
    {"fruit":"Oranges", "price":240},
    {"fruit":"Pineapples", "price":190}
]
#sort the basket list using keys(fruit and price)
def bubble_sort(basket, key=None):
    s=len(basket)#s=size
    for i in range(s-1):
        for j in range(s-1):
            if basket[j][key]>basket[j+1][key]:
                temporary_basket=basket[j]
                basket[j]=basket[j+1]
                basket[j + 1]=temporary_basket

    return basket
print(basket)
print(bubble_sort(basket, key="price"))