def insert_items(lst, entry, elem):
    it = iter(lst)
    for i in range(len(lst)-1):
        if next(it) == entry:
            lst.insert(i+1, elem)
    if lst[-1] == entry:
        lst.append(elem)
    return lst

double_lst = [1, 2, 1, 2, 3, 3]
double_lst = insert_items(double_lst, 3, 4)
print(double_lst)

r = range(6)
r_iter = iter(r)

r_2 = r_iter
print(next(r_iter))
print(next(r_2))



r_3 = r_iter
print(list(r_3))

class A:
    time = 1
    def __init__(self,argument):
        self.arg = argument

try:
    a = A(10)
    a.time=2
except TypeError as e:
    print(A.time, a.time,a.arg)
    


from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV, train_test_split

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 定义模型
model = svm.SVC()

# 定义参数网格
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001, 0.0001], 'kernel': ['linear', 'rbf']}

# 创建网格搜索对象
grid_search = GridSearchCV(model, param_grid, cv=5)

# 进行参数调整
grid_search.fit(X_train, y_train)

# 输出最佳参数和得分
print("最佳参数:", grid_search.best_params_)
print("最佳得分:", grid_search.best_score_)

# 在测试集上评估模型
best_model = grid_search.best_estimator_
accuracy = best_model.score(X_test, y_test)
print("在测试集上的准确度:", accuracy)
