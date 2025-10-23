#!/usr/bin/env python3
"""
GPA Calculator
This program calculates your GPA based on courses and grades you input.
"""

def get_grade_point(grade):
    """Convert letter grade to grade point."""
    grade_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_scale.get(grade.upper(), None)

def calculate_gpa(courses):
    """Calculate GPA from list of courses."""
    if not courses:
        return 0.0
    
    total_points = 0.0
    total_credits = 0.0
    
    for course in courses:
        grade_point = get_grade_point(course['grade'])
        credits = course['credits']
        total_points += grade_point * credits
        total_credits += credits
    
    return total_points / total_credits if total_credits > 0 else 0.0

def main():
    """Main function to run the GPA calculator."""
    print("=" * 50)
    print("GPA CALCULATOR")
    print("=" * 50)
    print("\nThis program will calculate your GPA based on your courses and grades.")
    print("\nGrade Scale:")
    print("  A = 4.0")
    print("  B = 3.0")
    print("  C = 2.0")
    print("  D = 1.0")
    print("  F = 0.0")
    print("\n" + "=" * 50)
    
    courses = []
    
    while True:
        print("\n--- Enter Course Information ---")
        
        # Get course name
        course_name = input("\nEnter course name (or 'done' to finish): ").strip()
        
        if course_name.lower() == 'done':
            break
        
        if not course_name:
            print("Course name cannot be empty. Please try again.")
            continue
        
        # Get credits
        while True:
            try:
                credits = float(input("Enter credit hours for this course: ").strip())
                if credits <= 0:
                    print("Credits must be a positive number. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number for credits.")
        
        # Get grade
        while True:
            grade = input("Enter grade (A, B, C, D, F): ").strip()
            grade_point = get_grade_point(grade)
            
            if grade_point is None:
                print("Invalid grade. Please enter A, B, C, D, or F.")
                continue
            break
        
        # Add course to list
        courses.append({
            'name': course_name,
            'credits': credits,
            'grade': grade,
            'grade_point': grade_point
        })
        
        print(f"\n✓ Added: {course_name} - {credits} credits - Grade: {grade} ({grade_point} points)")
    
    # Display results
    if not courses:
        print("\nNo courses entered. Exiting.")
        return
    
    print("\n" + "=" * 50)
    print("SUMMARY OF COURSES")
    print("=" * 50)
    
    total_credits = 0.0
    
    for i, course in enumerate(courses, 1):
        print(f"\n{i}. {course['name']}")
        print(f"   Credits: {course['credits']}")
        print(f"   Grade: {course['grade']} ({course['grade_point']} points)")
        print(f"   Quality Points: {course['credits'] * course['grade_point']:.2f}")
        total_credits += course['credits']
    
    # Calculate and display GPA
    gpa = calculate_gpa(courses)
    
    print("\n" + "=" * 50)
    print("FINAL RESULTS")
    print("=" * 50)
    print(f"Total Credits: {total_credits:.1f}")
    print(f"Your GPA: {gpa:.2f}")
    print("=" * 50)
    
    # GPA interpretation
    if gpa >= 3.5:
        print("\n Excellent work! You're on the Dean's List!")
    elif gpa >= 3.0:
        print("\n Good job! Keep up the solid work!")
    elif gpa >= 2.0:
        print("\n You're passing. Consider studying more to improve your GPA.")
    else:
        print("\n  Your GPA is below 2.0. You may need academic support.")