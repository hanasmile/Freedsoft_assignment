function inventoryAllocator(order, warehouse) {
    let countWarehouse = warehouse.length;
    let remaining = 1;
    let allocation = [];

    for(let i = 0; i < countWarehouse && remaining !== 0; i++){
        let warehouseItems = Object.keys(warehouse[i].inventory);
        let result = {}

        warehouseItems.forEach(item => {
            let warehouseAmounts = warehouse[i].inventory[item];

            if(order[item]) {
                if(warehouseAmounts  >= order[item]) {
                    result[item]      = order[item];
                    warehouseAmounts -= order[item];
                    order[item]       = 0;
                }
                else if(warehouseAmounts < order[item] && warehouseAmounts !== 0) {
                    result[item] 
                        ? result[item] += warehouseAmounts
                        : result[item]  = warehouseAmounts
                    
                    order[item]      -= warehouseAmounts;
                    warehouseAmounts -= order[item];
                }
            }
        });

        if(Object.keys(result).length) allocation.push({[warehouse[i].name]: result});
        remaining = Object.values(order).reduce((prev, curr) => prev + curr); 
    }
    remaining 
        ? console.log([])
        : console.log(allocation)
};

// Test

// order = { apple: 1 }
// warehouse = [{ name: 'owd', inventory: { apple: 1 } }]

// order = { apple: 1 }
// warehouse = [{ name: 'owd', inventory: { apple: 1 }}, { name: 'dm', inventory: { apple: 10 }}, { name: 'third', inventory: { apple: 100 } }]

// order = { apple: 1 }
// warehouse = [{ name: 'owd', inventory: { banana: 3 } }, { name: 'dm', inventory: { 'apple': 5, 'orange': 10 } }]

// order = { apple: 1 }
// warehouse = [{ name: 'owd', inventory: { apple: 0 } }]

// order = { apple: 1 }
// warehouse = [{ name: 'owd', inventory: { banana: 1 } }]

// order = { apple: 5, banana : 10 }
// warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5, banana: 5 } }]

// order = { apple: 5, banana: 5, orange: 5 }
// warehouse = [{ name: 'owd', inventory: { apple: 5, orange: 10 } }, { name: 'dm', inventory: { banana: 5, orange: 10 } }]

// order = { apple: 10 }
// warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5 } }]

// order = { apple: 10 }
// warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5, banana: 5 } }]

// inventoryAllocator(order, warehouse);