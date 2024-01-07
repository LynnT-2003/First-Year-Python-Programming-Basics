gas = input("Enter a remaining gas (litre): ")
rate = input("Enter a consumption rate (km/litre): ")
distance = input("nter a traveling distance:  ")


req_gas = float(distance) / float(rate)

need_gas = float(req_gas) - float(gas)
extra_gas = float(gas) - float(req_gas)

if float(gas) >= float(req_gas):
    print("You can reach a destination and you still have " + str(extra_gas) + " litre(s) in the tank")
else:
    print("You need " + str(need_gas) + " more litre(s) to reach your destination")






