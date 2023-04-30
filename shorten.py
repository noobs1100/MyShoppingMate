

import json
import openai
openai.api_key = "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"

# Open the input file and parse the JSON data
with open('reviews.json', 'r') as f:
    reviews = json.load(f)

# Iterate through each review and generate a summary
for review in reviews:
    text = review 
    prompt = f"Summarize the following review: {text}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50
    )
    summary = response.choices[0].text.strip()
    review['summary'] = summary

# Save the summarized reviews to a new JSON file
with open('summarized_reviews.json', 'w') as f:
    json.dump(reviews, f)
