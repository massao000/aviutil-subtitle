# aviutil-subtitle
aviutilの字幕付けを楽にするGUI

## テンプレートの作成

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/3e40f253-2bcf-4311-8785-0d58cc4a42be)

1. テンプレートにしたいテキストをレイヤーに入る
1. 拡張編集内で右クリック
1. `ファイル`から`オブジェクトファイルのエクスポート`で保存

## GUIの使い方

`default_exo.txt`に字幕のテンプレートパスを一行目に書き込む

GUIは以下のようなものになります

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/f35a304c-9f34-45cf-9b23-3d63564fd8e5)

<br>

テキストファイル欄にある`Browse`を押すと以下のようになります

<!-- ![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/0673a84e-bc43-4d26-9e3b-568de5f98ebb) -->

![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/69ea0d73-54d3-4ac2-9891-66fe0edf0346)

変換するときのファイル構成
```
Folder
├─audio.wav
├─audio.wav
├─audio.wav
└─text.txt
```

新しくオーディオディレクトリの選択を増やしました。
これはテキストのオブジェクトを音声に合わせて配置するようにしました。
自動で読み込んだテキストファイルのディレクトリに選択されます。

ファイル構成のようにしていれば楽にできます。

注意としては音声ファイルとテキストの行数を合わせてください
![image](https://github.com/massao000/aviutil-subtitle/assets/69783019/10451880-5c49-4361-8592-44b63a0554f4)

- 表示されたテキストは編集が可能です
- 自動で読み込んだテキストファイルのディレクトリに保存先の設定がされます、保存先の指定も可能です
- 変換ボタンを押せば保存されます。
- 保存名は`jimaku.exo`

---

[参考コード](https://gist.github.com/pandanote-info/41ddc167763279f4c9044e01edb2bd15#file-txt2exo-py)
