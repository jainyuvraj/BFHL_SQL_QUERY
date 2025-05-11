import requests
import json
from datetime import datetime

def make_api_call(access_token, sql_query):
    
    url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    
   
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    
    # Request body
    payload = {
        "finalQuery": sql_query
    }
    
  
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
      
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
   
    access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDUzIyMTMxMSIsIm5hbWUiOiJZdXZyYWogamFpbiIsImVtYWlsIjoieXV2cmFqamFpbjIyMDMzNkBhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjM4ODQsImV4cCI6MTc0Njk2NDc4NH0.sTlHlDFv6znPknWszhqol3y7xbmvXOjkN5WWYwnBcDk"
    
  
    sql_query = "SELECT p.AMOUNT AS SALARY, CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME, TIMESTAMPDIFF(YEAR, e.DOB, CURRENT_DATE()) AS AGE, d.DEPARTMENT_NAME FROM PAYMENTS p JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID WHERE DAY(p.PAYMENT_TIME) != 1 ORDER BY p.AMOUNT DESC LIMIT 1"
    
    
  
    result = make_api_call(access_token, sql_query)
    
 
    print(json.dumps(result, indent=4))
