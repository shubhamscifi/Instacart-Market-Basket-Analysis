# [Instacart-Market-Basket-Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/)  <a href="https://www.linkedin.com/in/me-shubham-agrawal"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" width="45" height="45" align="right" /></a>


<img src="https://github.com/shubhamscifi/Instacart-Market-Basket-Analysis/blob/main/Best%20F1-Score.png"/><br>
  *The score is very close to the competition's winner's score i.e. 0.409 . [Competition Leaderboard](https://www.kaggle.com/c/instacart-market-basket-analysis/leaderboard)
  
* **Tech and Algo used:** Auto-Encoder, Logistic-Regression, Decision Tree, Random-Forest, AdaBoost, Gradient Boosting, Feature-Engineering, Python, Tensorflow, Pandas, Sklearn, Matplolib, Seaborn, Plotly.

- Open repo in [VS Code Online](https://github.dev/shubhamscifi/Instacart-Market-Basket-Analysis).

# **Problem Overview:**

**Goal:** Predict which products will an Instacart consumer purchase again.

1. Instacart is a grocery ordering and delivery app.
2.   Currently they use transactional data to develop models that predict which products a user will buy again, try for the first time, or add to their cart next during a session.
3.    The **goal** is to **predict which previously purchased products will be in a user’s next order.**
4. For each orderid in the test set, we should predict a space-delimited list of product ids for that order.
5. Predict an explicit 'None' value for orders with no reordered items.
6. In the data provided, over 3 million grocery orders are present.
7. More than 200,000 Instacart users.
8. For each user, instacart provided between 4 and 100 of their orders in the dataset, with the sequence of products purchased in each order.

## Key Takeaways:
- Reorder of a product by a user highly depends on the frequency and recency of past purchases.
- Fruits and Vegetables are reordered much more than any other product.
- Personal Care products are reordered very less.
- **Gradient Boosting** gave the best result for the dataset.
- **Probability Calibration** was needed since the dataset was highly imbalanced.

## Top 10 Feature Engineering:
1. **purchase_weight_order_up:** Weight of user-product pair based on frequency of purchase and recency(order) of purchase.
2. **reorder_weight_order_up:** Weight of user-product pair based on frequency of reorder and recency(order) of reorder.
3. **#orders_since_last_purchase_up:** No. of orders placed by the user after his/her last purchase of the given product.
4. **#reorders_in_last_3_orders_up:** No. of times user has reordered the given product in his/her last 3 orders.
5. **purchase_weight_days_up:** Weight of user-product pair based on frequency of purchase and recency(days) of purchase.
6. **#purchases_in_last_3_orders_up:** No. of times user has purchased the given product in his/her last 3 orders.
7. **p(reorder|user,product)_up:** (#orders where given product was rerodered by user) / (Total #orders by user)
8. **p(reorder|product)_p:** (#reorders of product p) / (#purchases of product p)
9. **exceed_in_max_lifetime_orders_up:** No. of orders placed after the last purchase of the given product by the user - Max no. of orders after which user u purchased product p in past.
10. **days_since_last_purchase_up:** No. of days passed after the last purchase of the given product by the user.

Click [here](https://www.kaggle.com/dataset/e3851032f9eb1cae54f06fc256d7608a5ea6629c4a55438458e75bb220c56494) to download the dataset with all the **96 engineered features**.

Description of data provided by Kaggle: [Link](https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b#file-data_description-md)

If you find this helpful, please do **star the repo.**

## You can find me on <a href="https://www.linkedin.com/in/me-shubham-agrawal"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" width="17" height="17" /></a>
