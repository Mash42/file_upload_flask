# -*- coding: utf-8 -*-
# content utf-8
import os
from flask import Flask, request, redirect, url_for, render_template,flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
app = Flask(__name__)

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = '.' + os.sep + 'upload'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ホーム
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", message="ファイルをアップロードしてください。")

# アップロード
@app.route('/upload', methods=["GET", "POST"])
def upload():
    message = "アップロード処理を実行しました。"
# リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            message = "ファイルがありません"
        # データの取り出し
        file = request.files['file']
        # ファイル名がなかった時の処理
        if file.filename == '':
            message = "ファイル名が取得できませんでした。"

        # 危険な文字を削除（サニタイズ処理）
        filename = secure_filename(file.filename)
        # ファイルの保存
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("index.html", message=message)

# アプリ起動
if __name__ == '__main__':
    app.run(host="localhost", port=5555, debug=True)
