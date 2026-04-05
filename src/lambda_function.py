import boto3
from PIL import Image
import os
import urllib.parse

s3 = boto3.client('s3')

OUTPUT_BUCKET = "processed-image-bucket-kuldeep"
RESIZE_WIDTH = 200
RESIZE_HEIGHT = 200


def lambda_handler(event, context):
    """
    AWS Lambda handler for image processing.
    Triggered by S3 PUT events on the input bucket.
    Downloads image, resizes it, and uploads to output bucket.
    """

    # Extract bucket name and file key from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    filename = os.path.basename(key)
    download_path = f'/tmp/{filename}'
    upload_path = f'/tmp/resized-{filename}'

    print(f"[START] Processing file: {filename}")
    print(f"[INFO]  Source Bucket: {bucket}")
    print(f"[INFO]  File Key: {key}")

    try:
        # Step 1: Download image from input bucket
        print(f"[STEP 1] Downloading image from S3...")
        s3.download_file(bucket, key, download_path)
        print(f"[STEP 1] Download complete!")

        # Step 2: Resize image using Pillow
        print(f"[STEP 2] Resizing image to {RESIZE_WIDTH}x{RESIZE_HEIGHT}...")
        with Image.open(download_path) as image:
            original_size = image.size
            resized = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
            resized.save(upload_path)
        print(f"[STEP 2] Resized from {original_size} to ({RESIZE_WIDTH}, {RESIZE_HEIGHT})")

        # Step 3: Upload processed image to output bucket
        print(f"[STEP 3] Uploading to output bucket...")
        output_key = f'processed/resized-{filename}'
        s3.upload_file(upload_path, OUTPUT_BUCKET, output_key)
        print(f"[STEP 3] Upload complete! -> s3://{OUTPUT_BUCKET}/{output_key}")

        print(f"[DONE] Image processed successfully!")

        return {
            'statusCode': 200,
            'body': f'Image {filename} resized from {original_size} to ({RESIZE_WIDTH},{RESIZE_HEIGHT}) successfully!'
        }

    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise e
