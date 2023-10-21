washing_product = "shoes"
rinse = True
spin = True

washing_times = {
    "jacket": 40,
    "wash_underwear": 70,
    "shoes": 20
}

total = washing_times.get(washing_product, 0)
if rinse:
    total += 15

if spin:
    total += 9

print(f"Total washing time: {total} minutes")
