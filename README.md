# 🍏 Food Healthiness Predictor (KNN-based Algorithm) 🍏

Welcome to the **Food Healthiness Predictor**, a machine learning-based tool that predicts whether a food is **healthy** or **unhealthy** based on its nutritional features. This implementation uses the **K-Nearest Neighbors (KNN)** algorithm to make the predictions.

---

## 📊 Algorithm Overview

The algorithm utilizes **K-Nearest Neighbors (KNN)**, a popular and simple machine learning method. In KNN, the healthiness of a given food item is determined based on the majority label of its `k` nearest neighbors in the feature space. The algorithm compares the nutritional values (such as fat, sugar, fiber, and vitamins) of the food being tested with other food items in the dataset. Then, the algorithm assigns a label (healthy or unhealthy) based on the features of the nearest foods.

---

## 🔍 Why KNN for This Problem?

The **KNN algorithm** works well here due to the relatively clear correlation between food features and their healthiness. Some correlations include:

- **High fat** levels typically make food less healthy 🧈.
- **Low sugar** levels are linked to healthier foods 🍭.
- **High fiber** content is associated with better health 🌾.
- **Higher protein** is usually better for muscle growth and overall health 🍗.

The algorithm relies on these clear relationships to classify foods as either healthy or unhealthy based on the similarity of their features and so far it has shown **an accuracy of %98** during tests. However, **KNN might not perform well** when we are dealing with datasets with weak or uncertain correlations between their features, such as predicting people's genders based on their ages, the two features have almost 0 correlations.

---

## 🥗 foods.py – A Dictionary of Foods

The **foods.py** file contains a collection of food items stored as dictionaries. These dictionaries have the following features:

- **salt** (g/100g)
- **sugar** (g/100g)
- **fat** (g/100g)
- **protein** (g/100g)
- **fiber** (g/100g)
- **vitamin** (mg/100g)

These foods are imported into **main.py**, and different food items can be assigned to the `tests` variable to check their healthiness.

---

## ⚠️ Limitations & Disclaimer

Please note that this algorithm is a **work-in-progress** and should NOT be considered an optimum or accurate nutritionist tool. Here are some important points:

- **Small Dataset**: The training dataset contains data for only **100 foods**, which is not enough for a robust, fully intelligent model. The data used is **AI-generated** and not from real-world sources.
- **Feature Selection**: Only **obvious nutritional features** were chosen for simplicity. This limitation impacts the algorithm's ability to produce highly accurate predictions in more complex scenarios.
- **Example Limitations**:
  - **Coca-Cola**: Due to its low fat and salt content, the algorithm might label it as "healthy". 🥤❌
  - **Yogurt**: Although yogurt is generally healthy, the algorithm might incorrectly classify it as "unhealthy" due to its high fat content and low fiber. 🥛❌

### 🚨 Important Reminder
This algorithm is not a replacement for expert dietary advice. It is intended for **educational purposes** and **exploration of basic machine learning concepts** only.

---

## 📈 Visualizations

The script uses **matplotlib** to create scatter plots of the dataset, with food items color-coded as **green (healthy)** or **red (unhealthy)**. You can visually inspect how the foods are distributed in relation to their nutritional values like fat and sugar and you might even customize the graphs according to your own favor.

---

## 🛠️ How to Use

1. **Install Dependencies**: 
   - Ensure you have the necessary libraries: `pandas` and `matplotlib`.
   
2. **Set Test Samples**: 
   - Modify the `tests` variable in **main.py** to include the food items you want to test.

3. **Run the Script**: 
   - Simply run **main.py**, and it will predict the healthiness of the foods in your `tests` variable!

---

Happy coding! 🍎
