from kivy.utils import platform


class TornWebView:
    """Wrapper for platform-specific WebView implementation."""
    
    def __init__(self):
        """Initialize the WebView handler based on platform."""
        self.webview = None
        
        if platform == 'android':
            self._init_android_webview()
        else:
            print("WebView is only implemented for Android currently")
    
    def _init_android_webview(self):
        """Initialize Android WebView using Pyjnius."""
        try:
            from jnius import autoclass
            
            # Android classes
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            WebChromeClient = autoclass('android.webkit.WebChromeClient')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            
            # Create WebView
            self.webview = WebView(activity)
            self.webview.setWebViewClient(WebViewClient())
            self.webview.setWebChromeClient(WebChromeClient())
            
            # Enable JavaScript
            self.webview.getSettings().setJavaScriptEnabled(True)
            
            # Enable DOM storage
            self.webview.getSettings().setDomStorageEnabled(True)
            
            # More WebView settings could be applied here
            
            # Set user agent (optional)
            user_agent = self.webview.getSettings().getUserAgentString()
            user_agent += " PyTorn/0.1.0"
            self.webview.getSettings().setUserAgentString(user_agent)
            
        except Exception as e:
            print(f"Error initializing Android WebView: {e}")
    
    def load_url(self, url):
        """Load a URL in the WebView.
        
        Args:
            url (str): The URL to load.
        """
        if self.webview:
            self.webview.loadUrl(url)
        else:
            print(f"WebView not initialized, can't load: {url}")
    
    def execute_javascript(self, script):
        """Execute JavaScript in the WebView.
        
        Args:
            script (str): JavaScript code to execute.
            
        Returns:
            bool: Success status.
        """
        if not self.webview:
            return False
        
        try:
            if platform == 'android':
                # For Android API 19+
                self.webview.evaluateJavascript(script, None)
            return True
        except Exception as e:
            print(f"Error executing JavaScript: {e}")
            return False
    
    def setup_python_bridge(self):
        """Set up the Python-JavaScript bridge."""
        # This is a placeholder - implementation will vary based on requirements
        if not self.webview:
            return
        
        # Inject bridge code
        bridge_js = """
        window.PythonBridge = {
            executePythonScript: function(scriptId) {
                // This is a placeholder - will be implemented with actual bridge
                console.log('Python script execution requested: ' + scriptId);
            },
            
            domAction: function(action, selector, value) {
                // Simple DOM manipulation helper
                var element = document.querySelector(selector);
                if (!element) return false;
                
                switch(action) {
                    case 'click':
                        element.click();
                        return true;
                    case 'setValue':
                        element.value = value;
                        return true;
                    case 'getText':
                        return element.textContent;
                    default:
                        return false;
                }
            }
        };
        """
        
        self.execute_javascript(bridge_js)