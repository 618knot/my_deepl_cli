# DeepLのドキュメントファイル翻訳を自前のAPIキーを使って行うためのCLIツール

> [!WARNING]
> DeepLのAPIを利用しているので、取り扱いにはご注意ください
> 使用は自己責任で

## 使い方

1. `my_deepl_cli`をVSCodeなどで開く
2. `requirements.txt`に記述されているpythonのライブラリをインポートする
3. `my_deepl_cli`直下に`.env`ファイルを作成する
4. DeepLのAPI KEYを取得してくる
5. `.env`に`DEEPL_API_KEY=`に取得したAPI KEYを入力する

```.env
DEEPL_API_KEY=hogehogeapikey
```

5. VSCodeにくっついているターミナルなどで下記コマンドを打つ

```sh
python translate_doc.py --input_file {翻訳したいファイル名} --output_file {出力ファイル名}

# ex)
python translate_doc.py --input_file hoge.pdf --output_file fuga.pdf
```

6. しばらく待てば翻訳済みのファイルが多分出力されます
