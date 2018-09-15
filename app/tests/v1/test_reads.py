import unittest
from app.api.v1 import Orders

class TestOrders(unittest.TestCase):
	def setUp(self):
		self.orders = Orders()

	def test_orders_read_one_order_in_storage(self):
    response = self.app.get('/api/v1/orders)
    result = json.loads(response.data)
    self.assertEqual(result["Message"], "Success")
    self.assertEqual(response.status_code, 200)
		
if __name__ == '__main__':
	unittest.main()
