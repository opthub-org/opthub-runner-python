[English Version](https://github.com/opthub-org/opthub-runner-python) 👈

# opthub-runner-python

![Skills](https://skillicons.dev/icons?i=py,graphql,vscode,github)

opthub-runner-pythonは、ローカル実行用のEvaluatorを提供するPythonパッケージです。

- Evaluator: Docker Imageを使って、ローカルで解を評価する機能

このリポジトリでは、opthub-runner-pythonのインストールやEvaluatorの利用方法を説明しています。


## 利用方法

まずは、事前に以下の環境設定が必要です。

1. Python 3.8以上をインストール
2. pipを使えるように設定
3. Docker\*をインストール

\*Macの場合は、[Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)をインストールして起動できます。

上記の環境設定が完了した後、以下のコマンドでPyPIから`opthub-runner-python`をインストールします。
```bash
pip install opthub-runner-python
```

インストール後、以下ようにPythonコードでEvaluatorクラスをインポートすることで利用できます。

```python
from opthub_runner.evaluator import Evaluator
```

Evaluatorクラスの具体的な利用方法は、[利用例](#usage)、[オプション](#option)、[実行結果](#result)を参考にしてください。

なお、コードを動かす際には**Dockerの起動**が必要となります。Dockerを起動した状態でないと、正常に実行できないので注意してください。


## 利用例 <span id="usage"></span>
以下に、最適解を`[1, 1]`とするSphere関数で解を評価する例を以下に示します。

```python
from opthub_runner.evaluator import Evaluator



evaluator = Evaluator("opthub/sphere:latest",
                      {"SPHERE_OPTIMA": [[1, 1]]}) # Initialize Evaluator

x = [0, 2] # Solution to evaluate
result = evaluator.run(x) # Evaluate

print(result) # {'objective': 2, 'feasible': None, 'constraint': None, 'info': None}
```

Evaluatorの初期化では、Sphere関数のDocker Image `opthub/sphere:latest`と、Dockerプロセスの環境変数`SPHERE_OPTIMA`を設定しています。その後runメソッドでは、内部でDockerプロセスを起動し、解`[0, 2]`を評価しています。

runメソッドに入力する解や利用するDockerイメージの情報は、[OptHub](https://opthub.ai)の各問題に記述されております。

## オプション <span id="option"></span>
Evaluatorクラスの初期化に用いる引数は以下の表の通りです (*は必須)。

| オプション | 型 | デフォルト値 | 説明 |
|----|----|----|----|
| docker_image* | str| - | 評価に用いるDocker Image名 |
| environment* | dict[str, object] | - | 環境変数 |
| rm | bool | True | 評価後にDocker Containerを削除するかどうか |
|timeout | int | 43200 | Docker Imageを使った解評価の制限時間　|

## 実行結果 <span id="result"></span>
Evaluatorクラスのrunメソッドは、評価結果を返します。評価結果は、Keyと、Keyに対応するValueの組を要素とする辞書で表されます。評価結果に含まれるKeyと、Keyに対応するValueの型を以下の表に示します。

| Key | Valueの型 | 説明 |
|----|----|----|
| objective | object | 解の目的関数値 |
| feasible | bool or None | 解の実行可能性 |
| constraint | object or None | 解の制約に関する情報 |
| info | object or None | 評価に関する情報 |

objective, constraint, feasible, infoの詳細な説明は、[OptHub](https://opthub.ai)の各問題に記述されております。

## トラブルシューティング
以下のエラーが出力された場合は、Dockerが起動していない可能性が高いです。Dockerを起動した上で、再実行してください。Macの場合は、Docker Desktopを起動することで、Dockerを起動できます。
```shell
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
```

## 開発者の方へ

以下のステップに従って環境をセットアップしてください。

1. このリポジトリをclone
2. Poetryの設定
3. `poetry install`を実行
4. 推奨されたVS Codeの拡張機能をダウンロード
5. 他のパッケージとの競合を避けるため、以下のVS Codeの拡張機能を無効にする
    - ms-python.pylint
    - ms-python.black-formatter
    - ms-python.flake8
    - ms-python.isort

## 連絡先

ご質問やご不明な点がございましたら、お気軽にお問い合わせください (Email: dev@opthub.ai)。

<img src="https://opthub.ai/assets/images/logo.svg" width="200">
