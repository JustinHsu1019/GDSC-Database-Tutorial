# 使用此 Python Script 以新建向量資料庫及插入數據

import os
import uuid
import weaviate
import consts.const as my_param
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_TYPE"] = my_param.OPENAI_API_TYPE
os.environ["OPENAI_API_VERSION"] = my_param.OPENAI_API_VERSION
os.environ["OPENAI_API_BASE"] = my_param.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = my_param.OPENAI_AZURE_API_KEY

class WeaviateManager:
    def __init__(self, classNm):
        self.url = my_param.WEAVIATE_URL
        self.embeddings = OpenAIEmbeddings(chunk_size=1, model=my_param.EMBEDDING_MODEL_SEARCH)
        self.client = weaviate.Client(
            url=my_param.WEAVIATE_URL,
            additional_headers={"X-Azure-Api-Key": f"{my_param.OPENAI_AZURE_API_KEY}"}
        )
        self.schema = self.client.schema
        self.classNm = classNm
        self.check_class_exist()
        pass

    def check_class_exist(self):
        if self.client.schema.exists(self.classNm):
            print(f'{self.classNm} is ready')
            return True
        schema = {
            "class": self.classNm,
            "properties": [
                {
                    "name": "uuid",
                    "dataType": ["text"]
                },
                {
                    "name": "title",
                    "dataType": ["text"]
                },
                {
                    "name": "content",
                    "dataType": ["text"]
                }
            ],
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "text2vec-openai": {
                    "resourceName": my_param.RESOURCE_NAME,
                    "deploymentId": my_param.EMBEDDING_MODEL_SEARCH
                }
            }
        }
        print(f'creating {self.classNm}...')
        self.client.schema.create_class(schema)
        print(f'{self.classNm} is ready')
        return True
        
    def insert_data(self, title_text, content_text):
        data_object = {
            "uuid": str(uuid.uuid4()),
            "title": title_text,
            "content": content_text
        }
        self.client.data_object.create(data_object, self.classNm)

if __name__ == "__main__":
    manager = WeaviateManager("Temp_1016")

    manager.insert_data("標題一", "這是第一筆資料的內容。")
    manager.insert_data("標題二", "這是第二筆資料的內容。")
    manager.insert_data("標題三", "這是第三筆資料的內容。")
