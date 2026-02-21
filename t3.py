# 計算
args1 = input("引数1つ目を入力してください")
args2 = input("引数２つ目を入力してください")

try:
    result = int(args1) + int(args2)
    print(f"結果：{result}")
except ValueError:   
    print("エラーが発生しました")
    print("有効な数字を入力してください")
except Exception as e:
    print("エラーが発生しました")
finally:
    print("処理を終了しました")

