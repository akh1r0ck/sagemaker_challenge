# sagemaker_challenge

Amazon SageMakerを試すための文章分類APIです

基本構成

<pre>
.
├── Dockerfile
├── src
│   └── app.py
└── test_boto3.py
</pre>

- Dockerfile：実行環境
- src/app.py：API本体
- test_boto3.py：エンドポイントを叩くテストプログラム

ライブラリ

Python 3.8.15

| Library | Version |
| --- | --- |
| Core | - |
| torch | 1.13.0 |
| simpletransformers | 0.63.9 |
| scipy | 1.9.3 |
| API | - |
| fastapi | 0.87.0 |
| uvicorn | 0.20.0 |
| pydantic | 1.10.2 |
| AWS | - |
| boto3 | 1.26.16 |

AWS上の操作

1. ECR > リポジトリ > リポジトリを作成
1. ECR > リポジトリ > リポジトリを選択 > プッシュコマンとの表示
1. SageMaker > 推論 > モデル > モデルの作成
1. SageMaker > 推論 > エンドポイント設定 > エンドポイント設定の作成
1. SageMaker > 推論 > エンドポイント > エンドポイントの作成

