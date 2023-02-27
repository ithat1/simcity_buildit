# simcity1.0
# Production times for simcity buildit
# Factory production times
factory_prod_items = ["Metal", "Wood",
                      "Plastic", "Seeds", "Minerals", "Chemicals"]  # Items produces in basic factory
factory_prod_time = [1, 3, 9, 20, 30, 120]
factory_prod_list = list(zip(factory_prod_items, factory_prod_time))
# print(factory_prod)
produce = input("Produce > ")
for product in factory_prod_list:
    if produce.lower() == product[0].lower():
        print(f"The time required to produce {product[0]} is {product[1]}m.")
