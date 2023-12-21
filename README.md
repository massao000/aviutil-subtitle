# aviutil-subtitle
aviutilの字幕付けを楽にするGUI

## テンプレートの作成

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/801c257b-bad8-4ebb-a3e0-8ce13e45647d)

1. テンプレートにしたいテキストをレイヤーに入る
1. 拡張編集内で右クリック
1. `ファイル`から`オブジェクトファイルのエクスポート`で保存

## GUIの使い方

`default_exo.txt`に字幕のテンプレートパスを一行目に書き込む

GUIは以下のようなものになります

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/f35a304c-9f34-45cf-9b23-3d63564fd8e5)

<br>

テキストファイル欄にある`Browse`を押すと以下のようになります

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/0673a84e-bc43-4d26-9e3b-568de5f98ebb)

- 表示されたテキストは編集が可能です
- 自動で読み込んだテキストファイルのディレクトリに保存先の設定がされます、保存先の指定も可能です
- 改行ごとにオブジェクトが生成されます
- 変換ボタンを押せば保存されます。
- 保存名は`jimaku.exo`

---

[参考コード](https://gist.github.com/pandanote-info/41ddc167763279f4c9044e01edb2bd15#file-txt2exo-py)
