# 使用此 Python Script 以獲得向量資料庫的總筆數及顯示資料 

import os
import weaviate
import consts.const as my_param

os.environ["OPENAI_API_TYPE"] = my_param.OPENAI_API_TYPE
os.environ["OPENAI_API_VERSION"] = my_param.OPENAI_API_VERSION
os.environ["OPENAI_API_BASE"] = my_param.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = my_param.OPENAI_AZURE_API_KEY

PROPERITIES = ["uuid", "title", "content"]
classNm = 'Temp_1016'

# 統計筆數
if __name__ == "__main__1":
    client = weaviate.Client(url=my_param.WEAVIATE_URL,
                             additional_headers={"X-Azure-Api-Key": f"{my_param.OPENAI_AZURE_API_KEY}"})
    print(client.query.aggregate(classNm).with_meta_count().do())

# 顯示所有資料
if __name__ == "__main__2":
    client = weaviate.Client(url=my_param.WEAVIATE_URL,
                             additional_headers={"X-Azure-Api-Key": f"{my_param.OPENAI_AZURE_API_KEY}"})
    client.schema.exists(classNm)

    result = client.query.get(class_name=classNm, properties=PROPERITIES).with_limit(10000).do()

    print(str(result))
