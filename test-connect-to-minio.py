from minio import Minio
from minio.error import S3Error

# Replace these values with your MinIO server details
# {"url":"https://minio.minio-operator.svc.cluster.local:443","accessKey":"4MEffUB7nHTMr4EO","secretKey":"t3ZPFrtUP8C4w9XuatdncjW2k0BEFyAw","api":"s3v4","path":"auto"}

minio_endpoint = "10.42.3.152"
access_key = "L2PGQJRRYJGZDKAA"
secret_key = "L5ONLMB2YLZVU4HUKTIQQIG2KWR5VERQ"
bucket_name = "thai-minio"
object_name = "test-object"
message_content = "Hello, MinIO!"

def push_message_to_minio():
    # Initialize MinIO client
    minio_client = Minio(
        minio_endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=True  # Set to True if using HTTPS
    )

    try:
        # Create a bucket if it doesn't exist
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Push the message to MinIO
        minio_client.put_object(
            bucket_name,
            object_name,
            message_content.encode('utf-8'),
            len(message_content)
        )

        print(f"Message '{message_content}' successfully pushed to MinIO.")

    except S3Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    push_message_to_minio()
