import numpy as nm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X = nm.array([[1, 0], [2, 0], [3, 0], [6, 0], [6, 0], [7, 0], [10, 0], [11, 0]])
print("Datasets with  8 points: \n", X, "\n Size: ", len(X))
y = nm.array([0, 0, 1, 1, 1, 0, 0, 0])
print("\n Clas label for the datasets X  Y:", y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=0, shuffle=False)
print("\nTraining Data  for X: \n", x_train)
print("\n Training Data for  Y:", y_train)

stand_scalar = StandardScaler()
x_train = stand_scalar.fit_transform(x_train)
x_test = stand_scalar.transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=3)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print('\nExpected Class labels for testing the data Y:', y_pred)

confusion_matrix_result = confusion_matrix(y_test, y_pred)
print("\nThe Confusion Matrix is\n", confusion_matrix_result)


total_value = sum(sum(confusion_matrix_result))
accuracy = (confusion_matrix_result[0, 0] + confusion_matrix_result[1, 1]) / total_value
print('\nThe expected accuracy is : ', accuracy)

sensitivity = confusion_matrix_result[1, 1] / (confusion_matrix_result[1, 0] + confusion_matrix_result[1, 1])
print('The expected sensitivity is  : ', sensitivity)

specificity = confusion_matrix_result[0, 0] / (confusion_matrix_result[0, 0] + confusion_matrix_result[0, 1])
print('The expected specificity is  : ', specificity)
