import os
import json
from datetime import datetime

def test_personal_learning_tutor():
    """
    Run a series of tests to verify the functionality of the Personal Learning Tutor GPT.
    """
    print("=== Personal Learning Tutor GPT - System Test ===")
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Running tests for core functionality and customization features...")
    
    # Import the necessary modules
    try:
        from core_functionality import PersonalLearningTutorGPT, TeachingStyle, ToneStyle, DifficultyLevel
        from customization_features import EnhancedPersonalLearningTutorGPT, LearningStyle, ContentFormat
        print("✓ Successfully imported modules")
    except ImportError as e:
        print(f"✗ Failed to import modules: {e}")
        return False
    
    # Test 1: Initialize the tutor
    try:
        tutor = EnhancedPersonalLearningTutorGPT()
        print("✓ Successfully initialized tutor")
    except Exception as e:
        print(f"✗ Failed to initialize tutor: {e}")
        return False
    
    # Test 2: Create user profile
    try:
        user_id = "test_user_001"
        tutor.create_user_profile(user_id, {
            "teaching_style": TeachingStyle.SOCRATIC.value,
            "tone_style": ToneStyle.FRIENDLY.value,
            "difficulty_level": DifficultyLevel.BEGINNER.value,
            "learning_style": LearningStyle.VISUAL.value,
            "content_format": ContentFormat.STEP_BY_STEP.value
        })
        print("✓ Successfully created user profile")
    except Exception as e:
        print(f"✗ Failed to create user profile: {e}")
        return False
    
    # Test 3: Process content
    try:
        sample_content = """
        # Introduction to Python
        
        Python is a high-level, interpreted programming language known for its readability and simplicity.
        
        ## Variables
        
        Variables in Python are created when you assign a value to them:
        
        ```python
        x = 10
        name = "Python"
        ```
        
        ## Control Flow
        
        Python supports standard control flow statements:
        
        ```python
        if x > 5:
            print("x is greater than 5")
        else:
            print("x is not greater than 5")
        ```
        """
        
        content_id = tutor.process_content(
            sample_content, 
            "notes", 
            {"author": "Test Author", "title": "Python Basics"}
        )
        
        print(f"✓ Successfully processed content with ID: {content_id}")
    except Exception as e:
        print(f"✗ Failed to process content: {e}")
        return False
    
    # Test 4: Generate explanation with template
    try:
        explanation = tutor.generate_explanation_with_template(
            user_id,
            "Python Variables",
            "explanation",
            "beginner"
        )
        
        print("✓ Successfully generated explanation with template")
        print("  Template keys: " + ", ".join(explanation.keys()))
    except Exception as e:
        print(f"✗ Failed to generate explanation with template: {e}")
        return False
    
    # Test 5: Create custom template
    try:
        custom_template = {
            "title": "Let's Learn About {concept}",
            "introduction": "I'm excited to teach you about {concept}!",
            "explanation": "{content}",
            "summary": "To wrap up our discussion on {concept}: {summary}",
            "next_steps": "Ready to practice? {next_steps}"
        }
        
        success = tutor.create_custom_template(user_id, "explanation", "enthusiastic", custom_template)
        
        if success:
            print("✓ Successfully created custom template")
        else:
            print("✗ Failed to create custom template")
            return False
    except Exception as e:
        print(f"✗ Failed to create custom template: {e}")
        return False
    
    # Test 6: Generate explanation with custom template
    try:
        custom_explanation = tutor.generate_explanation_with_template(
            user_id,
            "Python Control Flow",
            "explanation",
            "enthusiastic"
        )
        
        print("✓ Successfully generated explanation with custom template")
        print("  Template keys: " + ", ".join(custom_explanation.keys()))
    except Exception as e:
        print(f"✗ Failed to generate explanation with custom template: {e}")
        return False
    
    # Test 7: Process input with preferences
    try:
        response = tutor.process_input_with_preferences(
            user_id,
            "Can you explain Python functions?"
        )
        
        print("✓ Successfully processed input with preferences")
        print(f"  Response type: {type(response)}")
    except Exception as e:
        print(f"✗ Failed to process input with preferences: {e}")
        return False
    
    # Test 8: Save and load user profile
    try:
        # Create profiles directory if it doesn't exist
        os.makedirs("./profiles", exist_ok=True)
        
        # Save profile
        profile_path = tutor.save_user_profile(user_id, "./profiles")
        print(f"✓ Successfully saved user profile to: {profile_path}")
        
        # Create a new tutor instance
        new_tutor = EnhancedPersonalLearningTutorGPT()
        
        # Load the profile
        success = new_tutor.load_user_profile(user_id, profile_path)
        
        if success:
            print("✓ Successfully loaded user profile")
        else:
            print("✗ Failed to load user profile")
            return False
    except Exception as e:
        print(f"✗ Failed during profile save/load: {e}")
        return False
    
    print("\nAll tests completed successfully!")
    print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

if __name__ == "__main__":
    test_personal_learning_tutor()
