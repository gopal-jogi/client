import unittest
import http.client

class TestSimpleServer(unittest.TestCase):
    def test_server_response(self):
        # address and port
        server_address = ('localhost', 9000)

        #  HTTP connection to the server
        connection = http.client.HTTPConnection(*server_address)

        try:
            # Send a GET request 
            connection.request('GET', '/?data=TestValue')

            response = connection.getresponse()
            
            self.assertEqual(response.status, 200)

            content = response.read().decode('utf-8')

            self.assertIn('Received data: TestValue', content)

        finally:
            # Close 
            connection.close()

    def test_post_request(self):

        server_address = ('localhost', 9000)

        connection = http.client.HTTPConnection(*server_address)

        try:
            data = 'data=TestPostValue'
            headers = {'Content-type': 'application/x-www-form-urlencoded'}
            connection.request('POST', '/', data, headers)

            response = connection.getresponse()

        
            self.assertEqual(response.status, 200)

        
            content = response.read().decode('utf-8')

            
            self.assertIn("POST data received and saved to file ", content)

        finally:
            connection.close()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleServer)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
