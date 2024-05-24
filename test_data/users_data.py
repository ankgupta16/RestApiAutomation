import os
import pandas as pd

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_path, 'test_data', 'user_data.csv')
df = pd.read_csv(file_path,sep=',',encoding="utf-8")


def get_create_user_data_from_csv():
    user_data = []
    for idx in df.index:
        user_dict = {
            'name': df['name'][idx],
            'gender': df['gender'][idx],
            'email': df['email'][idx],
            'status': df['status'][idx],
        }
        user_data.append(user_dict)
    print(user_data)
    return user_data


get_create_user_data_from_csv()