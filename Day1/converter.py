exchange_rate = {
    ('USD', 'EUR'): 0.92,
    ('USD', 'BRL'): 6.27,
    ('USD', 'AOA'): 825,
    ('EUR', 'USD'): 1.09,
}

def converter(source_currency, target_currency, value):
    coins = (source_currency, target_currency)

    if coins in exchange_rate:
        return value*exchange_rate[coins]
    else:
        raise ValueError('Invalid coins!')
        
while True:
    print("Welcome to Converte Pro")
    print("Available Exchanges: ", [f"{key[0]} to {key[1]}" for key in exchange_rate.keys()])
    
    source_currency = input("From: ").upper()
    target_currency = input("To: ").upper()
    value = float(input("Amount to Exchange: "))
    converter_app = converter(source_currency, target_currency, value)
    print(f'The value converter is: {converter_app:.2f}')
        