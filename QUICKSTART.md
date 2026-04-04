# Quick Start Guide

Get your photography portfolio website up and running in minutes.

## Prerequisites

- Node.js 14.0.0 or higher
- npm (comes with Node.js)

## Quick Setup

### Option 1: Automated Setup (Recommended)

```bash
# Make the setup script executable (if needed)
chmod +x setup.sh

# Run the automated setup
./setup.sh
```

The script will:
- Check Node.js and npm versions
- Install all dependencies
- Start the preview system automatically

### Option 2: Manual Setup

```bash
# Install dependencies
npm install

# Start development server with auto-refresh
npm run dev
```

## Usage

### Development Commands

```bash
# Start with file watching and auto-refresh (recommended)
npm run dev

# Start local server only
npm run serve

# Open browser once (no watching)
npm run preview

# Manual commands with custom options
node preview.js --watch --serve --port 8080
```

### File Structure Overview

```
├── index.html          # Homepage
├── about.html          # About page  
├── contact.html        # Contact page
├── projects/           # Project pages
├── styles/main.css     # All styles
├── js/main.js          # JavaScript
├── images/             # Your photos
└── preview.js          # Auto-preview script
```

### Customization Steps

1. **Replace placeholder content** in HTML files
2. **Add your photos** to the `images/` folder
3. **Update contact information** in `contact.html`
4. **Modify colors and styles** in `styles/main.css`

### Auto-Preview Features

- ✅ **File watching**: Automatically detects changes
- ✅ **Browser refresh**: Updates browser on save
- ✅ **Local server**: Serves files locally
- ✅ **SPA routing**: Handles clean URLs
- ✅ **Error handling**: Graceful error messages

## Next Steps

1. Open the browser (should open automatically)
2. Start editing files in your code editor
3. See changes instantly in the browser
4. Customize the design and content
5. Deploy when ready

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
node preview.js --port 8080
```

**Dependencies not installing:**
```bash
rm -rf node_modules package-lock.json
npm install
```

**Browser not opening:**
- Check if pop-ups are blocked
- Manually visit: http://localhost:3000

## Deployment

When ready to deploy:

1. Remove development files:
   ```bash
   rm preview.js package.json package-lock.json setup.sh
   ```

2. Upload to your web host

## Support

- Check browser console for errors
- Verify file paths and names
- Test on different screen sizes

---

**Ready to start? Run `./setup.sh` and begin customizing!**