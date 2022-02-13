def inventoryAllocator(order, warehouse):
    allocation = []

    for i in range(len(warehouse)):
        warehouseItems = list(warehouse[i]['inventory'].keys())
        result = {}

        for item in order:
            if item in warehouseItems and order[item] != 0:
                warehouseAmounts = warehouse[i]['inventory'][item]

                if warehouseAmounts  >= order[item]:
                    result[item]      = order[item]
                    warehouseAmounts -= order[item]
                    order[item]       = 0
                    
                elif warehouseAmounts < order[item] and warehouseAmounts != 0:
                    if item in result:
                        result[item] += warehouseAmounts
                    else:
                        result[item] = warehouseAmounts

                    order[item]     -= warehouseAmounts
                    warehouseAmounts = 0

        if len(result) != 0 : allocation.append({warehouse[i]['name']: result})
    
    if sum(order.values()) != 0:
        print([])
    else:
        print(allocation)

## Test

# order = { 'apple': 1 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]

# order = { 'apple': 1 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 1 }}, { 'name': 'dm', 'inventory': { 'apple': 10 }}, { 'name': 'third', 'inventory': { 'apple': 100 } }]

# order = { 'apple': 1 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'banana': 3 }}, { 'name': 'dm', 'inventory': { 'apple': 5, 'orange': 10 } }]

# order = { 'apple': 1 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]

# order = { 'apple': 1 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'banana': 1 } }]

# order = { 'apple': 5, 'banana' : 10 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 5 }}, { 'name': 'dm', 'inventory': { 'apple': 5, 'banana': 5 } }]

# order = { 'apple': 5, 'banana': 5, 'orange': 5 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 }}, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } }]

# order = { 'apple': 10 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 5 }}, { 'name': 'dm', 'inventory': { 'apple': 5} }]

# order = { 'apple': 10 }
# warehouse = [{ 'name': 'owd', 'inventory': { 'apple': 5 }}, { 'name': 'dm', 'inventory': { 'apple': 5, 'banana': 5 } }]

# inventoryAllocator(order, warehouse)