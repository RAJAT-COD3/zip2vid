import zipfile

with zipfile.ZipFile("test1.zip", "r") as zip_file:
    binary_data = zip_file.read()

with open("binary_data.txt", "w") as text_file:
    for byte in binary_data:
        text_file.write(str(byte))
