import json

num = int(input())

comments = {}
for _ in range(num):
    comment_json = input()
    comment = json.loads(comment_json)
    problem_id = comment['Problem_ID']
    star = comment['Star']
    comment_text = comment['Comments']
    
    if problem_id not in comments:
        comments[problem_id] = []
    
    comments[problem_id].append((star, comment_text))

average_all = sum(sum(star for star, _ in prob_comments) / len(prob_comments) for prob_comments in comments.values()) / len(comments)

final_comments = []

for problem_id, prob_comments in sorted(comments.items()):
    average_prob = sum(star for star, _ in prob_comments) / len(prob_comments)
    
    if average_prob < average_all:
        selected_comment = min(prob_comments, key=lambda x: x[0])
    else:
        selected_comment = max(prob_comments, key=lambda x: x[0])
    
    
    final_comments.append((problem_id,  average_prob, selected_comment[1]))
    
csv_str = "Problem_ID;Star;Comment\n"
csv_str += "\n".join(f"{problem_id};{average_prob:.2f};{comment}" for problem_id, average_prob, comment in final_comments)

print(csv_str)