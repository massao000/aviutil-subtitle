import os, re
from binascii import hexlify, b2a_hex
from glob import glob
import wave

def exo_changer(exo_tmp, text, output_exo_path, wavs):
    """_summary_

    Args:
        exo_tmp (_type_): exofile
        text (_type_): テキスト
        output_exo_path (_type_): 出力場所
        wavs (_type_): 音声ファイルの場所
    """

    exedit = {}
    zero = {}
    # 現在のセクションの文字列をそのまま入れます。
    currentsection = "exedit"
    originalstart = 0
    originalend = 0
    sectionsnum = 0
    with open(exo_tmp, mode='r', encoding='shift_jis') as f:
        for line in f:
            m = re.match(r'\[([^\]]+)',line)
            if m:
                if m.group(1) != "exedit":
                    currentsection = m.group(1)
                    mm = re.match(r'^\d+$',m.group(1))
                    if mm:
                        sectionsnum = int(currentsection)
            elif re.match(r'[^\r\n\s]',line):
                kv = line.split('=',1)
                if currentsection == "exedit":
                    exedit[kv[0]] = kv[1]
                else:
                    if currentsection not in zero:
                        zero[currentsection] = {}
                    zero[currentsection][kv[0]] = kv[1]
                    if kv[0] == 'start':
                        if (currentsection == 0):
                            originalstart = int(kv[1])
                    elif kv[0] == 'end':
                        originalend = int(kv[1])
                        
    texts = text.split('\n')

    # 使用例
    wav_info_dict = create_wav_info_dict(wavs)
    keys = list(wav_info_dict.keys())
    
    sectionsnum = sectionsnum + 1
    sectioncount = 0
    deltaframes = originalend-originalstart
    startpos = originalstart
    currentsection = 0

    with open(f'{output_exo_path}\\jimaku.exo', 'w', encoding='shift_jis') as f2:
        output_str = "[exedit]\n"
        f2.write(output_str)
        for k,v in exedit.items():
            # print(f"{k:s}={v:s}",end="")
            output_str = f"{k:s}={v:s}"
            f2.write(output_str)
            
        hex_padding = "0000" * (4096 // 4)  # Paddingを事前に生成

        for num, text in enumerate(texts):
            # print(text)
            try:
                first_key = keys[num]
                first_value = wav_info_dict[first_key]
                audio_file_path = first_value['file_path']
                duration = first_value['duration']
            except:
                audio_file_path = ''
                duration = 100
            
            for k, v in zero.items():
                
                m = re.match(r'^\d+$', k)
                if m:
                    currentsection = sectioncount + int(k)
                    output_str = f"[{currentsection:d}]\n"

                    for vk, vv in v.items():
                        if vk == "start":
                        # if vk == "start" or vk == "end":
                            output_str += f"{vk:s}={startpos + int(vv)}\n"
                        elif vk == "end":
                            output_str += f"{vk:s}={startpos + duration}\n"
                        else:
                            output_str += f"{vk:s}={vv:s}"

                    f2.write(output_str)
                    # print(output_str)
                else:
                    sectionname = re.sub(r'^\d+', str(currentsection), k)
                    output_str = f"[{sectionname:s}]\n"

                    for vk, vv in v.items():
                        if vk == "text":
                            text_in_utf16 = b2a_hex(text.encode('utf-16')).decode("ascii")[4:]
                            output_str += f"text={text_in_utf16}{hex_padding[len(text_in_utf16):]}\n"
                        elif vk == "file":
                            output_str += f"file={audio_file_path}\n"
                        else:
                            output_str += f"{vk:s}={vv:s}"

                    f2.write(output_str)
                    # print(output_str)
                

            sectioncount += sectionsnum
            # startpos += deltaframes + 18
            startpos += duration + 18
            print(startpos)

def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate) * 60
        return int(duration)


def create_wav_info_dict(directory_path):
    wav_files = glob(directory_path + '/*.wav')  # ディレクトリ内のWAVファイルを取得

    wav_info_dict = {}  # ファイルパスと長さを格納する辞書

    for idx, wav_file in enumerate(wav_files, start=1):
        duration = get_wav_duration(wav_file)
        key = f"{idx}"  # 連番をキーに追加
        wav_info_dict[key] = {"file_path": wav_file, "duration": duration}

    return wav_info_dict


# if __name__ == "__main__":
#     x = 'testread.exo'
#     textfile = "冷たい冬の日、私は君と出会った。\n雪が降る中、君の笑顔はまるで暖かな陽だまり。\n一緒に歩きながら、君は言った。\n「雪の結晶みたいに、君との瞬間が特別なんだ」\nその言葉が心に染み入り、君との冒険が始まった。\n雪が降り積もる中、二人は互いに寄り添い、\n細やかな気遣いで心を通わせた。\nそして、冬が終わりを告げる頃、\n君の言葉が空気に溶けて、愛の温もりが残る。"
#     z = 'D:/program/python/myapp/aviutil_text/31雪の結晶、君の笑顔ok'
#     exo_changer(x, textfile, z)