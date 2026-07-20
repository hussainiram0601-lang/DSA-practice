class StockSpanner:

    def __init__(self):
        # The stack will store pairs of: (price, span)
        self.st = []

    def next(self, price: int) -> int:
        # Every day starts with a minimum span of 1 (itself)
        span = 1
        
        # Pop elements from the stack while the previous price is <= current price
        while len(self.st) > 0 and self.st[-1][0] <= price:
            # Add the span of the popped price to our current span
            span += self.st.pop()[1]
            
        # Push the current price and its accumulated span onto the stack
        self.st.append((price, span))
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)