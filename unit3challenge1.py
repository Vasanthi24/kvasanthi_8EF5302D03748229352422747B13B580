def linear_search_product(products, target_product):
  indices = []

  for i, product in enumerate(products):
      if product == target_product:
          indices.append(i)

  return indices

# Example usage:
products_list = ["apple", "banana", "orange", "apple", "grape", "apple"]
target_product_name = "apple"
result = linear_search_product(products_list, target_product_name)

if result:
  print(f"The product '{target_product_name}' was found at indices: {result}")
else:
  print(f"The product '{target_product_name}' was not found in the list.")
