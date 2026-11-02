# PRACTICAL NO. 09
# AIM: To implement Apriori and generate association rules using support and confidence.

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ['Milk', 'Bread'],
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Butter'],
    ['Milk', 'Bread', 'Butter']
]

te = TransactionEncoder()
encoded_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(encoded_data, columns=te.columns_)

print("Transaction Data:")
print(df)

frequent_itemsets = apriori(
    df,
    min_support=0.4,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Compatibility with mlxtend versions that require num_itemsets.
try:
    rules = association_rules(
        frequent_itemsets,
        num_itemsets=len(df),
        metric="confidence",
        min_threshold=0.6
    )
except TypeError:
    rules = association_rules(
        frequent_itemsets,
        metric="confidence",
        min_threshold=0.6
    )

print("\nAssociation Rules:")
if rules.empty:
    print("No association rules found.")
else:
    print(rules[['antecedents', 'consequents', 'support', 'confidence']])
