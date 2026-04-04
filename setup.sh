#!/bin/bash

# Photography Portfolio Setup Script
# Automatically installs dependencies and starts the preview system

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="Photography Portfolio"
NODE_VERSION="14.0.0"
PORT="3000"

# Print colored output
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if Node.js is installed
check_nodejs() {
    if command -v node >/dev/null 2>&1; then
        NODE_VERSION_ACTUAL=$(node --version | sed 's/v//')
        print_success "Node.js found: v$NODE_VERSION_ACTUAL"
        
        # Check if version is sufficient
        if [ "$(printf '%s\n' "$NODE_VERSION" "$NODE_VERSION_ACTUAL" | sort -V | head -n1)" = "$NODE_VERSION" ]; then
            print_success "Node.js version is sufficient"
        else
            print_warning "Node.js version $NODE_VERSION_ACTUAL is older than recommended $NODE_VERSION"
        fi
    else
        print_error "Node.js is not installed"
        print_info "Please install Node.js from https://nodejs.org/"
        exit 1
    fi
}

# Check if npm is installed
check_npm() {
    if command -v npm >/dev/null 2>&1; then
        NPM_VERSION=$(npm --version)
        print_success "npm found: v$NPM_VERSION"
    else
        print_error "npm is not installed"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_info "Installing dependencies..."
    
    if [ -f "package.json" ]; then
        npm install
        if [ $? -eq 0 ]; then
            print_success "Dependencies installed successfully"
        else
            print_error "Failed to install dependencies"
            exit 1
        fi
    else
        print_error "package.json not found"
        exit 1
    fi
}

# Check if port is available
check_port() {
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null; then
        print_warning "Port $PORT is already in use"
        read -p "Would you like to use a different port? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            read -p "Enter port number: " PORT
        fi
    else
        print_success "Port $PORT is available"
    fi
}

# Start the preview system
start_preview() {
    print_info "Starting preview system on port $PORT..."
    print_info "Press Ctrl+C to stop the preview"
    echo
    
    # Start the preview with both watch and serve modes
    node preview.js --watch --serve --port $PORT
}

# Main function
main() {
    echo -e "${BLUE}=====================================${NC}"
    echo -e "${BLUE}   $PROJECT_NAME Setup Script${NC}"
    echo -e "${BLUE}=====================================${NC}"
    echo
    
    # Check prerequisites
    check_nodejs
    check_npm
    
    # Install dependencies
    install_dependencies
    
    # Check port availability
    check_port
    
    echo
    echo -e "${GREEN}🎉 Setup completed successfully!${NC}"
    echo
    
    # Ask if user wants to start preview
    read -p "Would you like to start the preview system now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        start_preview
    else
        print_info "You can start the preview later with: npm run dev"
        print_info "Or manually with: node preview.js --watch --serve"
    fi
}

# Help function
show_help() {
    echo "Usage: ./setup.sh [options]"
    echo
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  -p, --port     Specify port number (default: 3000)"
    echo
    echo "Examples:"
    echo "  ./setup.sh                    # Use default port 3000"
    echo "  ./setup.sh --port 8080        # Use custom port"
    echo "  ./setup.sh --help             # Show help"
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        *)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
    shift

done

# Run main function
main