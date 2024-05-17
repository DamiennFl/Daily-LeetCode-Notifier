import webbrowser
import requests

url = "https://leetcode.com/graphql"

query = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    question {
      difficulty
      status
      title
      topicTags {
        name
        id
        slug
      }
    }
  }
}
"""
headers = {
    "Content-Type": "application/json",
}
data = {"query": query}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    question_data = result["data"]["activeDailyCodingChallengeQuestion"]

    # Get info
    question_details = question_data["question"]
    file1 = open("daily_question.txt", "w")
    date = question_data["date"]
    title = question_details["title"]
    difficulty = question_details["difficulty"]
    topic_tags = [tag["name"] for tag in question_details["topicTags"]]

    # print to file
    L = [
        f"Date: {date}\n",
        f"Title: {title} \n",
        f"Difficulty: {difficulty} \n",
        f"Topic Tags: {topic_tags} \n",
    ]

    print(L)
    file1.writelines(L)
else:
    print("Failed to fetch the question of the day.")
