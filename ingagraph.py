import numpy as np
import pandas as pd
import graphviz
import lingam
import lightgbm as lgb
from lingam.utils import make_dot
from sklearn.linear_model import LinearRegression

print([np.__version__, pd.__version__, graphviz.__version__, lingam.__version__])

np.set_printoptions(precision=3, suppress=True)
np.random.seed(0)

x3 = np.random.uniform(size=10000)
x0 = 3.0*x3 + np.random.uniform(size=10000)
x2 = 6.0*x3 + np.random.uniform(size=10000)
x1 = 3.0*x0 + 2.0*x2 + np.random.uniform(size=10000)
x5 = 4.0*x0 + np.random.uniform(size=10000)
x4 = 8.0*x0 - 1.0*x2 + np.random.uniform(size=10000)
X = pd.DataFrame(np.array([x0, x1, x2, x3, x4, x5]).T ,columns=['x0', 'x1', 'x2', 'x3', 'x4', 'x5'])

model = lingam.DirectLiNGAM()
model.fit(X)
make_dot(model.adjacency_matrix_)

labels = [f'var{i}' for i in range(X.shape[1])]
make_dot(model.adjacency_matrix_, labels=labels)

dot = make_dot(model.adjacency_matrix_, labels=labels)

# Save pdf
dot.render('dag')

# Save png
dot.format = 'png'
dot.render('dag')
target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = LinearRegression()

reg.fit(X.iloc[:, features], X.iloc[:, target])

make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_coefs=reg.coef_)

dot2 = make_dot(model.adjacency_matrix_, labels=labels)

# Save pdf
dot2.render('dag2')

# Save png
dot2.format = 'png'
dot2.render('dag2')
target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = LinearRegression()

#make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_target_label='Target', prediction_line_color='#0000FF')
dot3 = make_dot(model.adjacency_matrix_, labels=labels)

#Save pdf
dot3.render('dag3')

#Save png
dot3.format = 'png'
dot3.render('dag3')
target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = LinearRegression()

target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = lgb.LGBMRegressor(random_state=0)
reg.fit(X.iloc[:, features], X.iloc[:, target])
reg.feature_importances_

make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_feature_importance=reg.feature_importances_)
dot4 = make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_feature_importance=reg.feature_importances_)

# Save pdf
dot4.render('dag4')

# Save png
dot4.format = 'png'
dot4.render('dag4')
target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = LinearRegression()

target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = lgb.LGBMRegressor(random_state=0)
reg.fit(X.iloc[:, features], X.iloc[:, target])
reg.feature_importances_

make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_feature_importance=reg.feature_importances_)
dot5 = make_dot(model.adjacency_matrix_, prediction_feature_indices=features, prediction_feature_importance=reg.feature_importances_)

# Save pdf
dot4.render('dag5')

# Save png
dot5.format = 'png'
dot5.render('dag5')
target = 0
features = [i for i in range(X.shape[1]) if i != target]
reg = LinearRegression()