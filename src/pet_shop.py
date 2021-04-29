
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, transaction_amount):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + transaction_amount
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
    
def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop) + pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)    

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] = get_customer_cash(customer) - amount
    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return get_customer_cash(customer) >= pet["price"]
    
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop["pets"]:
        if customer_can_afford_pet(customer, pet):
            remove_customer_cash(customer, pet["price"])
            add_pet_to_customer(customer, pet)
            increase_pets_sold(pet_shop, 1)
            add_or_remove_cash(pet_shop, pet["price"])
    


    
