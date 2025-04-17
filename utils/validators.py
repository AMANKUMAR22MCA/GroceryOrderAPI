from fastapi import HTTPException

def raise_not_found(message):
    """
    Raises an HTTPException with a 404 (Not Found) status code.
    
    Args:
        message (str): The error message to be returned in the response.
        
    Raises:
        HTTPException: A 404 error with the provided message.
    """
    raise HTTPException(status_code=404, detail=message)

def raise_bad_request(message):
    """
    Raises an HTTPException with a 400 (Bad Request) status code.
    
    Args:
        message (str): The error message to be returned in the response.
        
    Raises:
        HTTPException: A 400 error with the provided message.
    """
    raise HTTPException(status_code=400, detail=message)
