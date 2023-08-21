# ユーザーからテキスト入力を受け取り、
# 文字列内の文字と出現回数をマッピングする
# 辞書を作成するスクリプトを記述してください。次に例を示します。
#
# user_input = "hello"
# result = {"h":1, "e":1, "l":2, "o":1}
user_input = input()
result = {}
for char in user_input:
    if not char in result:
        result[char] = 1
    else:
        result[char] += 1