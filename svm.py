#load the important packages
from sklearn.datasets import load_breast_cancer 
import matplotlib.pyplot as plt 
from sklearn.SVM import SVC
from sklearn.SVM import SVC

#load the dataset
cancer=load_breast_cancer()
X=cancer .target
Y=cancer .target

#build the model
SVM=SVC(kernel='rbf',gamma=0.5,C=1.0)

#train the model
SVM.fit(X,Y)

#plot the decision boundary
DecisionBoundaryDisplay.from_estimator(SVM,x,response_method='pre' \

#scatter plot the data points
plt.scatter(x[1:,0],X[:,1],C=Y,s=20,edgecolor="k")
plt.title("SVM Decision Boundary")
plt.show():
