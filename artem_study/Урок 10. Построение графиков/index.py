import pandas as pd
from sklearn.preprocessing import LabelBinarizer

# Ваш исходный код
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot формат
label_binarizer = LabelBinarizer()
one_hot_encoded = label_binarizer.fit_transform(data['whoAmI'])

# Создание DataFrame из one-hot кодированных данных
one_hot_df = pd.DataFrame(one_hot_encoded, columns=label_binarizer.classes_)

# Объединение исходного DataFrame с новым DataFrame
data = pd.concat([data, one_hot_df], axis=1)

# Вывод результатов
data.head()
