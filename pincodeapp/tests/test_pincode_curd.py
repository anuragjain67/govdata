from tastypie.test import ResourceTestCase
from pincodeapp.models import PinCodeDirectory


class TestPincodeResource(ResourceTestCase):
    '''
    Test cases for pincodes
    '''

    def setUp(self):
        '''
        Initial setup of Test cases
        '''
        super(TestPincodeResource, self).setUp()
        pincode_karnataka = PinCodeDirectory(pincode="560102", state_name="Karnataka")
        pincode_karnataka.save()
        pincode_rajasthan = PinCodeDirectory(pincode="305002", state_name="Rajasthan")
        pincode_rajasthan.save()

    def test_get_pincodes(self):
        """
        It will test for get pincodes 
        """
        response = self.api_client.get('/api/pincodes/')
        deserialized_response = self.deserialize(response)
        self.assertEqual(deserialized_response["meta"]["total_count"], 2)

    def test_search_pincodes(self):
        """
        It will test for search pincode api
        """
        # Query for rajasthan
        response = self.api_client.get('/api/pincodes/?q=raja')
        deserialized_response = self.deserialize(response)
        self.assertEqual(deserialized_response["meta"]["total_count"], 1)

        #Query for pincode
        response = self.api_client.get('/api/pincodes/?q=305')
        deserialized_response = self.deserialize(response)
        self.assertEqual(deserialized_response["meta"]["total_count"], 1)

        #Query for null, it should return all data
        response = self.api_client.get('/api/pincodes/?q=')
        deserialized_response = self.deserialize(response)
        self.assertEqual(deserialized_response["meta"]["total_count"], 2)

    def test_post_pincodes(self):
        """
        It will test for post pincodes 
        """
        pincode_jaipur = {
                "pincode": "312122",
                "district_name": "jaipur"
                }
        response = self.api_client.post('/api/pincodes/', data=pincode_jaipur)
        self.assertHttpCreated(response)

        # Also verify it comes through get api
        response = self.api_client.get('/api/pincodes/')
        deserialized_response = self.deserialize(response)
        self.assertEqual(deserialized_response["meta"]["total_count"], 3)
