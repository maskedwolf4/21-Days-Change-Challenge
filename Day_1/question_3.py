"""
**Q3 - API Response Time Categorizer**
Question: Write a function that categorizes API response times into 'fast' (<100ms), 'medium' (100-500ms), 'slow' (500-1000ms), or 'critical' (>1000ms).
Input: `[45][230][780][1200][95]`
Expected Output: `['fast', 'medium', 'slow', 'critical', 'fast']`
Usage: Performance monitoring in FastAPI applications
"""

# function to monitor API Response Time

def performance_feedback(api_response_time:list) -> list:

    categories = []
    for i in api_response_time:

        if i < 100:
            categories.append("fast")
        elif i in range(100,500):
            categories.append("medium")
        elif i in range(500, 1000):
            categories.append("slow")
        else:
            categories.append("critical")

    return categories
    

feed_back = performance_feedback([45,230,780,1200,95])

print(feed_back)