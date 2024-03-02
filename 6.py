# 1f - 0.453592 kg
# 1d - 0.0254 m
# IMT - mass(kg) / height(m)^2
pounds = float(input("Введите вес в фунтах: "))
inchs = float(input("Введите высоту в дюймах: "))
pounds_kg = pounds * 0.453592
inchs_m = inchs * 0.0254

imt = pounds_kg / (inchs_m ** 2)
print(f"Индекс массы тела: {imt:.2f}")