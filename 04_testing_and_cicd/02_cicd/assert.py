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
            return "assertion error"

# `contains` 用のテスト `test_contains` を作成してください
def test_contatins():
    names = ["Nick", "Lewis", "Nikos"]
    result = my_assert(contains("Nick",names)==True)
    print(result)
    
    result = my_assert(contains("Chris",names)==False)
    print(result)
    
# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    names = ["Nick", "Lewis", "Nikos"]
    names_len = len(names)    
    result = my_assert(add_name("Alice",names)=="Alice")
    print(result)
    
    result = my_assert(len(names) == names_len+1 )

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    result = my_assert(add_two(3)==5)
    print(result)
    
    result = my_assert(add_two(-2)==0)
    print(result)

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    result = my_assert(divide_by_two(4)==2)
    print(result)

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    greeting_msg = f"Hello, Ken. It is 5 degrees warmer today than yesterday"
    result = my_assert(greeting("Ken",5)== greeting_msg)
    print(result)
    

# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
