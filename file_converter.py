import sys
import os
import markdown

first_hint = """
##USAGE##

% reverse inputpath outputpath
% copy inputpath outputpath
% duplicate-contents inputpath n
% replace-string inputpath needle newstring

"""
second_hint = "\033[92minputpath is always 'base.txt'\033[0m"

hint = f"{first_hint}{second_hint}"


# if sys.argv[1] == "copy" or sys.argv[1] == "reverse" or sys.argv[1] == "duplicate-contents" or sys.argv[1] == "replace-string":
# sys.argv[1] validation
if sys.argv[1] not in ["copy", "reverse", "duplicate-contents", "replace-string"] and sys.argv[2] != "base.txt":
    print(hint)
else:
    command = sys.argv[1]
    base_file = sys.argv[2]
    result_file = sys.argv[3]

    ## copy ##
    # copy inputpath outputpath
    if command == "copy" and base_file == "base.txt" and sys.argv[3]:

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
    elif command == "reverse" and base_file == "base.txt" and sys.argv[3]:
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
    elif command == "duplicate-contents" and base_file == "base.txt" and sys.argv[3].isdigit():

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
    elif command == "replace-string":
        search_string = sys.argv[3]
        replace_string = sys.argv[4]

        with open(base_file, 'r') as source:
            source_temp = source.read()

        result_filename = base_file

        if search_string in source_temp:
            replaced_string_txt = source_temp.replace(
                search_string, replace_string)
            with open(base_file, 'w') as output_file:
                output_file.write(replaced_string_txt)
            print(f"string replaced '{search_string}' to '{replace_string}'")
        else:
            print("string not found in base.txt")

    else:
        print(hint)
