from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool
import random

@tool
def qualify_pay_adjustment(employee_name: str, adjustment_type: str):
    """
    Mock function to simulate checking if an employee qualifies for a pay adjustment. 
    
    Args:
        employee_name (str): The employee's name
        adjustment_type (str): Type of adjustment ("Relocation", "Raise", etc)
    
    Returns:
        dict: Simplified response simulating backend qualification results
    """
    review_date = datetime.now()

    return {
        "message": f"Qualification check complete for {employee_name}.",
        "data": {
            "employee_name": employee_name,
            "review_date": review_date.isoformat(),
            "adjustment_type": adjustment_type.upper(),
            "qualified": True,
            "evaluated_at": datetime.now().isoformat() + "Z"
        }
    }
