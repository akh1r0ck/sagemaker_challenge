<div align="center">
  <img src="./docs/assets/icon.png" width="800"/>
</div>

<p align="center">
    <a href="https://github.com/akh1r0ck/sagemaker_challenge/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/akh1r0ck/sagemaker_challenge.svg">
    </a>
    <img src="https://img.shields.io/badge/python-3.8.15-blue.svg">
    <img src="https://img.shields.io/badge/conda-22.9.0-brightgreen.svg">
</p>

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

※Coreの3つとAPIの3つはAPIのローカルデバッグ用です．APIのローカルデバッグをしない場合はboto3だけインストールすれば問題ありません．

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
    1. モデル名：適当に入力
    1. コンテナ入力オプション：モデルアーティファクトと推論イメージの場所を指定します。を選択（デフォルト）
    1. モデルアーティファクトと推論イメージの場所を指定します。：単一のモデルを使用するを選択（デフォルト）
    1. 推論コードイメージの場所：ECRのURIを入力
1. SageMaker > 推論 > エンドポイント設定 > エンドポイント設定の作成
    1. エンドポイント設定名：適当に入力
    2. エンドポイントのタイプ：サーバーレスを選択
    3. モデルの追加：作成したモデルを選択
    4. 本番稼働用バリアントの設定がデフォルトだと動かないので アクション > 編集 で変更
        | parameter | default | changed | maximum |
        | --- | --- | --- | --- |
        | メモリサイズ | 1 | 3 | 6 |
        | 最大同時実行数 | 20 | 1 | 20 |

        最大はそれぞれ6，20になっています．今回は3，1に設定します．
1. SageMaker > 推論 > エンドポイント > エンドポイントの作成
    1. エンドポイント名：適当に入力
    1. エンドポイント設定のアタッチ
        - 既存のエンドポイント設定の使用（デフォルト）
            1. エンドポイント設定：作成したエンドポイント設定をラジオボタンで選択
            1. エンドポイント設定の選択を押す
        - 新しいエンドポイント設定の作成：前述のエンドポイント設定の作成の手順で作成

### ローカル（上記手順4）

1. test_boto3.py > 作成したエンドポイントを呼び出すように書き換え  
    `endpoint_name = "eeeendpoint”`を作成したエンドポイントの名前に変える
1. test_boto3.pyを実行
