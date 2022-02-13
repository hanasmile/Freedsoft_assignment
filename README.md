## Programming Level

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution).

Your task is to implement InventoryAllocator class to produce the cheapest shipment.

The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example an order of apples, bananas and oranges of 5 units each will be `{ apple: 5, banana: 5, orange: 5 }`

The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for these items. For example the inventory across two warehouses called owd and dm for apples, bananas and oranges could look like `[{ name: owd, inventory: { apple: 5, orange: 10 }}, { name: dm, inventory: { banana: 5, orange: 10 } }]`

You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to ship from than the second warehouse.

Please write unit tests with your code, a few are mentioned below, but these are not comprehensive.

## Test cases

- Order can be shipped using one warehouse

```Javascript
// input
order = { apple: 1 }
warehouse = [{ name: 'owd', inventory: { apple: 1 } }]

// output
[{ owd: { apple: 1 } }]
```

```Javascript
// input
order = { apple: 1 }
warehouse = [{ name: 'owd', inventory: { apple: 1 } }, { name: 'dm', inventory: { apple: 10 }}, { name: 'third', inventory: { apple: 100 } }]

// output
[{ owd: { apple: 1 } }]
```

```Javascript
// input
order = { apple: 1 }
warehouse = [{ name: 'owd', inventory: { banana: 3 } }, { name: 'dm', inventory: { apple: 5, orange: 10 } }]

// output
[{ dm: { apple: 1 } }]

```

- Order can't be shipped because of nothing enough inventory

```Javascript
// input
order = { apple: 1 }
warehouse = [{ name: 'owd', inventory: { apple: 0 } }]

// output
[]
```

```Javascript
// input
order = { apple: 1 }
inventory = [{ name: 'owd', inventory: { banana: 1 } }]

// output
[]
```

```Javascript
// input
order = { apple: 5, banana : 10 }
warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5, banana: 5 } }]

// output
[]
```

- Order can be shipped using multiple warehouses

```Javascript
// input
order = { apple: 5, banana: 5, orange: 5 }
warehouse = [{ name: 'owd', inventory: { apple: 5, orange: 10 } }, { name: 'dm', inventory: { banana: 5, orange: 10 } } ]

// output
[{ owd: { apple: 5, orange: 5 } }, { dm: { banana: 5 } }]
```

```Javascript
// input
order = { apple: 10 }
warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5}}]

// output
[{ owd: { apple: 5 } }, { dm: { apple: 5 } }]
```

```Javascript
// input
order = { apple: 10 }
warehouse = [{ name: 'owd', inventory: { apple: 5 } }, { name: 'dm', inventory: { apple: 5, banana: 5 }}]

// output
[{ owd: { apple: 5 } }, { dm: { apple: 5 } }]
```
