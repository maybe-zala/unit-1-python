print("""How's My Grades Looking? 
      
Class: Pre-Law (Criminal)

Assignments:

| Assignment            | Weight |
| --------------------- | ------ |
| Crime Study           | 5%     |
| Case Evaluation       | 5%     |
| Negotiation Practice  | 10%    |
| Case Study Project    | 20%    |
| Crimimology Report    | 5%     |
| Legal Doc Analysis    | 5%     |
| Case Brief            | 10%    |
| Professional Report   | 10%    |
| Mock Trial            | 30%    |
""")

grade_so_far = 0
points_available = 0

crime_study = int(input("What did you make on your Crime Study? [0-100]: "))
grade_so_far += crime_study / 100 * 5
points_available += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

case_evaluation = int(input("What did you make on your Case Evaluation? [0-100]: "))
grade_so_far += case_evaluation / 100 * 5
points_available += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

negotiation_practice= int(input("What did you make on your Negotiation Practice? [0-100]: "))
grade_so_far += negotiation_practice / 100 * 10
points_available += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

case_study_project = int(input("What did you make on your Case Study Project? [0-100]: "))
grade_so_far += case_study_project / 100 * 20
points_available += 20
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

criminology_report = int(input("What did you make on your Criminology Report? [0-100]: "))
grade_so_far += criminology_report / 100 * 5
points_available += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

legal_doc_analysis = int(input("What did you make on your Legal Doc Analysis? [0-100]: "))
grade_so_far += legal_doc_analysis / 100 * 5
points_available += 5
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

case_brief = int(input("What did you make on your Case Brief? [0-100]: "))
grade_so_far += case_brief / 100 * 10
points_available += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

professional_report = int(input("What did you make on your Professional Report? [0-100]: "))
grade_so_far += professional_report / 100 * 10
points_available += 10
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")

mock_trial = int(input("What did you make on your Mock Trial? [0-100]: "))
grade_so_far += mock_trial / 100 * 30
points_available += 30
print(f"Worst Possible: {grade_so_far}")
print(f"Best Possible: {(100 - points_available + grade_so_far)}")
