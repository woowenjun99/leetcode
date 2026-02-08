from collections import defaultdict

class OrderManagementSystem:
    def __init__(self):
        self.order_id_to_order_type = {}
        self.order_id_to_order_price = {}
        self.order_price_and_order_type_to_order_id = defaultdict(lambda: defaultdict(set))

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.order_id_to_order_type[orderId] = orderType
        self.order_id_to_order_price[orderId] = price
        self.order_price_and_order_type_to_order_id[orderType][price].add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        order_type = self.order_id_to_order_type[orderId]
        price = self.order_id_to_order_price[orderId]
        self.order_price_and_order_type_to_order_id[order_type][price].remove(orderId)
        self.order_id_to_order_price[orderId] = newPrice
        self.order_price_and_order_type_to_order_id[order_type][newPrice].add(orderId)

    def cancelOrder(self, orderId: int) -> None:
        order_type = self.order_id_to_order_type[orderId]
        price = self.order_id_to_order_price[orderId]
        self.order_price_and_order_type_to_order_id[order_type][price].remove(orderId)
        del self.order_id_to_order_type[orderId]
        del self.order_id_to_order_price[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return list(self.order_price_and_order_type_to_order_id[orderType][price])

