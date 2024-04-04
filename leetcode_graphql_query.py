import webbrowser
import requests

url = "https://leetcode.com/graphql"

query = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    userStatus
    link
    question {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      hasVideoSolution
      hasSolution
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
data = {
    "query": query
}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    question_data = result['data']['activeDailyCodingChallengeQuestion']

    print("Question of the Day:")
    print("Date:", question_data['date'])
    print("User Status:", question_data['userStatus'])
    print("Link:", question_data['link'])
    question_details = question_data['question']
    print("Title:", question_details['title'])
    print("Difficulty:", question_details['difficulty'])
    print("Topic Tags:", [tag['name'] for tag in question_details['topicTags']])
    
    webbrowser.open(question_data['link'])
else:
    print("Failed to fetch the question of the day.")
