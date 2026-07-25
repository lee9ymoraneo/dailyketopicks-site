#!/usr/bin/env python3
"""
AI Content Generator for Daily Keto Picks Blog
Generates markdown blog posts for keto/health niche
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "src" / "content" / "posts"
CONFIG_DIR = Path(__file__).parent / "config"

TOPICS = {
    "keto": [
        {"title": "Ultimate Keto Meal Plan for Beginners", "keywords": ["keto meal plan", "beginner keto", "keto diet"], "category": "Meal Plans"},
        {"title": "15 Easy Keto Breakfast Recipes", "keywords": ["keto breakfast", "easy recipes", "low carb"], "category": "Recipes"},
        {"title": "What is the Keto Diet? Complete Guide", "keywords": ["keto diet", "ketogenic", "what is keto"], "category": "Keto Basics"},
        {"title": "Top 10 Keto Snacks for Weight Loss", "keywords": ["keto snacks", "weight loss", "low carb snacks"], "category": "Recipes"},
        {"title": "Keto for Beginners: Getting Started", "keywords": ["keto beginner", "getting started", "keto guide"], "category": "Keto Basics"},
        {"title": "Best Keto Foods to Buy at Grocery Store", "keywords": ["keto foods", "grocery list", "keto shopping"], "category": "Keto Basics"},
        {"title": "How to Calculate Your Keto Macros", "keywords": ["keto macros", "macro calculator", "macros guide"], "category": "Keto Basics"},
        {"title": "Keto Dinner Recipes Under 30 Minutes", "keywords": ["keto dinner", "quick recipes", "easy meals"], "category": "Recipes"},
        {"title": "Benefits of the Keto Diet", "keywords": ["keto benefits", "health benefits", "why keto"], "category": "Keto Basics"},
        {"title": "Keto Meal Prep: Weekly Guide", "keywords": ["keto meal prep", "weekly prep", "meal planning"], "category": "Meal Plans"},
        {"title": "Keto Desserts That Actually Taste Good", "keywords": ["keto desserts", "low carb sweets", "keto treats"], "category": "Recipes"},
        {"title": "How to Break a Weight Loss Plateau on Keto", "keywords": ["weight loss plateau", "keto stall", "plateau break"], "category": "Weight Loss"},
        {"title": "Keto vs Paleo: Which Diet is Better?", "keywords": ["keto vs paleo", "diet comparison", "which diet"], "category": "Keto Basics"},
        {"title": "Best Keto Supplements for Beginners", "keywords": ["keto supplements", "beginner supplements", "keto vitamins"], "category": "Keto Basics"},
        {"title": "Keto Flu: How to Prevent and Treat It", "keywords": ["keto flu", "keto symptoms", "keto side effects"], "category": "Keto Basics"},
        {"title": "10 Keto Smoothie Recipes", "keywords": ["keto smoothie", "low carb smoothie", "keto drinks"], "category": "Recipes"},
        {"title": "Keto for Women: Special Considerations", "keywords": ["keto for women", "female keto", "women health"], "category": "Keto Basics"},
        {"title": "How to Eat Out on Keto", "keywords": ["eating out keto", "restaurant keto", "keto dining"], "category": "Keto Basics"},
        {"title": "Keto Shopping List: Complete Guide", "keywords": ["keto shopping list", "grocery guide", "keto foods"], "category": "Keto Basics"},
        {"title": "Keto Weight Loss: What to Expect", "keywords": ["keto weight loss", "weight loss timeline", "keto results"], "category": "Weight Loss"},
        {"title": "Best Keto Restaurants and Chains", "keywords": ["keto restaurants", "chain restaurants", "keto friendly"], "category": "Keto Basics"},
        {"title": "Keto Intermittent Fasting Guide", "keywords": ["keto fasting", "intermittent fasting", "keto IF"], "category": "Weight Loss"},
        {"title": "Keto Pizza Recipes That Are Actually Good", "keywords": ["keto pizza", "low carb pizza", "pizza recipe"], "category": "Recipes"},
        {"title": "How to Track Your Keto Progress", "keywords": ["keto tracking", "progress tracking", "keto metrics"], "category": "Weight Loss"},
        {"title": "Keto for Athletes: Performance Guide", "keywords": ["keto athletes", "keto performance", "athletic keto"], "category": "Keto Basics"},
        {"title": "Best Keto Meal Delivery Services", "keywords": ["keto meal delivery", "meal service", "keto meals"], "category": "Meal Plans"},
        {"title": "Keto Grocery Haul: What I Buy", "keywords": ["keto grocery haul", "shopping haul", "keto foods"], "category": "Keto Basics"},
        {"title": "How to Make Keto Bread at Home", "keywords": ["keto bread", "low carb bread", "bread recipe"], "category": "Recipes"},
        {"title": "Keto for Beginners: Common Mistakes", "keywords": ["keto mistakes", "beginner errors", "keto tips"], "category": "Keto Basics"},
        {"title": "Best Keto Apps for Tracking", "keywords": ["keto apps", "tracking apps", "keto tools"], "category": "Keto Basics"},
        {"title": "Keto Meal Plan: 7-Day Sample", "keywords": ["7 day meal plan", "weekly plan", "keto menu"], "category": "Meal Plans"},
        {"title": "Keto Coffee: How to Make Bulletproof Coffee", "keywords": ["keto coffee", "bulletproof coffee", "keto drinks"], "category": "Recipes"},
        {"title": "Keto for Diabetics: What to Know", "keywords": ["keto diabetes", "diabetic keto", "blood sugar"], "category": "Keto Basics"},
        {"title": "How to Start Keto After the Holidays", "keywords": ["post holiday keto", "new year keto", "fresh start"], "category": "Keto Basics"},
        {"title": "Keto Comfort Food Recipes", "keywords": ["keto comfort food", "comfort food", "keto meals"], "category": "Recipes"},
        {"title": "Understanding Ketosis: The Science", "keywords": ["ketosis", "keto science", "how ketosis works"], "category": "Keto Basics"},
        {"title": "Keto Diet for Beginners Over 40", "keywords": ["keto over 40", "middle age keto", "older adults keto"], "category": "Keto Basics"},
        {"title": "Best Keto Meal Replacement Shakes", "keywords": ["keto shakes", "meal replacement", "keto drinks"], "category": "Meal Plans"},
        {"title": "How to Calculate Net Carbs", "keywords": ["net carbs", "carb counting", "keto carbs"], "category": "Keto Basics"},
        {"title": "Keto Success Stories: Real Results", "keywords": ["keto success", "real results", "transformation"], "category": "Success Stories"},
        {"title": "Keto Holiday Recipes Guide", "keywords": ["keto holidays", "holiday recipes", "festive keto"], "category": "Recipes"},
        {"title": "How to Stay Motivated on Keto", "keywords": ["keto motivation", "staying motivated", "keto mindset"], "category": "Weight Loss"},
        {"title": "Keto for Beginners: Week 1 Guide", "keywords": ["keto week 1", "first week keto", "starting keto"], "category": "Keto Basics"},
        {"title": "Best Keto Cookbooks Reviewed", "keywords": ["keto cookbooks", "cookbook review", "keto books"], "category": "Keto Basics"},
        {"title": "Keto Meal Prep Containers Guide", "keywords": ["meal prep containers", "keto storage", "meal prep"], "category": "Meal Plans"},
        {"title": "How to Handle Keto Cravings", "keywords": ["keto cravings", "stop cravings", "craving control"], "category": "Weight Loss"},
        {"title": "Keto for Beginners: FAQ", "keywords": ["keto faq", "keto questions", "keto answers"], "category": "Keto Basics"},
        {"title": "Best Keto Friendly Restaurants", "keywords": ["keto restaurants", "dining out", "restaurant guide"], "category": "Keto Basics"},
        {"title": "Keto Meal Plan: Budget Friendly", "keywords": ["budget keto", "cheap keto", "affordable meals"], "category": "Meal Plans"},
        {"title": "How to Use MCT Oil on Keto", "keywords": ["mct oil", "keto oil", "mct benefits"], "category": "Keto Basics"},
    ],
}


def generate_markdown(title: str, keywords: list, category: str, publish_date: str) -> str:
    tags = ", ".join(keywords[:3])

    markdown = f"""---
