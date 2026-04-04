#!/usr/bin/env node

/**
 * Photography Portfolio Auto-Preview Script
 * Automatically opens browser when code changes are detected
 */

const fs = require('fs');
const path = require('path');
const chokidar = require('chokidar');
const opn = require('opn');
const express = require('express');

// Configuration
const CONFIG = {
    port: 3000,
    host: 'localhost',
    watchPatterns: [
        '**/*.html',
        '**/*.css', 
        '**/*.js',
        '!node_modules/**'
    ],
    browser: 'default',
    debounceDelay: 1000
};

// Global variables
let browserOpened = false;
let debounceTimer = null;
let server = null;

/**
 * Display usage information
 */
function showUsage() {
    console.log(`
Photography Portfolio Auto-Preview
Usage: node preview.js [options]

Options:
  --watch, -w      Watch for file changes and auto-refresh
  --serve, -s      Start local server and open browser
  --port <number>  Specify port (default: ${CONFIG.port})
  --help, -h       Show this help message

Examples:
  node preview.js --watch      # Watch for changes
  node preview.js --serve      # Start server and open browser
  node preview.js --watch --serve --port 8080  # Combined mode
    `);
}

/**
 * Parse command line arguments
 */
function parseArgs() {
    const args = process.argv.slice(2);
    const options = {
        watch: false,
        serve: false,
        port: CONFIG.port
    };

    for (let i = 0; i < args.length; i++) {
        const arg = args[i];
        
        switch (arg) {
            case '--watch':
            case '-w':
                options.watch = true;
                break;
            case '--serve':
            case '-s':
                options.serve = true;
                break;
            case '--port':
                options.port = parseInt(args[++i], 10) || CONFIG.port;
                break;
            case '--help':
            case '-h':
                showUsage();
                process.exit(0);
            default:
                console.error(`Unknown option: ${arg}`);
                showUsage();
                process.exit(1);
        }
    }

    return options;
}

/**
 * Start local development server
 */
function startServer(port) {
    return new Promise((resolve, reject) => {
        const app = express();
        
        // Serve static files
        app.use(express.static('.'));
        
        // Handle SPA routing
        app.get('*', (req, res) => {
            const filePath = path.join(__dirname, req.path);
            
            // If file exists, serve it
            if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
                res.sendFile(filePath);
            } else {
                // Otherwise serve index.html for SPA routing
                res.sendFile(path.join(__dirname, 'index.html'));
            }
        });
        
        server = app.listen(port, CONFIG.host, (err) => {
            if (err) {
                reject(err);
            } else {
                console.log(`🚀 Server running at http://${CONFIG.host}:${port}`);
                resolve(server);
            }
        });
    });
}

/**
 * Open browser to preview site
 */
function openBrowser(port) {
    const url = `http://${CONFIG.host}:${port}`;
    
    if (!browserOpened) {
        console.log(`🌐 Opening browser: ${url}`);
        opn(url, { app: CONFIG.browser }).catch(err => {
            console.error('Failed to open browser:', err.message);
        });
        browserOpened = true;
    } else {
        console.log(`🔄 File changed, reload: ${url}`);
        // In a real implementation, you might want to send a reload signal to the browser
    }
}

/**
 * Handle file change events with debouncing
 */
function handleFileChange(event, filePath) {
    console.log(`📁 ${event}: ${path.relative(process.cwd(), filePath)}`);
    
    // Debounce to avoid multiple rapid triggers
    if (debounceTimer) {
        clearTimeout(debounceTimer);
    }
    
    debounceTimer = setTimeout(() => {
        openBrowser(CONFIG.port);
    }, CONFIG.debounceDelay);
}

/**
 * Start file watching
 */
function startWatching() {
    console.log('👀 Watching for file changes...');
    
    const watcher = chokidar.watch(CONFIG.watchPatterns, {
        ignored: /node_modules/,
        persistent: true,
        ignoreInitial: true
    });
    
    watcher
        .on('add', (path) => handleFileChange('added', path))
        .on('change', (path) => handleFileChange('changed', path))
        .on('unlink', (path) => handleFileChange('removed', path))
        .on('error', (error) => console.error('Watcher error:', error));
    
    return watcher;
}

/**
 * Cleanup function
 */
function cleanup() {
    console.log('\n🛑 Shutting down...');
    
    if (debounceTimer) {
        clearTimeout(debounceTimer);
    }
    
    if (server) {
        server.close();
    }
    
    process.exit(0);
}

/**
 * Main function
 */
async function main() {
    try {
        const options = parseArgs();
        CONFIG.port = options.port;
        
        console.log('📸 Photography Portfolio Auto-Preview');
        console.log('=====================================\n');
        
        // Start server if requested
        if (options.serve) {
            await startServer(options.port);
            openBrowser(options.port);
        }
        
        // Start watching if requested
        if (options.watch) {
            const watcher = startWatching();
            
            // Handle graceful shutdown
            process.on('SIGINT', cleanup);
            process.on('SIGTERM', cleanup);
            
            console.log('\nPress Ctrl+C to stop watching');
        } else if (!options.serve) {
            // If no mode specified, just open browser once
            openBrowser(options.port);
        }
        
    } catch (error) {
        console.error('❌ Error:', error.message);
        process.exit(1);
    }
}

// Run main function
if (require.main === module) {
    main();
}

module.exports = { main, startServer, openBrowser };