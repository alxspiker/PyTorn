// Example JavaScript userscript for PyTorn

// ==UserScript==
// @name        Torn Quick Stats
// @description Adds a quick stats panel to Torn pages
// @match       https://www.torn.com/*
// @version     1.0
// @author      PyTorn Example
// ==UserScript==

(function() {
    'use strict';
    
    // Configuration
    const config = {
        showEnergy: true,
        showNerve: true,
        showHappy: true,
        showLife: true,
        refreshInterval: 30,  // seconds
        position: 'top-right'  // top-right, top-left, bottom-right, bottom-left
    };
    
    // CSS for the stats panel
    const panelStyle = `
        #pytorn-stats-panel {
            position: fixed;
            z-index: 9999;
            background-color: rgba(0, 0, 0, 0.8);
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            font-size: 12px;
            font-family: 'Arial', sans-serif;
        }
        #pytorn-stats-panel.top-right {
            top: 10px;
            right: 10px;
        }
        #pytorn-stats-panel.top-left {
            top: 10px;
            left: 10px;
        }
        #pytorn-stats-panel.bottom-right {
            bottom: 10px;
            right: 10px;
        }
        #pytorn-stats-panel.bottom-left {
            bottom: 10px;
            left: 10px;
        }
        .pytorn-stat {
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
        }
        .pytorn-stat-label {
            margin-right: 10px;
        }
        .pytorn-stat-value {
            font-weight: bold;
        }
        .pytorn-progress {
            height: 4px;
            width: 100%;
            background-color: #444;
            margin-top: 2px;
            border-radius: 2px;
            overflow: hidden;
        }
        .pytorn-progress-bar {
            height: 100%;
            border-radius: 2px;
        }
        .pytorn-progress-energy .pytorn-progress-bar {
            background-color: #7cc833;
        }
        .pytorn-progress-nerve .pytorn-progress-bar {
            background-color: #ff7373;
        }
        .pytorn-progress-happy .pytorn-progress-bar {
            background-color: #e3e338;
        }
        .pytorn-progress-life .pytorn-progress-bar {
            background-color: #71aad6;
        }
    `;
    
    // Create and inject the CSS
    function injectStyles() {
        const styleElement = document.createElement('style');
        styleElement.textContent = panelStyle;
        document.head.appendChild(styleElement);
    }
    
    // Create the stats panel
    function createStatsPanel() {
        const panel = document.createElement('div');
        panel.id = 'pytorn-stats-panel';
        panel.className = config.position;
        
        document.body.appendChild(panel);
        return panel;
    }
    
    // Update the stats panel with current values
    function updateStats() {
        const panel = document.getElementById('pytorn-stats-panel') || createStatsPanel();
        panel.innerHTML = '';
        
        // Get stats from the page
        const stats = getPlayerStats();
        
        // Energy
        if (config.showEnergy) {
            addStatToPanel(panel, 'Energy', stats.energy, stats.energyMax, 'energy');
        }
        
        // Nerve
        if (config.showNerve) {
            addStatToPanel(panel, 'Nerve', stats.nerve, stats.nerveMax, 'nerve');
        }
        
        // Happy
        if (config.showHappy) {
            addStatToPanel(panel, 'Happy', stats.happy, stats.happyMax, 'happy');
        }
        
        // Life
        if (config.showLife) {
            addStatToPanel(panel, 'Life', stats.life, stats.lifeMax, 'life');
        }
    }
    
    // Add a single stat to the panel
    function addStatToPanel(panel, label, value, maxValue, type) {
        const statDiv = document.createElement('div');
        statDiv.className = 'pytorn-stat';
        
        const labelSpan = document.createElement('span');
        labelSpan.className = 'pytorn-stat-label';
        labelSpan.textContent = label + ':';
        
        const valueSpan = document.createElement('span');
        valueSpan.className = 'pytorn-stat-value';
        valueSpan.textContent = `${value}/${maxValue}`;
        
        statDiv.appendChild(labelSpan);
        statDiv.appendChild(valueSpan);
        
        // Progress bar
        const progressDiv = document.createElement('div');
        progressDiv.className = `pytorn-progress pytorn-progress-${type}`;
        
        const progressBar = document.createElement('div');
        progressBar.className = 'pytorn-progress-bar';
        progressBar.style.width = `${(value / maxValue) * 100}%`;
        
        progressDiv.appendChild(progressBar);
        statDiv.appendChild(progressDiv);
        
        panel.appendChild(statDiv);
    }
    
    // Get player stats from the page
    function getPlayerStats() {
        // In a real script, we would extract these from the page
        // For this example, we'll return placeholder values
        return {
            energy: 150,
            energyMax: 160,
            nerve: 25,
            nerveMax: 50,
            happy: 5000,
            happyMax: 5000,
            life: 850,
            lifeMax: 1000
        };
    }
    
    // Initialize the script
    function initialize() {
        injectStyles();
        updateStats();
        
        // Set up periodic refresh
        setInterval(updateStats, config.refreshInterval * 1000);
    }
    
    // Run the script when the page is loaded
    if (document.readyState === 'complete') {
        initialize();
    } else {
        window.addEventListener('load', initialize);
    }
})();