# Images Directory

This directory is for storing all the photography images used in your portfolio website.

## Image Requirements

### Recommended Image Sizes

For optimal display quality and performance, use the following image sizes:

- **Hero Images**: 1200x800px (landscape orientation)
- **Project Thumbnails**: 400x300px (landscape orientation)
- **Project Gallery Images**: 800x600px (landscape orientation)
- **Profile Photo**: 400x400px (square orientation)
- **Detail Shots**: 1000x667px (landscape orientation)

### File Naming Convention

Use descriptive, consistent file names:

```
project-category-image-number.jpg
```

Examples:
- `urban-landscape-1.jpg`
- `portrait-series-2.jpg`
- `nature-wildlife-3.jpg`
- `profile-photo.jpg`

### Image Formats

- **JPEG**: Best for photographs with many colors
- **PNG**: Best for images with transparency
- **WebP**: Modern format with better compression (recommended)

## Adding Your Images

### Step 1: Prepare Your Images

1. **Resize** images to recommended dimensions
2. **Optimize** for web (compress without losing quality)
3. **Rename** files using the naming convention

### Step 2: Update HTML Files

Replace placeholder image references in HTML files:

**Homepage (`index.html`):**
```html
<!-- Change this -->
<img src="images/placeholder-1.jpg" alt="Project 1">

<!-- To this -->
<img src="images/your-project-image.jpg" alt="Your Project Title">
```

**Project Pages (`projects/`):**
```html
<!-- Change this -->
<img src="../images/urban-1.jpg" alt="Skyline at Golden Hour">

<!-- To this -->
<img src="../images/your-urban-image.jpg" alt="Your Image Description">
```

### Step 3: Image Optimization Tips

1. **Use image editing software** like Photoshop, Lightroom, or free alternatives
2. **Compress images** using tools like:
   - TinyPNG (online)
   - ImageOptim (Mac)
   - Squoosh (web-based)
3. **Maintain aspect ratio** when resizing
4. **Use descriptive alt text** for accessibility and SEO

## Sample Image Structure

Here's how you might organize your images:

```
images/
├── hero-background.jpg      # Main hero image
├── profile-photo.jpg        # About page profile
├── urban-landscape-1.jpg    # Urban project images
├── urban-landscape-2.jpg
├── urban-landscape-3.jpg
├── nature-wildlife-1.jpg    # Nature project images
├── nature-wildlife-2.jpg
├── portrait-series-1.jpg    # Portrait project images
└── portrait-series-2.jpg
```

## Performance Considerations

- **File Size**: Keep images under 500KB each
- **Lazy Loading**: Already implemented - images load as you scroll
- **Responsive Images**: Consider using `srcset` for different screen sizes
- **CDN**: For high traffic, consider using a CDN for image delivery

## Copyright and Licensing

- Only use images you have the rights to publish
- Consider adding watermarks if appropriate
- Respect copyright laws for commercial use

## Tools for Image Management

### Free Tools
- **GIMP**: Advanced image editing
- **Paint.NET**: Simple image editing
- **Canva**: Easy online design
- **Photopea**: Free online Photoshop alternative

### Professional Tools
- **Adobe Photoshop**: Industry standard
- **Adobe Lightroom**: Photo management and editing
- **Capture One**: Professional photo editing

## Troubleshooting

### Common Issues

1. **Images not displaying**: Check file paths and names
2. **Slow loading**: Compress images further
3. **Poor quality**: Use higher resolution source images
4. **Wrong aspect ratio**: Maintain original proportions when resizing

### Best Practices

1. **Backup original files** before editing
2. **Keep organized** with consistent naming
3. **Test on different devices** for responsiveness
4. **Monitor page load times** with browser dev tools

---

**Remember**: Your photography is the heart of this portfolio. Take the time to select and prepare your best work for the best presentation!