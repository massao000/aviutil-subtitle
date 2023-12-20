import os, re
from binascii import hexlify, b2a_hex


def exo_changer(exo_tmp, text, output_exo_path):
    """_summary_

    Args:
        exo_tmp (_type_): exofile
        text (_type_): テキスト
        output_exo_path (_type_): 出力場所
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

        for text in texts:
            print(text)
            # for k, v in filtered_items:
            for k, v in zero.items():
                
                m = re.match(r'^\d+$', k)
                if m:
                    currentsection = sectioncount + int(k)
                    output_str = f"[{currentsection:d}]\n"

                    for vk, vv in v.items():
                        if vk == "start" or vk == "end":
                            output_str += f"{vk:s}={startpos + int(vv):d}\n"
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
                        else:
                            output_str += f"{vk:s}={vv:s}"

                    f2.write(output_str)
                    # print(output_str)
                

            sectioncount += sectionsnum
            startpos += deltaframes
            
if __name__ == "__main__":
    x = 'D:\\YouTube\\裏路地朗読茶房\\Tmp\\mojitest.exo'
    textfile = "暑い夏の日、街は静まりかえっていた。 \n彼女は仕事の疲れを感じながらも、\nスーパーの冷やかしコーナーで冷たいジュースを手に入れた。\n会計待ちの列で目に入ったのは、焦げ茶の制服を着た老紳士。\n彼が小銭を見つけて手に取り、主人公は心の底から微笑む。\nそして、ジュースを差し出す瞬間、老紳士は驚きと共に笑顔を返した。\n瞬く間に広がる温かい雰囲気。\n広がる日常が、いくつかの細やかな出来事から優しさに満ちた特別な瞬間に変わった。"
    z = 'script'
    exo_changer(x, textfile, z)