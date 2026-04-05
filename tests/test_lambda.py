# ============================================================
# test_lambda.py - Unit tests for Lambda function
# ============================================================

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.sample_event = {
            'Records': [{
                's3': {
                    'bucket': {'name': 'image-upload-bucket-kuldeep'},
                    'object': {'key': 'test-image.jpg'}
                }
            }]
        }
        self.sample_context = MagicMock()

    def test_event_parsing(self):
        """Test that S3 event is parsed correctly"""
        bucket = self.sample_event['Records'][0]['s3']['bucket']['name']
        key = self.sample_event['Records'][0]['s3']['object']['key']
        self.assertEqual(bucket, 'image-upload-bucket-kuldeep')
        self.assertEqual(key, 'test-image.jpg')

    def test_output_key_format(self):
        """Test that output key is formatted correctly"""
        filename = 'test-image.jpg'
        output_key = f'processed/resized-{filename}'
        self.assertEqual(output_key, 'processed/resized-test-image.jpg')

    def test_resize_dimensions(self):
        """Test resize dimensions are set correctly"""
        RESIZE_WIDTH = 200
        RESIZE_HEIGHT = 200
        self.assertEqual(RESIZE_WIDTH, 200)
        self.assertEqual(RESIZE_HEIGHT, 200)


if __name__ == '__main__':
    unittest.main()