title: "{title}"
description: "Expert guide on {keywords[0]}. Discover tips, recipes, and advice for successful {category.lower()}."
pubDate: {publish_date}
author: "Daily Keto Picks Team"
category: "{category}"
tags: [{tags}]
---

# {title}

*Published on {publish_date} • {category}*

## Key Takeaways

- Essential information about {keywords[0]}
- Expert tips for {keywords[1]}
- Best practices for {keywords[2]}

## Introduction

Welcome to our comprehensive guide on {keywords[0]}. Whether you're new to keto or looking to optimize your approach, this guide will help you succeed.

## Understanding the Basics

Before diving in, it's important to understand the fundamentals of {keywords[0]}.

### Why It Matters

Following a ketogenic lifestyle can offer numerous benefits:

1. **Weight Loss** - Many people experience significant weight loss
2. **Mental Clarity** - Better focus and cognitive function
3. **Stable Energy** - No more energy crashes
4. **Reduced Inflammation** - Potential health benefits

### Getting Started

Here's how to begin your {keywords[0]} journey:

- Start with the basics
- Set realistic goals
- Plan your meals
- Track your progress

## Expert Tips

### Success Strategies

Follow these strategies for best results:

1. **Plan Ahead** - Meal prep is key to success
2. **Stay Hydrated** - Drink plenty of water
3. **Track Your Macros** - Know your numbers
4. **Be Patient** - Results take time

