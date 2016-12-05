def convert(path):
    file = open("sample.srt", encoding="utf8")
    lines = [line for line in file]
    file.close()

    flag = False
    index = 1
    output = ['WEBVTT FILE','\n','\n']
    for token in lines:
        try:
            if int(token) == index:
                flag = True
                output.append(token)
                index += 1
        except ValueError:
            if flag:
                flag = False
                token = token.replace(',', '.')
            output.append(token)


    oFile = open("subs.vtt",'w+', encoding="utf8")
    oFile.writelines(output)
    oFile.close()

convert("k")