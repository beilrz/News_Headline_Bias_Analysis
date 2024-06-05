from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_fixed
import numpy as np
from tqdm import tqdm
import boto3

def get_cos_similiarity(A, B):
    # cosine similarity between A and B
    cos_sim=np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))

    return cos_sim

def cluster_centroid(vectors):
    return np.mean(vectors, axis=0)

client = OpenAI()
@retry(stop=stop_after_attempt(7), wait=wait_fixed(5))
def get_embedding(text, client = client, model="text-embedding-3-large"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def send_message_to_sqs(queue_url, messages):
    sqs = boto3.client('sqs')

    messages_batch = []
    for x in tqdm(messages):
        if len(messages_batch) >= 10:
            # send message
            response = sqs.send_message_batch(
                QueueUrl=queue_url,
                Entries=messages_batch)
    
            # empty the batch
            messages_batch = []
    
        message = {"Id" : str(uuid.uuid4()), "MessageBody" : json.dumps({"url" : x})}
        messages_batch.append(message)