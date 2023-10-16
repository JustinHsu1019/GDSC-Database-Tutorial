import os
import weaviate
import consts.const as my_param
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_TYPE"] = my_param.OPENAI_API_TYPE
os.environ["OPENAI_API_VERSION"] = my_param.OPENAI_API_VERSION
os.environ["OPENAI_API_BASE"] = my_param.OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = my_param.OPENAI_AZURE_API_KEY

class WeaviateSemanticSearch:
    def __init__(self, classNm):
        self.url = my_param.WEAVIATE_URL
        self.embeddings = OpenAIEmbeddings(chunk_size=1, model=my_param.EMBEDDING_MODEL_SEARCH)
        self.client = weaviate.Client(
            url=my_param.WEAVIATE_URL,
            additional_headers={"X-Azure-Api-Key": f"{my_param.OPENAI_AZURE_API_KEY}"}
        )
        self.classNm = classNm

    def semantic_search(self, query_text, num):
        query_vector = self.embeddings.embed_query(query_text)

        vector_str = ",".join(map(str, query_vector))

        gql_query = f"""
        {{
            Get {{
                {self.classNm}(nearVector: {{vector: [{vector_str}] }}, limit: {num}) {{
                    content
                    _additional {{
                        distance
                    }}
                }}
            }}
        }}
        """

        search_results = self.client.query.raw(gql_query)
        
        if 'errors' in search_results:
            raise Exception(search_results['errors'][0]['message'])
        
        results = search_results['data']['Get'][self.classNm]
        
        return results

if __name__ == "__main__":
    searcher = WeaviateSemanticSearch("Temp_1016")
    results = searcher.semantic_search("標題1", 2)

    for idx, result in enumerate(results, 1):
        print(f"Top{idx} Result: {result}")
        print(f"Vector Distance: {result['_additional']['distance']}")
