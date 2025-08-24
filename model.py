from sklearn.linear_model import
LogisticRegression

x = [[0,0],[1,1]]
y = [0,1]

model = LogisticRegression().fit(x, y)
print("Model trained. Coefficients:", model.coef_)