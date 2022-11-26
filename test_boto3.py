import boto3
import json


endpoint_name = "eeeendpoint"

client = boto3.Session().client(
    "sagemaker-runtime", 
    )

body = {
    "test_text": "string",
    "test_list": [
        "string"
    ]
}

F = json.dumps(body)

bin_pred = client.invoke_endpoint(
    EndpointName=endpoint_name,
    Body=F,
    ContentType="application/json",
)["Body"].read()
pred = json.loads(bin_pred)
print(pred)


