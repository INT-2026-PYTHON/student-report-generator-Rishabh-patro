"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def generate_report(records):

    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    topper = top_scorer(records)
    passed = passing_students(records)

    report = ""

    report += f"Total Records: {len(records)}\n"
    report += f"Subjects Offered: {subjects}\n\n"

    report += "Average Scores:\n"

    for name in sorted(averages):
        report += f"{name}: {averages[name]}\n"

    report += f"\nTop Scorer: {topper[0]} ({topper[1]})\n"
    report += f"Passing Students: {passed}"

    return report

    
    pass
