class Student: #(クラス)
    def __init__(self,name):#コンストラクタ／初期化メソッド
        self.name = name #アトリビュート定義
    def avg(self,math,english):#メソッド
        print ((math + english)/2)

a001 = Student("sato") #インスタンス化
print(a001.name)

a002 = Student("tanaka") #インスタンス化
print(a002.name)