def calculate_total_price(price, tax_rate=0.10):
    tax_amount = price * tax_rate
    total_price = price + tax_amount
    return total_price

price = 100  # 商品の金額
tax_rate = 0.10  # 消費税率（10%）
total = calculate_total_price(price, tax_rate)
print(f"消費税を含む合計金額: {total}円")
