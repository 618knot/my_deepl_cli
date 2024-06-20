import fire
import deepl
import os
from os.path import join, dirname
from dotenv import load_dotenv

# ▽▽▽ DeepL translatorを使うための準備 ▽▽▽

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("DEEPL_API_KEY")
translator = deepl.Translator(API_KEY)

# △△△ DeepL translatorを使うための準備 △△△


def translate_document(input_file, output_file):
  """
  入力された文書ファイルを日本語に翻訳して出力する

  Parameters
  ----------
  input_file: string
    翻訳したいファイル名(ファイルのpathでも可)
    本ディレクトリ配下のものに限る

  output_file: string
    翻訳後に出力されるファイル名(pathを含めても可)
    本ディレクトリ配下に出力される
  """
  try:
    result = translator.translate_document_from_filepath(
      input_path=f"./{input_file}",
      output_path=f"./{output_file}",
      target_lang="JA"
    )
  
    print(result)

  except:
    print("some error occurred")

if __name__ == "__main__":
  fire.Fire(translate_document)
