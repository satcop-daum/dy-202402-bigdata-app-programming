import kagglehub

# Download latest version
path = kagglehub.dataset_download("kimjmin/seoul-metro-usage")

print("파일이 저장된 장소:", path)
