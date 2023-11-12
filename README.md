# Customer Segmentation using RFM Modeling and K-means Clustering
Welcome to the Customer Segmentation project repository! This project utilizes RFM (Recency, Frequency, Monetary) modeling and K-means clustering to enhance customer segmentation. Additionally, a clustomate web app has been developed using Streamlit, hosted on the Streamlit Community for accessibility.

# Project Overview
# RFM Modeling Enhancement
I addressed a common issue with RFM modeling, where it could be biased in segmenting customers into silver and gold categories. By rectifying this bias, the RFM model now accurately distinguishes between high-value and low-value customers within the same segment, such as standard and elite.

# K-means Clustering Expansion
Incorporating K-means clustering with siloed scores revealed new customer patterns. The initial loyalty levels (platinum, gold, silver, bronze) were expanded to include  gold standard, gold elite, silver standard and silver elite. This comprehensive segmentation results in six distinct customer segments.

# Web App Features
The web app provides a holistic view of customer segmentation, offering:

**RFM Loyalty Levels:** The traditional loyalty levels derived from RFM modeling, providing insights into customer behavior based on recency, frequency, and monetary values.

**K-means Clustering:** Utilizing K-means clustering, customers are categorized into two clusters (0 and 1), uncovering additional patterns beyond the conventional loyalty levels.

**Enhanced RFM Version:** The web app combines RFM loyalty levels and K-means clustering results to present an enhanced version of loyalty, including gold elite, gold standard, silver elite, silver standard, and more.

# Model Utilization in Web App

The web app incorporates two predictive models:

**Logistic Regression:** Predicts the cluster ID for each customer based on their characteristics.

**Random Forest Classifier:** Predicts customer loyalty levels, enhancing the understanding of customer behavior.

Visit the hosted web app on the Streamlit Community to explore the enhanced RFM segmentation and gain valuable insights into customer behavior.
**App URL :** https://clustomate.streamlit.app/

Feel free to contribute, report issues, or provide feedback. Happy segmenting!


