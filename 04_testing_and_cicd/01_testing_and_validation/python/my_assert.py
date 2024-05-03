# ----これらの関数を変更する必要はありません----

names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----

# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg=None):
    if not expr:
        if msg:
            return msg
        else:
            return "AssertionError: Expression evaluated to False"

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    my_assert(contains("Nick", names) == True, "Nick should be in the list")
    my_assert(contains("Alice", names) == False, "Alice should not be in the list")

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    names_len = len(names)
    my_assert(add_name("Alice", names) == "Alice", "Failed to add Alice to the list")
    my_assert(len(names) == (names_len + 1))

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    my_assert(add_two(3) == 5, "Failed to add two to the number")

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    my_assert(divide_by_two(6) == 3.0, "Failed to divide the number by two")

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    expected_message = "Hello, John. It is 10.5 degrees warmer today than yesterday"
    my_assert(greeting("John", 10.5) == expected_message, "Failed to generate the greeting message")

# テストの実行
    test_contains()
    test_add_name()
    test_add_two()
    test_divide_by_two()
    test_greeting()