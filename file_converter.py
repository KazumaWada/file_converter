import sys
import os
import markdown


base_file = sys.argv[2]
result_file = sys.argv[3]
## copy ##
if sys.argv[1] == "copy":

    # base.txtの内容を変数result_txtに格納しているだけで、
    # ファイルにはまだ変更が反映されていない。
    with open(base_file, 'r') as source:
        source_temp = source.read()
        print(source_temp)  # null.空欄になっている。

    # copyするfile名を定義
    result_filename = result_file

    with open(result_filename, 'w') as result_file:
        result_file.write(source_temp)
        print(result_file)

## reverse ##
if sys.argv[1] == "reverse":
    print("reverse A B")
    with open(base_file, 'r') as source:
        source_temp = source.read()

    result_filename = result_file

    with open(result_filename, 'w') as result_file:
        # 逆にする
        reversed_txt = source_temp[::-1]
        # 逆にした結果を書き込む
        result_file.write(reversed_txt)
        print(reversed_txt)

## duplicate-contents ##
# duplicate-contents inputpath n
if sys.argv[1] == "duplicate-contents":
    # result.txtは使われないからずらす

    with open(base_file, 'r') as source:
        source_temp = source.read()

    result_filename = base_file

    with open(result_filename, 'w') as base_file:
        duplicated_txt: str = ''

        # sys.argvはstrとして定義されているから
        count = int(sys.argv[3])
        while count > 0:
            duplicated_txt += source_temp
            count -= 1
        # 結果を書き込む
        base_file.write(duplicated_txt)
        print(duplicated_txt)


# replace-string inputpath needle newstring
# baseにある文字列"needle"を"newstring"に変える
if sys.argv[1] == "replace-string":
    search_string = sys.argv[3]
    replace_string = sys.argv[4]

    with open(base_file, 'r') as source:
        source_temp = source.read()

    result_filename = base_file

if search_string in source_temp:

    replaced_string_txt = source_temp.replace(search_string, replace_string)
    with open(base_file, 'w') as output_file:
        output_file.write(replaced_string_txt)
        print(f"string replaced '{search_string}' to '{replace_string}'")
else:
    print("not found")
