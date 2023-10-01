import os

# 変換元ディレクトリのパス
source_dir = "test"

# 変換先ディレクトリのパス
output_dir = "test2"

# 変換元ディレクトリ内のファイルを再帰的にリストアップ
for root, _, files in os.walk(source_dir):
    for filename in files:
        source_file_path = os.path.join(root, filename)
        output_file_path = os.path.join(
            output_dir, os.path.relpath(source_file_path, source_dir)
        )

        # sjisでファイルの中身を確認して、エラーが出たらsjisではないとみなす
        try:
            with open(source_file_path, "r", encoding="sjis") as source_file:
                for line in source_file:
                    pass
        except UnicodeDecodeError:
            print(f"UTF-8 ファイル: {source_file_path}")
            continue

        # 存在しない場合はディレクトリ生成
        output_dir_path = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        # ファイルの文字コードをShift-JISからUTF-8に変換
        with open(source_file_path, "r", encoding="sjis") as source_file, open(
            output_file_path, "w", encoding="utf-8", newline="\r\n"
        ) as output_file:
            for line in source_file:
                output_file.write(line)

print("変換が完了しました。")
