class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = []
        self.distance_to_zero = []

    def add(self, num: int) -> None:
        if num == 0:
            self.distance_to_zero.append(0)
            self.prefix_product.append(0)
            return

        if not self.distance_to_zero or self.distance_to_zero[-1] == -1: self.distance_to_zero.append(-1)
        else: self.distance_to_zero.append(self.distance_to_zero[-1] + 1)

        if not self.prefix_product or self.prefix_product[-1] == 0: self.prefix_product.append(num)
        else: self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.distance_to_zero[-1] != -1 and self.distance_to_zero[-1] <= k - 1: return 0
        if len(self.prefix_product) - k - 1 < 0: return self.prefix_product[-1]
        return self.prefix_product[-1] // max(self.prefix_product[len(self.prefix_product) - k - 1],  1)
