import platform
import hashlib

# Function to generate a unique device ID
def get_device_id():
    # Example: Using platform and hashlib to generate a device ID based on platform details
    platform_info = platform.uname()
    device_info = f"{platform_info.system}-{platform_info.node}-{platform_info.processor}".encode()
    device_id = hashlib.sha256(device_info).hexdigest()
    return device_id


# Get the device ID of the current machine
current_device_id = get_device_id()

print(f"Device ID: {current_device_id}")
# Wait for the user to press "Enter"
input("Press Enter to get the exite...")
