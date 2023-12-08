import unittest
import http.client

class TestSimpleServer(unittest.TestCase):
    def test_server_response(self):
        # Set the server address and port
        server_address = ('localhost', 9000)

        # Create an HTTP connection to the server
        connection = http.client.HTTPConnection(*server_address)

        try:
            # Send a GET request to the server with a data parameter
            connection.request('GET', '/?data=TestValue')

            # Get the response from the server
            response = connection.getresponse()
            

            # Check that the response status code is 200 OK
            self.assertEqual(response.status, 200)

            # Read and decode the response content
            content = response.read().decode('utf-8')

            # Check that the response contains the expected data
            self.assertIn('Received data: TestValue', content)

        finally:
            # Close the connection
            connection.close()

    def test_post_request(self):
        # Set the server address and port
        server_address = ('localhost', 9000)

        # Create an HTTP connection to the server
        connection = http.client.HTTPConnection(*server_address)

        try:
            # Send a POST request to the server with a data parameter
            data = 'data=TestPostValue'
            headers = {'Content-type': 'application/x-www-form-urlencoded'}
            connection.request('POST', '/', data, headers)

            # Get the response from the server
            response = connection.getresponse()

            # Check that the response status code is 200 OK
            self.assertEqual(response.status, 200)

            # Read and decode the response content
            content = response.read().decode('utf-8')

            # Check that the response indicates successful reception of POST data
            self.assertIn("POST data received and saved to file ", content)

        finally:
            # Close the connection
            connection.close()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleServer)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)