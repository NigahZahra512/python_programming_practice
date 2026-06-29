class CloudStorageManager:

    def upload_image(self, file_name, file_size_mb):

        # Check file extension
        if not (file_name.endswith(".jpg") or file_name.endswith(".png")):
            raise ValueError("Only .jpg and .png files are allowed!")


        if file_size_mb >= 2:
            raise ValueError("File size must be under 2 MB!")

        # Return mock URL
        return "https://cdn.cloudstorage.com/images/" + file_name



cloud = CloudStorageManager()

try:
    url = cloud.upload_image("shirt.jpg", 1.5)
    print("Upload Successful ")
    print("Image URL:", url)

except ValueError as e:
    print("Error:", e)