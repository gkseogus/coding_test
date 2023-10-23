def solution(order):
    price = 0
    
    for i in order:
        if i in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano"]:
            price += 4500
        elif i in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            price += 5000
        else:
            price += 4500
            
    return price