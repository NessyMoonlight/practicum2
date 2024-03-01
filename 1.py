total_summ = float(input())
silver_count = 96
golden_count = 96 / 16
silver_price = 48
silver_summ = 48 * silver_count
golden_summ = total_summ - silver_summ
golden_price = golden_summ / golden_count
print(round(golden_price))
