import requests
from token import token
file_list = ['1.txt', '2.txt', '3.txt']

class YaUploader:

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json/txt', 'Authorization': f'OAuth {self.token}'}

    def get_upload_link(self, file_path):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{file_path}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def create_folder(self, folder_name):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': f'/{folder_name}'}
        response = requests.put(url, headers=self.get_headers(), params=params)
        if response.status_code == 201:
            print(f"Папка {params['path']} успешно создана\nstatus_code: {response.status_code}")
        else:
            print(f"Папка {folder_name} уже существует\n status_code: {response.status_code}")
        return response.status_code

    def upload(self, file_path, disk_file_name):
        upload_link = self.get_upload_link(file_path)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Загрузка прошла успешно')

    def multiple_upload(self, file_list):
        for file in file_list:
            disk_file_name = file
            upload_link = self.get_upload_link(disk_file_name)
            response = requests.put(upload_link, headers=self.get_headers(), data=open(file_path, 'rb'))
            if response.status_code == 201:
                print(f'Загрузка файла {file} прошла успешно')

if __name__ == '__main__':
    path_to_file = ...
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.multiple_upload(path_to_file)