### Common Mistakes to Avoid

Many beginners make these mistakes:

- Eating too much protein
- Not eating enough fats
- Forgetting electrolytes
- Giving up too soon

## Recommended Resources

Based on our experience, here are some helpful resources:

| Resource | Why We Recommend It |
|----------|---------------------|
| Keto Calculator | Helps determine your macros |
| Meal Planning App | Makes meal prep easier |
| Food Scale | Essential for tracking |
| Keto Cookbook | Recipe inspiration |

## Conclusion

Starting your {keywords[0]} journey can be overwhelming, but with the right information and support, you can succeed. Remember to be patient with yourself and celebrate small wins along the way.

## Frequently Asked Questions

### What is {keywords[0]}?

{keywords[0]} refers to the practice of following a ketogenic diet and lifestyle to achieve health and wellness goals.

### How long does it take to see results?

Most people begin to see results within 2-4 weeks of consistent keto eating, though individual results may vary.

### Is keto safe for everyone?

While keto can be beneficial for many people, it's always best to consult with a healthcare professional before making significant dietary changes.
"""

    return markdown


def generate_batch(niche: str, count: int):
    topics = TOPICS.get(niche, TOPICS["keto"])
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    start_date = datetime(2024, 1, 15)
    end_date = datetime.now()
    total_days = (end_date - start_date).days

    generated = []
    for i in range(count):
        topic = topics[i % len(topics)]
        day_offset = int((i / count) * total_days)
        pub_date = (start_date + timedelta(days=day_offset)).strftime("%Y-%m-%d")

        filename = topic["title"].lower().replace(" ", "-").replace("'", "")
        filename = "".join(c for c in filename if c.isalnum() or c == "-")
        filename = f"{filename}.md"

        filepath = CONTENT_DIR / filename
        if filepath.exists():
            print(f"Skipping {filename} (already exists)")
            continue

        content = generate_markdown(topic["title"], topic["keywords"], topic["category"], pub_date)
        filepath.write_text(content, encoding="utf-8")

        generated.append({
            "title": topic["title"],
            "filename": filename,
            "date": pub_date,
            "category": topic["category"],
        })
        print(f"Generated: {filename}")

    log_path = CONFIG_DIR / "generation_log.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing_log = []
    if log_path.exists():
        existing_log = json.loads(log_path.read_text())
    existing_log.extend(generated)
    log_path.write_text(json.dumps(existing_log, indent=2))

    print(f"\nGenerated {len(generated)} posts")
    return generated


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate blog content for Daily Keto Picks")
    parser.add_argument("--niche", choices=["keto"], default="keto")
    parser.add_argument("--count", type=int, default=50)
    args = parser.parse_args()
    print(f"Generating {args.count} {args.niche} posts...")
    generate_batch(args.niche, args.count)


if __name__ == "__main__":
    main()
