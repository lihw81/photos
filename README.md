# Photography Portfolio Website

A modern, responsive photography portfolio website built with HTML, CSS, and JavaScript. Perfect for showcasing your photography projects and connecting with clients.

## Features

- **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations and transitions
- **Project Gallery**: Organized project showcase with detailed project pages
- **Contact Form**: Functional contact form with validation
- **Fast Loading**: Optimized for performance with lazy loading images
- **SEO Friendly**: Proper HTML structure and meta tags for search engine optimization
- **Auto-Preview**: Automatic browser refresh on code changes

## Auto-Preview Feature

The project includes an automated preview system that:

- **Watches for file changes** in HTML, CSS, and JavaScript files
- **Automatically opens browser** when changes are detected
- **Provides live reload** functionality during development
- **Includes local server** for testing

### Quick Start

```bash
# Install dependencies
npm install

# Start auto-preview with file watching
npm run dev

# Or start server only
npm run serve

# Or open browser once
npm run preview
```

### Manual Usage

```bash
# Watch for changes and auto-refresh
node preview.js --watch

# Start local server and open browser
node preview.js --serve

# Combined mode (recommended for development)
node preview.js --watch --serve

# Custom port
node preview.js --watch --serve --port 8080
```

## File Structure

```
homepage/
├── index.html              # Main homepage
├── about.html              # About page
├── contact.html            # Contact page
├── projects/               # Projects directory
│   ├── index.html          # Projects overview page
│   └── urban.html          # Sample project detail page
├── styles/                 # CSS styles directory
│   └── main.css            # Main stylesheet
├── js/                     # JavaScript directory
│   └── main.js             # Main JavaScript file
├── preview.js              # Auto-preview script
├── package.json            # Project dependencies
├── images/                 # Images directory
└── README.md               # This file
```

## Getting Started

### Prerequisites

- Node.js (version 14.0.0 or higher)
- A web browser (Chrome, Firefox, Safari, etc.)
- A text editor (VS Code, Sublime Text, etc.)

### Installation

1. Clone or download this project to your local machine
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the auto-preview system:
   ```bash
   npm run dev
   ```
4. The browser will automatically open and refresh on file changes

### Development Workflow

1. **Start development**: Run `npm run dev`
2. **Make changes**: Edit HTML, CSS, or JavaScript files
3. **Auto-refresh**: Browser automatically updates
4. **Test**: Verify changes in the browser
5. **Repeat**: Continue development with instant feedback

## Customization Guide

### 1. Update Personal Information

**About Page (`about.html`):**
- Replace `[Your Name]` with your actual name
- Update the biography and experience sections
- Modify the equipment list to match your gear
- Add your actual awards and recognition

**Contact Page (`contact.html`):**
- Update email, phone number, and address
- Replace social media handles with your actual profiles
- Modify the services offered section

### 2. Add Your Projects

**Homepage (`index.html`):**
- Update the featured projects section
- Replace placeholder images with your actual photos
- Modify project titles and descriptions

**Projects Page (`projects/index.html`):**
- Add or remove project cards as needed
- Update project images, titles, and descriptions
- Create new project detail pages for each project

**Project Detail Pages (`projects/`):**
- Use `urban.html` as a template for new projects
- Replace placeholder content with your project details
- Add your actual project images

### 3. Customize Styling

**Colors and Themes (`styles/main.css`):**
- Modify CSS variables to change color schemes
- Adjust fonts and typography
- Customize spacing and layout

#### 4. Add Your Images

1. Create an `images` folder in the root directory
2. Add your photography images to this folder
3. Update image references in HTML files to point to your actual images

Recommended image sizes:
- Project thumbnails: 400x300px
- Project gallery images: 800x600px
- Hero images: 1200x800px
- Profile image: 400x400px

## Auto-Preview Script Details

The `preview.js` script provides the following features:

### File Watching
- Monitors HTML, CSS, and JavaScript files
- Excludes node_modules directory
- Uses debouncing to prevent rapid triggers

### Local Server
- Serves static files from project root
- Handles SPA routing for clean URLs
- Configurable port (default: 3000)

### Browser Integration
- Automatically opens default browser
- Provides visual feedback for file changes
- Supports graceful shutdown

### Command Line Options

```bash
# Display help
node preview.js --help

# Watch mode only
node preview.js --watch

# Server mode only
node preview.js --serve

# Combined mode (recommended)
node preview.js --watch --serve

# Custom port
node preview.js --watch --serve --port 8080
```

## Deployment

### Local Testing

1. Open `index.html` in your web browser
2. Test all navigation links and forms
3. Check responsiveness on different screen sizes

### Web Hosting

You can deploy this website to any web hosting service:

- **GitHub Pages**: Free hosting for static websites
- **Netlify**: Easy deployment with continuous integration
- **Vercel**: Fast deployment for static sites
- **Traditional web hosting**: Upload files via FTP

**Note**: The auto-preview script is for development only and should not be deployed to production.

## Browser Support

This website supports all modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Tips

1. **Optimize Images**: Compress images before uploading
2. **Lazy Loading**: Images load as you scroll (already implemented)
3. **Minify CSS/JS**: Consider minifying files for production
4. **CDN Usage**: Use CDN for fonts and libraries

## Troubleshooting

### Auto-Preview Issues

1. **Browser doesn't open**: Check if port 3000 is available
2. **Changes not detected**: Verify file patterns in watch configuration
3. **Server errors**: Check console for specific error messages

### Common Issues

1. **Images not displaying**: Check file paths and names
2. **Slow loading**: Compress images further
3. **Poor quality**: Use higher resolution source images
4. **Wrong aspect ratio**: Maintain original proportions when resizing

## Support

If you need help customizing this template:

1. Check the HTML comments for guidance
2. Refer to the CSS classes and structure
3. Test changes in small increments
4. Use browser developer tools for debugging

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Photographing!** 📸

Remember to replace all placeholder content with your actual photography work and personal information to make this portfolio truly yours.