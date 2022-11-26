# sagemaker_challenge

Amazon SageMakerを試すための文章分類APIです

## ディレクトリ基本構成

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

## 実行環境

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

```bash
$ pip install -r requirements.txt
```

<details><summary>個別インストール</summary>

```bash
$ pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
$ pip install simpletransformers
$ pip install scipy
$ pip install fastapi uvicorn pydantic boto3
```

</details>


## AWS上の操作

1. ECR > リポジトリ > リポジトリを作成
1. ECR > リポジトリ > リポジトリを選択 > プッシュコマンとの表示
1. SageMaker > 推論 > モデル > モデルの作成
1. SageMaker > 推論 > エンドポイント設定 > エンドポイント設定の作成
1. SageMaker > 推論 > エンドポイント > エンドポイントの作成

