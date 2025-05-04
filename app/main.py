from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.utils import platform

# For handling Torn API
from app.api.torn_api import TornAPI

# For browser component
from app.browser.webview import TornWebView

# For script management
from app.script_manager.manager import ScriptManager


class PyTornApp(App):
    """Main application class for PyTorn."""
    
    # App title
    title = 'PyTorn'
    
    # Version info
    version = StringProperty('0.1.0')
    
    def build(self):
        """Build the application UI."""
        # Main layout
        self.layout = BoxLayout(orientation='vertical')
        
        # Header with title
        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(Label(text=f'PyTorn v{self.version}'))
        
        # API data section
        self.api_view = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.api_view.add_widget(Label(text='Torn API Data (Coming Soon)'))
        
        # Browser button
        browser_btn = Button(text='Open Torn Browser', size_hint=(1, 0.1))
        browser_btn.bind(on_press=self.open_browser)
        
        # Scripts button
        scripts_btn = Button(text='Userscripts', size_hint=(1, 0.1))
        scripts_btn.bind(on_press=self.open_scripts)
        
        # Add components to layout
        self.layout.add_widget(header)
        self.layout.add_widget(self.api_view)
        self.layout.add_widget(browser_btn)
        self.layout.add_widget(scripts_btn)
        
        return self.layout
    
    def on_start(self):
        """Initialize app components on startup."""
        # Initialize API
        self.api = TornAPI()
        
        # Initialize script manager
        self.script_manager = ScriptManager()
    
    def open_browser(self, instance):
        """Open the Torn.com browser view."""
        # In a real implementation, we would transition to a browser screen
        # For now, we'll just print a message
        print("Opening browser (not implemented yet)")
        
        # This will be implemented to show WebView
        # self.webview = TornWebView()
        # self.webview.load_url('https://torn.com')
    
    def open_scripts(self, instance):
        """Open the userscript manager."""
        # In a real implementation, we would transition to a script manager screen
        print("Opening script manager (not implemented yet)")


if __name__ == '__main__':
    PyTornApp().run()