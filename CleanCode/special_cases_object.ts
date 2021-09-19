// Concrete Order
class Order {
    private _items: any[];

    constructor(items: any[]) {
        this._items = items;
    }

    public placeOrder() {
        // API call or whatever...
    }
}

// Null "version" of the Order
class NullOrder extends Order {
    constructor() {
        super([]);
    }

    public placeOrder() {
        // We just do nothing!
        // No errors are thrown!
    }
}

// Usage:
const orders: Order[] = [
    new Order(['fancy pants', 't-shirt']), new NullOrder()
];

for (const order of orders) {
    // This won't throw on nulls since we've
    // used the null object pattern.
    order.placeOrder();
}
