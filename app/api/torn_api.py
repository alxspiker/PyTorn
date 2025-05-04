import requests


class TornAPI:
    """Class for interacting with the Torn.com API."""
    
    BASE_URL = 'https://api.torn.com'
    
    def __init__(self, api_key=None):
        """Initialize the API handler.
        
        Args:
            api_key (str, optional): The Torn API key. Can be set later.
        """
        self.api_key = api_key
    
    def set_api_key(self, api_key):
        """Set the API key.
        
        Args:
            api_key (str): The Torn API key.
        """
        self.api_key = api_key
    
    def get_player(self, player_id=''):
        """Get player information.
        
        Args:
            player_id (str, optional): The player ID. Uses '' for current player.
            
        Returns:
            dict: Player data or error message.
        """
        if not self.api_key:
            return {'error': 'API key not set'}
        
        url = f'{self.BASE_URL}/user/{player_id}?selections=basic,cooldowns,bars&key={self.api_key}'
        
        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return {'error': str(e)}
    
    def check_notifications(self):
        """Check for notifications and events.
        
        Returns:
            dict: Notification data or error message.
        """
        if not self.api_key:
            return {'error': 'API key not set'}
        
        url = f'{self.BASE_URL}/user/?selections=notifications,events&key={self.api_key}'
        
        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            return {'error': str(e)}