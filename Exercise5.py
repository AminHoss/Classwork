small_bottle = int(input("Number of small bottles: "))
large_bottle = int(input("Number of large bottles: "))
refund_small = small_bottle * 0.1
refund_large = large_bottle * 0.25
total_cost = refund_small + refund_large
print("The refund you get is ${:.2f}".format(total_cost))
