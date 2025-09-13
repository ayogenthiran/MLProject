#!/usr/bin/env python3
"""
Test script for the logger functionality
"""

from src.logger import logger

def test_logger():
    """Test different log levels"""
    print("Testing logger functionality...")
    
    # Test different log levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Test with variables
    user_name = "John Doe"
    model_accuracy = 0.95
    logger.info(f"User {user_name} trained a model with accuracy: {model_accuracy}")
    
    # Test error handling
    try:
        result = 10 / 0
    except Exception as e:
        logger.error(f"Division by zero error: {str(e)}")
    
    print("Logger test completed! Check the logs/ directory for the log file.")

if __name__ == "__main__":
    test_logger()
