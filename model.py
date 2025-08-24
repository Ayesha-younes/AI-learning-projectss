from sklearn.linear_model import
LogisticRegression

#Expanded dataset
x = [[0,0],[1,1],[1,0],[0,1]]
y = [0,1,1,0]

#Tuned Logistic Regression
model = LogisticRegression(max_iter=200,solver="liblinear").fit(x, y)
print("Model trained. Coefficients:",model.coef_)
print("Model intercept:", model.intercept_)