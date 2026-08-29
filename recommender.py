"""
recommender.py
----------------
Core logic for RazorGrow AI.

This module analyzes which products are frequently bought TOGETHER by
customers (a technique called "market basket analysis" / co-purchase
analysis). Based on this, it recommends upsell (higher-value related
item) and cross-sell (complementary item) suggestions for merchants.

No external AI API key is required, so this works fully offline and is
free to run and demo.
"""

import pandas as pd
from collections import defaultdict


def load_data(path="data/sample_data.csv"):
    """Load the merchant transaction data."""
    return pd.read_csv(path)


def build_co_purchase_map(df: pd.DataFrame):
    """
    Build a mapping of: product -> {other_product: times_bought_together}

    This groups all purchases by customer, then looks at every pair of
    products a customer bought, and counts how often each pair occurs
    across all customers.
    """
    co_map = defaultdict(lambda: defaultdict(int))

    grouped = df.groupby("customer_id")["product_bought"].apply(list)

    for products in grouped:
        unique_products = list(set(products))
        for i, p1 in enumerate(unique_products):
            for p2 in unique_products:
                if p1 != p2:
                    co_map[p1][p2] += 1

    return co_map


def get_recommendations(product: str, co_map: dict, df: pd.DataFrame, top_n=3):
    """
    Given a product the customer is currently buying, return the top_n
    products most frequently bought alongside it -- split into:
      - cross_sell: cheaper/complementary items
      - upsell: pricier related items
    """
    if product not in co_map:
        return {"cross_sell": [], "upsell": []}

    related = sorted(co_map[product].items(), key=lambda x: x[1], reverse=True)
    related = related[:top_n]

    price_lookup = df.drop_duplicates("product_bought").set_index("product_bought")["price"].to_dict()
    current_price = price_lookup.get(product, 0)

    cross_sell, upsell = [], []
    for prod, count in related:
        entry = {
            "product": prod,
            "price": price_lookup.get(prod, 0),
            "times_bought_together": count,
        }
        if price_lookup.get(prod, 0) >= current_price:
            upsell.append(entry)
        else:
            cross_sell.append(entry)

    return {"cross_sell": cross_sell, "upsell": upsell}


def generate_pitch(product: str, recs: dict):
    """
    Generate a simple, friendly conversational recommendation message --
    the 'conversational purchase assistance' part of the project.
    """
    lines = []
    for item in recs.get("upsell", []):
        lines.append(
            f"Customers who bought **{product}** often upgraded to "
            f"**{item['product']}** (₹{item['price']}) — consider bundling this as a premium option."
        )
    for item in recs.get("cross_sell", []):
        lines.append(
            f"**{item['product']}** (₹{item['price']}) pairs well with **{product}** — "
            f"suggest it at checkout to increase basket size."
        )
    if not lines:
        lines.append(f"Not enough purchase history yet to recommend pairings for {product}.")
    return lines
