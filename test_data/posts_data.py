import os
import pandas as pd

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_path, 'test_data','post_data.csv')
df = pd.read_csv(file_path, sep=',', encoding="utf-8")

def get_create_post_data_from_csv():
    post_data = []
    for idx in df.index:
        post_dict = {
            'title': df['title'][idx],
            'body': df['body'][idx],
        }
        post_data.append(post_dict)
    return post_data
