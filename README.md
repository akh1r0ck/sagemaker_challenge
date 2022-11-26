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

```
Python 3.8.15
conda 22.9.0
```

セットアップコマンド

```bash
$ conda create -n st python=3.8.15
$ git clone https://github.com/akh1r0ck/sagemaker_challenge.git
$ cd sagemaker_challenge
$ pip install -r requirements.txt
```

<details><summary>ライブラリの個別インストール</summary>

```bash
$ pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
$ pip install simpletransformers
$ pip install scipy
$ pip install fastapi uvicorn pydantic boto3
```

</details>

主要なライブラリはこの通りです．

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


## 実行手順

ざっくり処理内容はこの通りです．

1. terminalでAWSのアカウントを設定
1. DockerImageをECR※にプッシュ
1. SageMakerでエンドポイント作成
1. ローカルで呼び出す

※ECR：Elastic Container Registry

### AWS側（上記手順1〜3）

1. アカウントアイコン > セキュリティ認証情報(IAM) > アクセスキー > 新しいアクセスキーの作成
1. AWS CLI > AWS Access Key IDとAWS Secret Access Key
1. ECR > リポジトリ > リポジトリを作成
1. ECR > リポジトリ > リポジトリを選択 > プッシュコマンドの表示
1. SageMaker > 推論 > モデル > モデルの作成
1. SageMaker > 推論 > エンドポイント設定 > エンドポイント設定の作成
1. SageMaker > 推論 > エンドポイント > エンドポイントの作成

### ローカル（上記手順4）

1. test_boto3.py > 作成したエンドポイントを呼び出すように書き換え
1. test_boto3.pyを実行
