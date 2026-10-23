# Laurent Munsi Bondo
# October 19,2026
# P4HW1_Laurent Munsi Bondo
# Write a program that asks the user to collect score using a loop.

def get_letter_grade(average):
    """Determines the letter grade based on a standard grading scale."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # 1. Ask the user for the total number of scores
    num_scores = int(input("How many scores do you want to enter? "))
    print()  # Empty line for formatting
    
    scores = []
    i = 1
    
    # 2. Collect and validate input scores
    while i <= num_scores:
        try:
            score = float(input(f"Enter score #{i}: "))
            
            # Check if the score is within the valid range
            if 0 <= score <= 100:
                scores.append(score)
                i += 1
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                # Prompt to re-enter the specific invalid score
                while True:
                    retry_score = float(input(f"Enter score #{i} again: "))
                    if 0 <= retry_score <= 100:
                        scores.append(retry_score)
                        i += 1
                        break
                    else:
                        print("\nINVALID Score entered!!!!")
                        print("Score should be between 0 and 100")
        except ValueError:
            print("Please enter a valid numeric value.")

    print()  # Empty line before results
    
    # 3. Calculate statistics
    lowest_score = min(scores)
    
    # Create the modified list by removing the first occurrence of the lowest score
    modified_list = scores.copy()
    modified_list.remove(lowest_score)
    
    # Calculate average of the modified list
    if modified_list:
        scores_average = sum(modified_list) / len(modified_list)
    else:
        scores_average = 0.0
        
    grade = get_letter_grade(scores_average)
    
    # 4. Display formatted Results
    print("-------------------Results-------------------")
    print(f"Lowest Score   : {lowest_score}")
    print(f"Modified List  : {modified_list}")
    print(f"Scores Average: {scores_average:.2f}")
    print(f"Grade          : {grade}")
    print("---------------------------------------------")

if __name__ == "__main__":
    main()
