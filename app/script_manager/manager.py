import os
import json
import time


class ScriptManager:
    """Manager for user scripts (JavaScript and Python)."""
    
    def __init__(self, scripts_dir=None):
        """Initialize the script manager.
        
        Args:
            scripts_dir (str, optional): Directory for storing scripts.
                Defaults to app storage location.
        """
        # Set default scripts directory
        if scripts_dir is None:
            from kivy.app import App
            app = App.get_running_app()
            self.scripts_dir = os.path.join(app.user_data_dir, 'scripts')
        else:
            self.scripts_dir = scripts_dir
        
        # Ensure directories exist
        self.js_dir = os.path.join(self.scripts_dir, 'js')
        self.py_dir = os.path.join(self.scripts_dir, 'python')
        
        os.makedirs(self.js_dir, exist_ok=True)
        os.makedirs(self.py_dir, exist_ok=True)
        
        # Load script metadata
        self.scripts = self._load_scripts()
    
    def _load_scripts(self):
        """Load script metadata from disk.
        
        Returns:
            dict: Scripts metadata.
        """
        metadata_path = os.path.join(self.scripts_dir, 'metadata.json')
        
        if not os.path.exists(metadata_path):
            # Create default metadata file
            default_metadata = {
                'js': {},
                'python': {}
            }
            with open(metadata_path, 'w') as f:
                json.dump(default_metadata, f)
            return default_metadata
        
        try:
            with open(metadata_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading scripts metadata: {e}")
            return {'js': {}, 'python': {}}
    
    def save_metadata(self):
        """Save script metadata to disk."""
        metadata_path = os.path.join(self.scripts_dir, 'metadata.json')
        
        try:
            with open(metadata_path, 'w') as f:
                json.dump(self.scripts, f)
        except Exception as e:
            print(f"Error saving scripts metadata: {e}")
    
    def add_script(self, name, script_type, code, description='', enabled=True):
        """Add a new script.
        
        Args:
            name (str): Script name.
            script_type (str): Script type ('js' or 'python').
            code (str): Script code content.
            description (str, optional): Script description.
            enabled (bool, optional): Whether script is enabled by default.
            
        Returns:
            str: Script ID if successful, None otherwise.
        """
        if script_type not in ['js', 'python']:
            return None
        
        # Generate a unique ID
        import uuid
        script_id = str(uuid.uuid4())
        
        # Save script file
        target_dir = self.js_dir if script_type == 'js' else self.py_dir
        file_ext = '.js' if script_type == 'js' else '.py'
        
        script_path = os.path.join(target_dir, f"{script_id}{file_ext}")
        
        try:
            with open(script_path, 'w') as f:
                f.write(code)
            
            # Update metadata
            self.scripts[script_type][script_id] = {
                'name': name,
                'description': description,
                'enabled': enabled,
                'created': time.time(),
                'modified': time.time()
            }
            
            self.save_metadata()
            return script_id
            
        except Exception as e:
            print(f"Error adding script: {e}")
            return None
    
    def get_script(self, script_id, script_type):
        """Get a script by ID.
        
        Args:
            script_id (str): Script ID.
            script_type (str): Script type ('js' or 'python').
            
        Returns:
            tuple: (metadata, code) if successful, (None, None) otherwise.
        """
        if script_type not in ['js', 'python']:
            return None, None
        
        if script_id not in self.scripts[script_type]:
            return None, None
        
        metadata = self.scripts[script_type][script_id]
        
        # Get script code
        target_dir = self.js_dir if script_type == 'js' else self.py_dir
        file_ext = '.js' if script_type == 'js' else '.py'
        script_path = os.path.join(target_dir, f"{script_id}{file_ext}")
        
        try:
            with open(script_path, 'r') as f:
                code = f.read()
            return metadata, code
        except Exception as e:
            print(f"Error reading script: {e}")
            return metadata, None
    
    def update_script(self, script_id, script_type, code=None, metadata_updates=None):
        """Update an existing script.
        
        Args:
            script_id (str): Script ID.
            script_type (str): Script type ('js' or 'python').
            code (str, optional): New script code.
            metadata_updates (dict, optional): Metadata fields to update.
            
        Returns:
            bool: Success status.
        """
        if script_type not in ['js', 'python']:
            return False
        
        if script_id not in self.scripts[script_type]:
            return False
        
        # Update code if provided
        if code is not None:
            target_dir = self.js_dir if script_type == 'js' else self.py_dir
            file_ext = '.js' if script_type == 'js' else '.py'
            script_path = os.path.join(target_dir, f"{script_id}{file_ext}")
            
            try:
                with open(script_path, 'w') as f:
                    f.write(code)
            except Exception as e:
                print(f"Error updating script code: {e}")
                return False
        
        # Update metadata if provided
        if metadata_updates and isinstance(metadata_updates, dict):
            for key, value in metadata_updates.items():
                if key != 'created':  # Don't allow changing creation time
                    self.scripts[script_type][script_id][key] = value
            
            # Update modification time
            self.scripts[script_type][script_id]['modified'] = time.time()
            
            self.save_metadata()
        
        return True
    
    def delete_script(self, script_id, script_type):
        """Delete a script.
        
        Args:
            script_id (str): Script ID.
            script_type (str): Script type ('js' or 'python').
            
        Returns:
            bool: Success status.
        """
        if script_type not in ['js', 'python']:
            return False
        
        if script_id not in self.scripts[script_type]:
            return False
        
        # Delete script file
        target_dir = self.js_dir if script_type == 'js' else self.py_dir
        file_ext = '.js' if script_type == 'js' else '.py'
        script_path = os.path.join(target_dir, f"{script_id}{file_ext}")
        
        try:
            if os.path.exists(script_path):
                os.remove(script_path)
            
            # Remove from metadata
            del self.scripts[script_type][script_id]
            self.save_metadata()
            
            return True
        except Exception as e:
            print(f"Error deleting script: {e}")
            return False
    
    def list_scripts(self, script_type=None):
        """List available scripts.
        
        Args:
            script_type (str, optional): Filter by script type ('js' or 'python').
                If None, return all scripts.
                
        Returns:
            dict: Scripts organized by type.
        """
        if script_type is None:
            return self.scripts
        
        if script_type in ['js', 'python']:
            return {script_type: self.scripts[script_type]}
        
        return {}