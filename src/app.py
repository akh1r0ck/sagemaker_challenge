from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from scipy.special import softmax
from simpletransformers.classification import ClassificationModel, ClassificationArgs

app = FastAPI()

class Test(BaseModel):
    test_text: str
    test_list: list

@app.get("/ping")
def ping():
    return {"Hello": "World"}

@app.post("/invocations")
def transformation(inputs: Test):
    
    inputs = inputs.test_list if len(inputs.test_list)>0 else [inputs.test_text] 

    model = ClassificationModel("roberta", "cardiffnlp/twitter-roberta-base-sentiment", use_cuda=False)
    _, raw_pred = model.predict(inputs)

    raw_pred = softmax(raw_pred, axis=1)
    outputs = [{"positive": round(raw[0], 3), "neutral": round(raw[1], 3), "negative": round(raw[2], 3)} for raw in raw_pred]
        
    return {"result": outputs}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080
    )