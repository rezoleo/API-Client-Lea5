class ApiError(Exception):
    """Custom exception class for API errors."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Error {status_code}: {message}")