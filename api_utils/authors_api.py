from api_utils.base_api import BaseAPI

class AuthorsAPI(BaseAPI):
    def __init__(self, base_url: str):
        super().__init__(base_url)
    def create_author(self, author_payload: dict):
        """
        Sends a POST request to create a new author.
        """
        return self.post("/api/v1/Authors", json=author_payload)

    def get_author(self, author_id: int):
        """
        Sends a GET request to retrieve an author by ID.
        """
        return self.get(f"/api/v1/Authors/{author_id}")

    def delete_author(self, author_id: int):
        """
        Sends a DELETE request to remove an author by ID.
        """
        return self.delete(f"/api/v1/Authors/{author_id}")
