import PySimpleGUI as sg
import os
from script import exo_changer

default_exo_file_path = 'default_exo.txt'

try:
    with open(default_exo_file_path, 'r', encoding='UTF-8') as f:
        default_exo = f.read()
except FileNotFoundError:
    # ファイルが存在しない場合は新規に作成
    default_exo = "テンプレートのexoパスの設定"
    with open(default_exo_file_path, 'w+', encoding='UTF-8') as f:
        f.write(default_exo)

# PySimpleGUIのGUIレイアウト
layout = [
    [sg.Text('exoファイル:', size=(15)), sg.InputText(default_text=default_exo,key='-EXO_FILE', disabled_readonly_background_color="gray", disabled=True), sg.FileBrowse(file_types=(("exoファイル", "*.exo"),))],
    [sg.Text('テキストファイル:'), sg.InputText(key='-TEXT_FILE', enable_events=True, disabled_readonly_background_color="gray", disabled=True), sg.FileBrowse(file_types=(("テキストファイル", "*.txt"),), enable_events=True)],
    [sg.Multiline(default_text='', size=(70, 10), key='-TEXT_OUTPUT')],
    [sg.Text('保存ディレクトリ:'), sg.InputText(key='-OUTPUT_DIR', disabled_readonly_background_color="gray", disabled=True), sg.FolderBrowse()],
    [sg.Button('変換', size=(30, 1), k='-EXECUTION')]
]

window = sg.Window('変換', layout)

while True:
    event, values = window.read()
    print(values)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if event == '-EXECUTION':
        if values['-EXO_FILE']:
            exo_file_path = values['-EXO_FILE']
        else:
            sg.popup_error('exoファイルがありません')
    
        if values['-TEXT_OUTPUT']:
            texts = values['-TEXT_OUTPUT']
        else:
            sg.popup_error('テキストがありません')
            
        if values['-OUTPUT_DIR']:
            output_dir = values['-OUTPUT_DIR']
        else:
            sg.popup_error('出力先がありません')
            
        if exo_file_path != '' and texts != '' and output_dir != '':
            exo_changer(exo_file_path, texts, output_dir)
            window['-TEXT_OUTPUT'].update('')
            window['-OUTPUT_DIR'].update('')
            window['-TEXT_FILE'].update('')

    if event == '-TEXT_FILE':
        # テキストファイルが選択されたときに内容をMultilineに表示
        text_file_path = values['-TEXT_FILE']
        print(text_file_path)
        if text_file_path:
            try:
                with open(text_file_path, 'r', encoding='UTF-8') as text_file:
                    text_data = text_file.read()
                    window['-TEXT_OUTPUT'].update(text_data)
                window['-OUTPUT_DIR'].update(os.path.dirname(text_file_path))
                
            except Exception as e:
                sg.popup_error(f'エラーが発生しました: {str(e)}', title='エラー')
window.close()