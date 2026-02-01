import random
from typing import List, Dict, Optional

random.seed(42)

ITEMS = [
    {"id": 1, "name": "Smart Watch", "category": "Technology", "price": 120, "gender_neutral": True},
    {"id": 2, "name": "Water Bottle", "category": "Accessories", "price": 10, "gender_neutral": True},
    {"id": 3, "name": "Pizza", "category": "Food", "price": 15, "gender_neutral": True},
    {"id": 4, "name": "Fiction Book", "category": "Entertainment", "price": 12, "gender_neutral": True},
    {"id": 5, "name": "Laptop", "category": "Technology", "price": 900, "gender_neutral": True},
    {"id": 6, "name": "Ring", "category": "Accessories", "price": 250, "gender_neutral": False},
    {"id": 7, "name": "KeyChain", "category": "Accessories", "price": 30, "gender_neutral": True},
    {"id": 8, "name": "Stickersheet", "category": "Entertainment", "price": 5, "gender_neutral": True},
    {"id": 9, "name": "Bread", "category": "Food", "price": 10, "gender_neutral": True},
    {"id": 10, "name": "Smart Phone", "category": "Technology", "price": 100, "gender_neutral": True},
    {"id": 11, "name": "Film", "category": "Entertainment", "price": 50, "gender_neutral": True},
]

# recommendation logic
def recommend_items(
    session_context: Optional[Dict] = None,
    seen_items: Optional[List[int]] = None,
    top_k: int = 3
) -> List[Dict]:
    session_context = session_context or {} # represents minimal session level signals eg preferred category
    seen_items = set(seen_items or []) # list of items already shown to user

    preferred_category = session_context.get("preferred_category")
    scored_items = []

    for item in ITEMS:
        if item["id"] in seen_items:
            continue  # Prefer unseen items
        score = 0
        reasons = []

        # Coldstart heuristics
        if item["price"] <= 50:
            score += 2
            reasons.append("affordable for first-time users")

        if item["gender_neutral"]:
            score += 1
            reasons.append("suitable for a broad audience")

        # Minimal session-level personalization
        if preferred_category and item["category"] == preferred_category:
            score += 3
            reasons.append("related to what you viewed")

        # Light exploration
        score += random.uniform(0, 1)

        scored_items.append({
            "item_id": item["id"],
            "name": item["name"],
            "category": item["category"],
            "score": round(score, 2),
            "explanation": build_explanation(reasons)
        })

    ranked_items = sorted(scored_items, key=lambda x: x["score"], reverse=True)
    return ranked_items[:top_k]


def build_explanation(reasons: List[str]) -> str:
    if not reasons:
        return "Recommended as a popular choice for new users."
    return "Recommended because it is " + ", ".join(reasons) + "."


if __name__ == "__main__":

    print("=== Cold Start (No User Data) ===")
    recommendations = recommend_items()
    for r in recommendations:
        print(f"- {r['name']} ({r['category']}): {r['explanation']}")

    print("\n=== Minimal Session Context (Viewed Technology) ===")
    session = {"preferred_category": "Technology"}
    seen = [1]  

    recommendations = recommend_items(session_context=session, seen_items=seen)
    for r in recommendations:
        print(f"- {r['name']} ({r['category']}): {r['explanation']}")
